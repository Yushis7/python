x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = 5
y = 10
print(x + y)


x = 5
y = "John"
print(x, y)
# print(x+y)로 하면 안돼


x = "이렇게 하자"
def myfunc():
  print("함수로만들기 " + x)
myfunc()


x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
#함수에서 x=fantastic으로 바꿔주면 x=awesome을 무시하게 되네


x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#함수에서 global x를 지정하면 함수를 벗어나도 fantastic으로 지정되네

