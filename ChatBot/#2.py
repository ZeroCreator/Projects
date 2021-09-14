import random
import nltk


BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет!', 'Здарова', 'Хей-хей!!'],
            'responses': ['Хай', 'Добрый вечер!', 'Здравствуйте!']
        },
        'bye': {
            'examples': ['Пока', 'Увидимся!', 'Покеда'],
            'responses': ['До свидания', 'Прощайте', 'Сайонара!']
        },
        'new_intent': {
            'examples': ['some_example1', 'some_example2', 'some_example3'],
            'responses': ['some_response1', 'some_response2', 'some_response3']
        },
        'new_intent1': {
            'examples': ['some_example1', 'some_example2', 'some_example3'],
            'responses': ['some_response1', 'some_response2', 'some_response3']
        },
        'new_intent2': {
            'examples': ['some_example1', 'some_example2', 'some_example3'],
            'responses': ['some_response1', 'some_response2', 'some_response3']
        },
        'new_intent3': {
            'examples': ['some_example1', 'some_example2', 'some_example3'],
            'responses': ['some_response1', 'some_response2', 'some_response3']
        },
        'new_intent4': {
            'examples': ['some_example1', 'some_example2', 'some_example3'],
            'responses': ['some_response1', 'some_response2', 'some_response3']
        },
        'new_intent5': {
            'examples': ['some_example1', 'some_example2', 'some_example3'],
            'responses': ['some_response1', 'some_response2', 'some_response3']
        }
    }
}


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