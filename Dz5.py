import colorama
def name1():
    pass
class Name:
    pass
cl = colorama
name_1 = name1
nick = Name
print(cl.__name__)
print(colorama.__name__)

list1 = []
for method in dir(colorama):
    print(method)
for method in dir():
    print(method)
data='name'
print(getattr(data, 'reverse', None))
print(hasattr(data, 'index'))
