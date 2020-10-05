import os
import pickle
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import dialogflow

from src.stop import *
from src.utils import *
from src.classifier import *
from src.settings import *


with open('message_analyzer.pickle', 'rb') as f:
     message_analyzer = pickle.load(f)

with open('sentiment_analyzer.pickle', 'rb') as f:
     sentiment_analyzer = pickle.load(f)

updater = Updater(TOKEN, use_context=False) # Токен API к Telegram
dispatcher = updater.dispatcher

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vnnlp-bot-kpwr-cace54ccce30.json' # скачанный JSON


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет!')


def textMessage(bot, update):

    message = update.message.text
    prediction = message_analyzer.predict([message])
    prediction = prediction[0]
    is_review = prediction >= IS_REVIEW_TRHESHOLD

    if is_review and len(message) >= MIN_REVIEW_LENGTH:

        prediction = sentiment_analyzer.predict([message])
        prediction = prediction[0]

        if prediction >= POSITIVE_THRESHOLD:
            text = random.choice(responces_to_positives)
        elif prediction <= NEGATIVE_THRESHOLD:
            text = random.choice(responces_to_negatives)
        else:
            text = random.choice(responces_to_neutrals)

        text = f'{text} \nС уважением, команда бота.'

    else:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        text_input = dialogflow.types.TextInput(text=update.message.text,
                                                language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
        except InvalidArgument:
             raise

        text = response.query_result.fulfillment_text
        if not text:
            text = 'Что?'

    bot.send_message(chat_id=update.message.chat_id,
                     text=text)


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
