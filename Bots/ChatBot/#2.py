import random
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# BOT_CONFIG = {
#     'intents': {
#         'hello': {
#             'examples': ['Привет!', 'Здарова', 'Хей-хей!!'],
#             'responses': ['Хай', 'Добрый вечер!', 'Здравствуйте!']
#         },
#         'bye': {
#             'examples': ['Пока', 'Увидимся!', 'Покеда'],
#             'responses': ['До свидания', 'Прощайте', 'Сайонара!']
#         }
#     }
# }

import codecs

with codecs.open('BOT_CONFIG.json', 'r', 'utf-8') as f:
  BOT_CONFIG = json.load(f)

"""
with open('BOT_CONFIG.json', 'r') as f:
  BOT_CONFIG = json.load(f)
"""

def clean(text):
  text = text.lower()
  cleaned_text = ''
  for ch in text:
    if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
      cleaned_text = cleaned_text + ch
  return cleaned_text


def get_intent(text):
  for intent in BOT_CONFIG['intents'].keys():
    for example in BOT_CONFIG['intents'][intent]['examples']:
      w1 = clean(example)
      w2 = clean(text)
      if nltk.edit_distance(w1, w2) / max(len(w1), len(w2)) < 0.4:
        return intent
  return 'интент не найден'


def bot(question):
  intent = get_intent(question)
  if intent != 'интент не найден':
    print(random.choice(BOT_CONFIG['intents'][intent]['responses']))
  else:
    print(intent)


question = ''
while question != 'стоп':
  question = input()
  bot(question)


X = []
y = []

for intent in BOT_CONFIG['intents'].keys():
    try:
        for example in BOT_CONFIG['intents'][intent]['examples']:
            X.append(example)
            y.append(intent)
    except:
        pass

len(X), len(y), len(set(y))


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
len(X_train), len(X_test)


vectorizer = CountVectorizer(preprocessor=clean, analyzer='char', ngram_range=(2,3))
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

len(vectorizer.get_feature_names())


log_reg = LogisticRegression(C=0.2)
log_reg.fit(X_train_vect, y_train)
log_reg.score(X_train_vect, y_train)


log_reg.score(X_test_vect, y_test)


def get_intent_by_model(text):
    return log_reg.predict(vectorizer.transform([text]))[0]


def bot(question):
  intent = get_intent_by_model(question)
  return random.choice(BOT_CONFIG['intents'][intent]['responses'])


question = ''
while True:
  question = input()
  if question != 'стоп':
      answer = bot(question)
      print(answer)
  else:
      break


bot(question)