# ФИЛЬТРЫ И МАКРОСЫ: macro, call ##################################################################

from jinja2 import Template

# EXAMPLE 1 ##################################################################
# ЭКРАНИРОВАНИЕ ДАННЫХ В СТРОКАХ ##################################################################



# Шаблон:
# {% if<условие>%}
#     <фрагмент истинности условия>
# {% endif %}

cities = [
    {'id': 1, 'city': 'Jots'},
    {'id': 4, 'city': 'Kaluga'},
    {'id': 56, 'city': 'Orel'},
    {'id': 81, 'city': 'Astana'},
    {'id': 3, 'city': 'Bern'},
]
# Символ - убирает перенос
link = '''<select name = "cities">
{% for c in cities -%} 
{% if c.id > 6 -%} 
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == "Jots" -%}     
    <option {{c['id']}}</option>    
{%else -%}    
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
