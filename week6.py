head=input()
color_Title1=input()
color_text=input()
Title1=input()
text=input()

def makehtml(fn):                                            
  def inner(*args,**kwargs):
    print ("<html>")
    print (fn(*args,**kwargs))
    print("</html>")
  return inner
def makehead(fn):                                            
  def inner(*args,**kwargs):
    print ("<head>")
    print (fn(*args,**kwargs))
    print("</head>")
  return inner  
def maketitle(fn):
  def inner(*args,**kwargs):
    print ("<title>" + fn(*args,**kwargs) + "</title>")
  return inner  
def makestyle(fn):
  def inner(*args,**kwargs):
    print ("<style>" + fn(*args,**kwargs) + "</style>")
  return inner  
def makebody(fn):
  def inner(*args,**kwargs):
    print ("<body>")
    print (fn(*args,**kwargs))
    print ("</body>")
  return inner
def makeh1(fn):
  def inner(*args,**kwargs):
    print ("<h1>" + fn(*args,**kwargs) + "</h1>")
  return inner
def makep(fn):
  def inner(*args,**kwargs):
    print ("<p>" + fn(*args,**kwargs) + "</p>")
  return inner

@makehtml
@makehead
@maketitle
@makestyle
def h0(text='hello'):
  return text



  




>>> def p(func):
...     def inner(text):
...         print('<p>')
...         func(text)
...         print('</p>')
...     return inner
...
>>> def li(func):
...     def inner(text):
...         print('<li>')
...         func(text)
...     return inner
...
>>> @p
... @li
... def hello(text):
...     print ('Hello %s'%text)
...
>>> hello('Python')
<p>
<li>
Hello Python
</p>




  



def makehtml(fn):                                            #применение декораторов, возвращающих значение
  def inner(*args,**kwargs):
    return "<html>" + fn(*args,**kwargs) + "</html>"
  return inner
def makebody(fn):
  def inner(*args,**kwargs):
    return "<body>" + fn(*args,**kwargs) + "</body>"
  return inner
def maketitle(fn):
  def inner(*args,**kwargs):
    return "<title>" + fn(*args,**kwargs) + "</title>"
  return inner  
@makehtml
def h0(text='hello'):
  @maketitle
  def h1(text='title'):
    return text
  @makebody
  def h2(text='body'):
    return text
  text=str(h1())+str(h2())
  return text
print (h0())  
<html><title>title</title><body>body</body></html>
