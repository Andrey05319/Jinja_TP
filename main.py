from jinja2 import Template

name = "Sven"
age = 47

tm =  Template("I am {{ a }} and my name is {{ n }}")
msg = tm.render(n=name, a=age)
# Add name and age parameter into the template

print(msg)

##################################################################

# # Avaliable constructions
# {%%} - спецификатор шаблона
# {{}} - выражение для вставки конструкций Python в шаблон
# {##} - блок комментариев
# ### - строковый комментарий
