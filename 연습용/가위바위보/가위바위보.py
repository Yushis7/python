import random

choices = ["가위", "바위", "보"]
computer = random.choice(choices)

user = input("가위, 바위, 보 중 하나를 선택하세요: ")

if user == computer:
    print(f"비겼습니다! (컴퓨터: {computer})")
elif (user == "가위" and computer == "보") or \
     (user == "바위" and computer == "가위") or \
     (user == "보" and computer == "바위"):
    print(f"이겼습니다! (컴퓨터: {computer})")
else:
    print(f"졌습니다! (컴퓨터: {computer})")
