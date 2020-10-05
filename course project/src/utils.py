import re
from nltk import word_tokenize
from pymorphy2 import MorphAnalyzer

from src.stop import basic_stop
from src.settings import TOKEN

morpher = MorphAnalyzer()

def normalize_word(word):
    return morpher.parse(word)[0].normal_form

def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'[*.,\n\t]', ' ', text)
    text_list = word_tokenize(str(text))
    text_list = [normalize_word(word) \
                 for word in text_list if word not in basic_stop]
    text = ' '.join(text_list)
#    text = text.replace(' не ', ' не не')
    return text