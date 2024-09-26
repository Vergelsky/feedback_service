from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, StateFilter
from aiogram import F
from aiogram import html, types
from keyboards import get_start_survey_kb, BUTTONS_TEXTS, get_answers_kb
from servicies import get_survey, get_irrelevant_message_text, send_answers

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state

router = Router()


class FSMSurveyState(StatesGroup):
    answers = State()


# Обработка команды старт
@router.message(CommandStart(), StateFilter(default_state))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Здравствуйте, {html.bold(message.from_user.full_name)}!\n"
                         f"Пройдите наш опрос!",
                         reply_markup=get_start_survey_kb())


# Обработка команды старт во время ответа на вопрос
@router.message(CommandStart(), StateFilter(FSMSurveyState.answers))
async def command_start_in_progress_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Мы уже начали, завершите опрос, пожалуйста!")
    await ask_question(message, state)


# Обработка нажатия кнопки "Начать опрос"
@router.message(F.text == BUTTONS_TEXTS['start_survey'], StateFilter(default_state))
async def start_survey_handler(message: Message, state: FSMContext):
    survey_data = await get_survey()

    if survey_data:
        await state.update_data(survey_data=survey_data, answers={})
        await state.update_data(current_question_index=0)
        await state.update_data(answers=[])
        await message.answer(f"{survey_data['title']}\n\n{survey_data['description']}")
        await ask_question(message, state)
    else:
        await message.answer("Извините, опрос временно не доступен, попробуйте позже!",
                             reply_markup=get_start_survey_kb())


# Обработка нажатия кнопки "Начать опрос" во время опроса
@router.message(F.text == BUTTONS_TEXTS['start_survey'], StateFilter(FSMSurveyState.answers))
async def start_survey_in_progress_handler(message: Message, state: FSMContext):
        await message.answer("Опрос уже запущен, пожалуйста, завершите его!")
        await ask_question(message, state)


# Обработка нажатия кнопки ответа на вопрос
@router.callback_query(StateFilter(FSMSurveyState.answers))
async def answers_handler(call: CallbackQuery, state: FSMContext):
    await save_answer_and_next_question(call, state)


@router.message(StateFilter(FSMSurveyState.answers))
async def irrelevant_message_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Пожалуйста, завершите прохождение опроса!")
    await ask_question(message, state)


@router.message()
async def irrelevant_message_handler(message: Message) -> None:
    await message.answer(get_irrelevant_message_text(message), reply_markup=get_start_survey_kb())


async def ask_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    survey_data = data.get('survey_data')
    current_question_index = data.get('current_question_index')

    if current_question_index >= len(survey_data['questions']):
        await finish_survey(message, state)
        return

    question = survey_data['questions'][current_question_index]
    question_full_text = f'{question['text']}:\n'
    for i in range(len(question['choices'])):
        question_full_text += f'{i + 1}. {question["choices"][i]["text"]}\n'

    # Коллбек для каждого варианта начинаем с номера вопроса (q_0_1, q_0_2, ...)
    for choice in question['choices']:
        choice['callback_choice'] = f'q_{question["id"]}_{str(choice["id"])}'

    print(question['choices'])

    await message.answer(question_full_text, reply_markup=get_answers_kb(question['choices']))

    await state.set_state(FSMSurveyState.answers)


async def save_answer_and_next_question(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    survey_data = data.get('survey_data')
    current_question_index = data.get('current_question_index')
    current_question_id = survey_data['questions'][current_question_index]['id']

    print('survey_data', survey_data, 'current_question_index', current_question_index, 'current_question_id', current_question_id)

    # Извлекаем номер вопроса и выбранный вариант из callack_data ('q_0_1')
    call_data_splitted = call.data.split('_')
    question_data, choice_data = call_data_splitted[1], call_data_splitted[-1]

    print('question_data', question_data, 'choice_data', choice_data)

    if question_data != str(current_question_id):
        await call.answer("Выберите один из актуальных вариантов!")
        return

    result = {'question': current_question_id, "choice": int(choice_data)}
    answers = data.get('answers')
    answers.append(result)
    await state.update_data(answers=answers)

    await state.update_data(current_question_index=current_question_index + 1)
    await call.answer()
    await ask_question(call.message, state)


async def finish_survey(message: types.Message, state: FSMContext):
    data = await state.get_data()
    # Вид ответов: {'survey_id': 1, 'client': 31234141342, 'responses': [{'question_id': 1, 'choise_id': 1}, {'question_id': 2, 'choise_id': 2}]}
    survey_data = data.get('survey_data')
    client = message.from_user.id
    answers = data.get('answers')
    response = {'survey': survey_data['id'], 'client': client, 'responses': answers}
    await send_answers(response)
    await state.clear()
    await message.answer("Опрос завершен!\n"
                         "Спасибо за участие!", reply_markup=get_start_survey_kb())

