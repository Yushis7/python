# from  itertools  import  count 

# def  generate_primes ( stop_at = None ) : 
#     primes  =  [] 
#     for  n  in  count ( start = 2 ): 
#         if  stop_at  is  not  None  and  n  >  stop_at : 
#             return  # StopIteration 예외 발생 
#         composite  =  False 
#         for  p  in  primes : 
#             if  not  n  %  p : 
#                 composite  =  True 
#                 break 
#             elif  p  **  2  >  n : 
#                 break 
#         if  not  composite : 
#             primes .append ( n ) yield n

# for  i  in  generate_primes ( 100 ):   # 0과 100 사이의 소수를 반복합니다. 
#     print ( i ) 

# for  i  in  generate_primes ():   # 모든 소수를 무한정 반복합니다. 
#     print ( i )


# print(''.join(map(lambda x, y: x + y, "Hello", "World")))

sum = lambda a, b: a+b
result = sum(3,4)
print(result)
# # 7

idx = 0
for element in ['AA', 'bb', 'Cc']:
    print(idx, element)
    idx += 1
# ...
# 0 AA
# 1 bb
# 2 Cc

for i in enumerate(['AA', 'bb', 'Cc']):
    print(i)
# ...
# (0, 'AA')
# (1, 'bb')
# (2, 'Cc')




names = ['blockdmask', 'gdgd', 'kimkim']
for idx, name in enumerate(names):         
    print(f'{idx}: {name}')
 
 

fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i,fruits)



numbers = [111, 333, 555, 777]
for i, num in enumerate(numbers):
    if i % 2 == 0:
        
        print(f'Index {i} is even, value: {num}')



