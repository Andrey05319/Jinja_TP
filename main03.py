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
# MAX, MIN, RANDOM, REPLACE ##################################################################

# cars = [
#     {'model': "Huyndai", 'price': 10001},
#     {'model': "Audi", 'price': 20002},
#     {'model': "Opel", 'price': 30003},
#     {'model': "Kia", 'price': 40004},
# ]
#
# # tpl = "Максимальная цена автомобиля {{ cs | max(attribute='price')}}" # выдаст элемент словаря
# # tpl = "Максимальная цена автомобиля {{ (cs | max(attribute='price')).price }}" # выдаст только стоимость
# # tpl = "Минимальная цена автомобиля {{ (cs | min(attribute='price')).price }}" # выдаст только стоимость
# # tpl = "Случайный автомобиль {{ cs | random }}"
# tpl = "Минимальная цена автомобиля {{ cs | replace('i', 'G') }}"
#
#
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# EXAMPLE 4 ##################################################################
# FILTER ##################################################################

# # Шаблон:
# # {{% filter<название фильтра>%}}
# # <фрагмент для применения фильтра>
# # {% endfilter %}
#
#
# persons = [
#     {"name": "Harry", "old": 11, "weight": 25},
#     {"name": "Hermiona", "old": 12, "weight": 23},
#     {"name": "Ron", "old": 10, "weight": 27},
# ]
#
# tpl = '''
# {%- for u in users-%}
# {% filter upper %}{{u.name}}{% endfilter %}
# {% endfor -%}
# '''
#
# tm = Template(tpl)
# msg = tm.render(users = persons)
#
# print(msg)

# EXAMPLE 5 ##################################################################
# Макроопределения ##################################################################

html = '''
{% macro input(name, value = '', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''

tm = Template(html)
msg = tm.render()

print(msg)

