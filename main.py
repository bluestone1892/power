import random #랜덤함수 호출



a = random.randint(1 , 1000) #밑을 1에서 100사이로 설정
b = random.randint(2 , 1000) #지수를 2에서 100사이로 설정
print(a**b) #밑이 a이고 지수가 b인 거듭제곱 구하기
print(str(a)+"는 밑 입니다") #밑 알려주기
print(str(b) + "는 지수 입니다") #지수 알려주기