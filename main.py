from jinja2 import Template

name = "Sven"

tm =  Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)