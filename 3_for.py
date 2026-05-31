"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
""" 
phone_list =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
a = 0
b = 0
def main(prod):
  sales_count = 0
  for a in prod:
    sales_count +=a
  sales_avg = round((sales_count / len(prod)) , 2)
  return sales_avg 

def summ(prod):
  sales_count = 0
  for a in prod:
    sales_count +=a
  return sales_count


for i in phone_list:
  result = main(i['items_sold'])
  summ_result = summ(i['items_sold'])
  b += summ_result
  a += result 
  print(f'Для товара {i['product']} средние продажи : {result} сумма проданных товаров: {summ_result}')
avg_cost = a / len(phone_list)
print(f'среднее кол-во продаж по всем товарам {avg_cost}') 
print(f'общее кол-во продаж по всем товарам {b}' )

  
