from django import template

register = template.Library()


def my_template(value, arg):
    if arg == "change":
        value = "Rahim"
        return value
    if arg == "title":
        return value.title()


register.filter("change_name", my_template)
