from jinja2 import Template

# EXAMPLE 1 ##################################################################

# name = "Sven"
# age = 47
#
# tm = Template("I am {{ a*2 }} and my name is {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)  # Add name and age parameter into the template
#
# print(msg)

# Avaliable constructions ##################################################################
# {%%} - спецификатор шаблона
# {{}} - выражение для вставки конструкций Python в шаблон
# {##} - блок комментариев
# ### - строковый комментарий

# EXAMPLE 2 ##################################################################
# USING THE CLASS ##################################################################

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# per = Person("Sven", 56)
#
# tm = Template("I am {{ p.age }} and my name is {{ p.name }}.")
# msg = tm.render(p=per)
#
# print(msg)

# EXAMPLE 3 ##################################################################
# USING THE DICTIONARY ##################################################################


per = {"name": "Harry Potter", "age": 11}

tm = Template("I am {{ p.age }} and my name is {{ p.name }}.")
#tm = Template("I am {{ p['age'] }} and my name is {{ p['name'] }}.")  # Alternative version
msg = tm.render(p=per)

print(msg)
