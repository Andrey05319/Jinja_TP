# ФИЛЬТРЫ И МАКРОСЫ: macro, call ##################################################################

from jinja2 import Template

# EXAMPLE 1 ##################################################################
# SUM ##################################################################

# # Шаблон:
# # sum - вычисление суммы поля в коллекции
# # sum(iterable, attribute=None, start=0)
#
# cars = [
#     {'model': "Huyndai", 'price': 10001},
#     {'model': "Aydi", 'price': 20002},
#     {'model': "Opel", 'price': 30003},
#     {'model': "Kia", 'price': 40004},
# ]
#
# tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price')}}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# EXAMPLE 2 ##################################################################
# SUM ##################################################################

# # Шаблон:
# # sum - вычисление суммы поля в коллекции
# # sum(iterable, attribute=None, start=0)
#
# digs = [1,2,3,4,5]
#
# tpl = "Суммарная цена автомобилей {{ cs | sum }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=digs)
#
# print(msg)

# EXAMPLE 3 ##################################################################
# MAX, MIN ##################################################################

# Шаблон:
# sum - вычисление суммы поля в коллекции
# sum(iterable, attribute=None, start=0)

cars = [
    {'model': "Huyndai", 'price': 10001},
    {'model': "Aydi", 'price': 20002},
    {'model': "Opel", 'price': 30003},
    {'model': "Kia", 'price': 40004},
]

# tpl = "Максимальная цена автомобиля {{ cs | max(attribute='price')}}" # выдаст элемент словаря
# tpl = "Максимальная цена автомобиля {{ (cs | max(attribute='price')).price }}" # выдаст только стоимость
tpl = "Минимальная цена автомобиля {{ (cs | min(attribute='price')).price }}" # выдаст только стоимость


tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)






