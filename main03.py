# ФИЛЬТРЫ И МАКРОСЫ: macro, call ##################################################################

from jinja2 import Template

# EXAMPLE 1 ##################################################################
# SUM ##################################################################

cars = [
    {'model': "Huyndai", 'price': 10001},
    {'model': "Aydi", 'price': 20002},
    {'model': "Opel", 'price': 30003},
    {'model': "Kia", 'price': 40004},
]

tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price')}}"

tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)
