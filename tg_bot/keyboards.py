from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

BUTTONS_TEXTS = {'start_survey': 'Давайте ваш опрос!'}


def get_start_survey_kb():
    button_need_survey = KeyboardButton(text=BUTTONS_TEXTS['start_survey'])
    need_survey_builder = ReplyKeyboardBuilder()
    need_survey_builder.row(button_need_survey)
    return need_survey_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)


def get_answers_kb(choices):
    answers_builder = InlineKeyboardBuilder()
    for i in range(len(choices)):
        print(f'{i + 1}. {choices[i]["text"]}', str(choices[i]['callback_choice']))
        answers_builder.row(InlineKeyboardButton(text=f'{i + 1}. {choices[i]["text"]}',
                                                 callback_data=str(choices[i]['callback_choice'])))
        answers_builder.adjust(1)
    return answers_builder.as_markup()
