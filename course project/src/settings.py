TOKEN = '1372658763:AAEFXhA4bjsnZLXC9ewnuDUW3KvxPEexuyM' # Токен API к Telegram

DIALOGFLOW_PROJECT_ID = 'vnnlp-bot-kpwr' # PROJECT ID из DialogFlow
DIALOGFLOW_LANGUAGE_CODE = 'ru' # язык
SESSION_ID = 'VNNLP_bot'  # ID бота из телеграма

MIN_REVIEW_LENGTH = 25
IS_REVIEW_TRHESHOLD = 0.5
POSITIVE_THRESHOLD = 0.75
NEGATIVE_THRESHOLD = 0.25

responces_to_positives = [
    'Благодарим за отзыв! Нам очень приятно получать хорошие слова от наших пользователей.',
]

responces_to_negatives = [
    'Спасибо за отзыв! Свяжитесь с нами, постараемся вместе разобраться с этой проблемой.',
]

responces_to_neutrals = [
    'Спасибо за отзыв! Если есть время, напишите, пожалуйста, подробнее.',
]