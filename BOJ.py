# str = 'a b c d e f g'
# # 파라미터 없이 split()
# res = str.split()
# print(res)

#1000번
# a,b=input().split()
# q=int(a)
# w=int(b)
# print(q+w)

# a,b=map(int,input().split())
# print(a+b)

#나눗셈만들기
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# ; A,B=input().split()
# ; print(int(A)*int(B))

# ; a, b = map(int, input().split())
# ; print(a + b)

# ; #사칙연산 만들기
# ; #두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

# ; a,b = input().split()
# ; a = int(a)
# ; b = int(b)
# ; print(a+b)
# ; print(a-b)
# ; print(a*b)
# ; print(int(a/b))
# ; #print(a//b)
# ; print(a%b)

# ; #차이점은 정수냐 자연수냐 차이인거 같은데 정수엔 int가 붙어야하고
# ; # 자연수는 그냥 print(a+b)해도 먹힐테니

# ; a, b = map(int , input().split())

# ; print(a+b) # 덧셈
# ; print(a-b) # 뺄셈
# ; print(a*b) # 곱셈
# ; print(a//b) # 몫
# ; print(a%b) # 나머지


# ; ; 준하 ??!
# ; print(input() + "??!")

#  id = input()
#  print(id + "??!")

# a = input()
# print(a+'??!')

#  불교서기
#a=int(input())
#print(a-543)

#Number = int(input())
#Result = Number - 543
#print(Result)

#y = int(input())
#print(y - 543)

# ; #나머지
# ; a, b, c = input().split()
# ; a = int(a)
# ; b = int(b)
# ; c = int(c)

# ; print((a+b)%c)
# ; print(((a%c)+(b%c))%c)
# ; print((a*b)%c)
# ; print(((a%c)*(b%c))%c)


# ; A,B,C = map(int,input().split())

# ; print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')

# ; ; sep이 붙으면 , 마다 \n을 해준다 예로 A,B,C sep='\n' 하면 A B C가 된다


# ; #곱셈 2588번

# ; A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
# ; B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# ; # 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
# ; AxB2 = A * int(B[2])
# ; AxB1 = A * int(B[1])
# ; AxB0 = A * int(B[0])
# ; AxB = A * int(B)

# ; print(AxB2, AxB1, AxB0, AxB, sep='\n')
# ; # sep='\n'로 줄바꿈

# ; 1. 문자열을 이용한 풀이(반복문X)
# ; <코드>

# ; A = int(input())
# ; B = input()

# ; print(A*int(B[2]))
# ; print(A*int(B[1]))
# ; print(A*int(B[0]))
# ; print(A*int(B))

# ; 2. 문자열을 이용한 풀이(반복문O)
# ; <코드>

# ; A = int(input())
# ; B = input()

# ; for i in range(3, 0, -1) :
# ;     print(A * int(B[i - 1]))

# ; print(A * int(B))

# ; 3. 산술 연산자를 이용한 풀이
# ; A = int(input())
# ; B = int(input())

# ; print(A * (B % 10))
# ; print(A * (B % 100 // 10))
# ; print(A * (B // 100))
#  print(A * B)

# a=int(input())
# b=input()

# print(a*int(b(2)))
# print(a*int(b(1)))
# print(a*int(b(0)))
# print(a*int(b))

# A = int(input())
# B = input()

# print(A*int(B[2]))
# print(A*int(B[1]))
# print(A*int(B[0]))
# print(A*int(B))

# # 꼬마정민  11382

# a,b,c=map(int,input().split())

# print(a+b+c)


# #고양이 10171
# print("\    /\\")  # \" 앞에 \를 붙여준다.
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")

# #개 10172
# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')  # \'앞에 \을 붙여준다.
# print('|"^"`    |')
# print("||_/=\\\__|")  # \\ 앞에 \을 하나 더 붙여준다.

A,B=map(int,input().split())
if A > B:
    print('>')  # if 조건식이 참일 때 문장
elif A < B:
    print('<')  # if조건식이 참이 아닌경우 elif 조건식이 참일 때 문장
else:
    print('==')  # 위의 모든 조건이 거짓일 때 문장

    
#     시험성적 9498 
#     # 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F
# score=int(input())

# if score>=90 :
#     print('A')
# elif score>=80 :
#     print('B')
# elif score>=70 :
#     print('C')
# elif score>=60 :
#     print('D')
# else :
#     print('F')  

#2884번 알람
H, M = map(int, input().split())

if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)	

#2525번 오븐시계
H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)

#2480 주사위 세개
a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c))
