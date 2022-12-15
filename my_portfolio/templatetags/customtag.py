from django import template

register = template.Library()

def strs(value):
  print(value.section_2.values().first())
  print(dir(value.section_2))
  return str(100)

register.filter("str", strs)