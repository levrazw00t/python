def mydecor1(tag):
    def wrapper(func_todecor):
        def inner(*args, **kwargs):
            return "<{0}>\n{1}</{0}>\n".format(tag, func_todecor(*args, **kwargs))
        return inner
    return wrapper
 
def mydecor2(tag):
    def wrapper(func_todecor):
        def inner(*args, **kwargs):
            return "<{0}>{1}</{0}>\n".format(tag,func_todecor(*args, **kwargs))
        return inner
    return wrapper
 
#return <html>
@mydecor1("html")
def decor_html(*args):
    return"{}{}".format(*args)
 
#return <head>
@mydecor1("head")
def decor_head(*args):
    return "{}{}".format(*args)
 
#return <title>
@mydecor2("title")
def decor_title(text):
    return text
 
#return <style>
@mydecor2("style")
def concat_style(func_1, func_2):
    return "{0}{1}".format(func_1, func_2)
 
def decor_style(*args, **kwargs):
    return "{0}".format(*args)+"{color:" + "{1}".format(*args)+"}"
 
#return <body>
@mydecor1("body")
def decor_body(*args):
    return "{}{}".format(*args)
 
@mydecor2("h1")
def head1(*args):
    return "{}".format(*args)
 
@mydecor2("p")
def paragraph(*args):
    return "{}".format(*args)
 
greeting = input()
blue = input()
red = input()
title = input()
article = input()
 
 
hello = decor_title(greeting)
style_decor = concat_style(decor_style("h1",blue), decor_style("p",red))
head = decor_head(hello, style_decor)
head2 = head1(title)
parag = paragraph(article)
body = decor_body(head2, parag)
final = decor_html(head, body)
print(final)
