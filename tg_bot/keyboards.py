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
    for choice in choices:
        answers_builder.row(InlineKeyboardButton(text=choice['text'], callback_data=str(choice['id'])))
        answers_builder.adjust(2)
    return answers_builder.as_markup()


# CallBackQuery

# id = '3536177471614819887'
# from_user = User(id=823330476, is_bot=False, first_name='Дмитрий', last_name='Игоревич', username='Graf_Werger',
#                  language_code='ru', is_premium=None, added_to_attachment_menu=None, can_join_groups=None,
#                  can_read_all_group_messages=None, supports_inline_queries=None, can_connect_to_business=None,
#                  has_main_web_app=None)
# chat_instance = '-4915928284669987658'
# message = Message(message_id=216, date=datetime.datetime(2024, 9, 13, 4, 10, 51, tzinfo=TzInfo(UTC)),
#                   chat=Chat(id=823330476, type='private', title=None, username='Graf_Werger', first_name='Дмитрий',
#                             last_name='Игоревич', is_forum=None, accent_color_id=None, active_usernames=None,
#                             available_reactions=None, background_custom_emoji_id=None, bio=None, birthdate=None,
#                             business_intro=None, business_location=None, business_opening_hours=None,
#                             can_set_sticker_set=None, custom_emoji_sticker_set_name=None, description=None,
#                             emoji_status_custom_emoji_id=None, emoji_status_expiration_date=None,
#                             has_aggressive_anti_spam_enabled=None, has_hidden_members=None, has_private_forwards=None,
#                             has_protected_content=None, has_restricted_voice_and_video_messages=None,
#                             has_visible_history=None, invite_link=None, join_by_request=None,
#                             join_to_send_messages=None, linked_chat_id=None, location=None,
#                             message_auto_delete_time=None, permissions=None, personal_chat=None, photo=None,
#                             pinned_message=None, profile_accent_color_id=None, profile_background_custom_emoji_id=None,
#                             slow_mode_delay=None, sticker_set_name=None, unrestrict_boost_count=None),
#                   message_thread_id=None,
#                   from_user=User(id=7199411932, is_bot=True, first_name='Тестовый бот', last_name=None,
#                                  username='lookup_t_0_0_bot', language_code=None, is_premium=None,
#                                  added_to_attachment_menu=None, can_join_groups=None, can_read_all_group_messages=None,
#                                  supports_inline_queries=None, can_connect_to_business=None, has_main_web_app=None),
#                   sender_chat=None, sender_boost_count=None, sender_business_bot=None, business_connection_id=None,
#                   forward_origin=None, is_topic_message=None, is_automatic_forward=None, reply_to_message=None,
#                   external_reply=None, quote=None, reply_to_story=None, via_bot=None, edit_date=None,
#                   has_protected_content=None, is_from_offline=None, media_group_id=None, author_signature=None,
#                   text='Вопрос 1', entities=None, link_preview_options=None, effect_id=None, animation=None, audio=None,
#                   document=None, paid_media=None, photo=None, sticker=None, story=None, video=None, video_note=None,
#                   voice=None, caption=None, caption_entities=None, show_caption_above_media=None,
#                   has_media_spoiler=None, contact=None, dice=None, game=None, poll=None, venue=None, location=None,
#                   new_chat_members=None, left_chat_member=None, new_chat_title=None, new_chat_photo=None,
#                   delete_chat_photo=None, group_chat_created=None, supergroup_chat_created=None,
#                   channel_chat_created=None, message_auto_delete_timer_changed=None, migrate_to_chat_id=None,
#                   migrate_from_chat_id=None, pinned_message=None, invoice=None, successful_payment=None,
#                   refunded_payment=None, users_shared=None, chat_shared=None, connected_website=None,
#                   write_access_allowed=None, passport_data=None, proximity_alert_triggered=None, boost_added=None,
#                   chat_background_set=None, forum_topic_created=None, forum_topic_edited=None, forum_topic_closed=None,
#                   forum_topic_reopened=None, general_forum_topic_hidden=None, general_forum_topic_unhidden=None,
#                   giveaway_created=None, giveaway=None, giveaway_winners=None, giveaway_completed=None,
#                   video_chat_scheduled=None, video_chat_started=None, video_chat_ended=None,
#                   video_chat_participants_invited=None, web_app_data=None, reply_markup=InlineKeyboardMarkup(
#         inline_keyboard=[[InlineKeyboardButton(text='Вариант 1 1', url=None, callback_data='1', web_app=None,
#                                                login_url=None, switch_inline_query=None,
#                                                switch_inline_query_current_chat=None,
#                                                switch_inline_query_chosen_chat=None, callback_game=None, pay=None),
#                           InlineKeyboardButton(text='Вариант 1 2', url=None, callback_data='2', web_app=None,
#                                                login_url=None, switch_inline_query=None,
#                                                switch_inline_query_current_chat=None,
#                                                switch_inline_query_chosen_chat=None, callback_game=None, pay=None)]]),
#                   forward_date=None, forward_from=None, forward_from_chat=None, forward_from_message_id=None,
#                   forward_sender_name=None, forward_signature=None, user_shared=None)
# inline_message_id = None
# data = '1'
# game_short_name = None
