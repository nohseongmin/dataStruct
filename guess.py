import random

answer = random.randrange(1, 1000)
win = False

for guesses in range(10):
    guess = int(input(f"{10-guesses}번 남음, 수 입력 : "))
    if answer == guess:
        print("정답")
        win = True
        break
    elif answer > guess:
        print("입력한 수는 정답 보다 작음\n")
    else:
        print("입력한 수는 정답 보다 큼\n")
    guesses = guesses + 1

if win==True:
    print("당신이 이겼습니다")
if win==False:
    print("패배")
