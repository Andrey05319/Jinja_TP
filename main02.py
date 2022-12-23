from jinja2 import Template

# EXAMPLE 3 ##################################################################
# ЭКРАНИРОВАНИЕ ДАННЫХ В СТРОКАХ ##################################################################


per = {"name": "Harry Potter", "age": 11}

tm = Template("I am {{ p.age }} and my name is {{ p.name }}.")
#tm = Template("I am {{ p['age'] }} and my name is {{ p['name'] }}.")  # Alternative version
msg = tm.render(p=per)

print(msg)