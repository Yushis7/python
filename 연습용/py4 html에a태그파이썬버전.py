a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#1번째 단어
a = "Hello, World!"
print(a[1])

#글자 하나하나씩
for x in "banana":
  print(x) 

#hello, world!스펠링 갯 수
a = "Hello, World!"
print(len(a))


#단어안에 free가 있는가 true
txt = "The best things in life are free!"
print("free" in txt)


#free가 안에 있다면 print 출력
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#expensive 단어가 없는가
txt = "The best things in life are free!"
print("expensive" not in txt)


#expensive 단어가 없다면 print 출력
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#0부터 5번쨰 글자까지
b = "Hello, World!"
print(b[:5])


#2번쨰부터 시작
b = "Hello, World!"
print(b[2:])


#뒤에서부터
b = "Hello, World!"
print(b[-5:-2])
