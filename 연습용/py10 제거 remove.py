thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


#[]지정 안해주면 오류남
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist) #this will cause an error because you have succsesfully deleted "thislist".


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
