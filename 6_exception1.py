"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

questions_and_answers = {'Как дела': 'Хорошо!', 'Что делаешь?': 'Программирую'}

def ask_user(answers_dict):
  while True:
    try:
      question = input('задай вопрос')
      if question not in answers_dict:
        continue
      else:
        print(answers_dict[question])
    except KeyboardInterrupt:
      print('Пока!')
      break
 
    
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
    

