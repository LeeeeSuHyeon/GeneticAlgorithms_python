import random

parent1 = input("10자 숫자 입력: ")
parent2 = input("10자 숫자 입력: ")
print("parent1: ", parent1)
print("parent2: ", parent2)


cutPoint = random.randint(0,9) # 0에서 9 사이 랜덤 숫자
print("cut point : before index ", cutPoint)

subString = parent1[0:cutPoint]
subString1 = parent1[cutPoint:9]

subString2 = parent2[0:cutPoint]
subString3 = parent2[cutPoint:9]

offString1 = subString + subString3
offString2 = subString2 + subString1

print("offString1 : ", offString1)
print("offString2 : ", offString2)


