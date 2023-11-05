import random

generation = 50         # 세대 수
population_size = 30    # chromosome 수 
length = 20             # chromosome 길이
chromosomes = []
chromosome = ""




# 하나의 모집단에 chromosome 30개 생성 
for _ in range(population_size) :

    # 길이 20인 chromosome 생성
    for _ in range(length) :
        chromosome += str(random.randint(0,1))

    chromosomes.append(chromosome)
    chromosome = ""
    # count = chromosomes[i].count('1')
    # print("%d : %s (f: %d)  "%(i+1, chromosomes[i], count))


# Generation 50
for g in range(generation) :

    print("--------------- Generation %d -------------------" %(g))

    # population 출력
    for i in range(population_size) :
        count = chromosomes[i].count('1')
        print("%d : %s (f: %d)  "%(i+1, chromosomes[i], count))
    
    # ---------------- Tournament Selection ----------------
    # 0~29 사이의 모두 다른 수를 뽑아 chromosome 4개 선택
    random_numbers = random.sample(list(range(30)), 4)   
    a = chromosomes[random_numbers[0]]
    b = chromosomes[random_numbers[1]]
    c = chromosomes[random_numbers[2]]
    d = chromosomes[random_numbers[3]]

    # 토너먼트 준결승
    t = 0.5                 

    r = random.randint(0, 1)
    if t > r : winA = a
    else : winA = b

    r = random.randint(0, 1)
    if t > r : winB = c
    else : winB = d

    # print(winA, winB)


    # ---------------- one-point crossover ----------------
    point = random.randint(0, length-1)
    c1 = winA[0:point] + winB[point:]
    c2 = winB[0:point] + winA[point:]
    # print(point, c1, c2)

    # ---------------- bit-flip mutation ----------------
    rate = 0.05
    list_c1 = list(c1)
    list_c2 = list(c2)

    for i in range(length):
        if random.random() < rate :
            if list_c1[i] == '0' :
                list_c1[i] = '1'
            else : list_c1[i] = '0'
            if list_c2[i] == '0' :
                list_c2[i] = '1'
            else : list_c2[i] = '0'
    c1 = ''.join(list_c1)
    c2 = ''.join(list_c2)
    # print(c1, c2)


    # ---------------- GENITOR style Replacement ----------------
    min_c = 20
    min_i = 0
    for i in range(len(chromosomes)):
        if chromosomes[i].count('1') < min_c :
            min_c = chromosomes[i].count('1')
            min_i = i
    # print(min_c)
    del(chromosomes[min_i])

    min_c = 20
    min_i = 0
    for i in range(len(chromosomes)):
        if chromosomes[i].count('1') < min_c :
            min_c = chromosomes[i].count('1')
            min_i = i
    # print(min_c)
    del(chromosomes[min_i])

    # print(len(chromosomes))
    chromosomes.append(c1)
    chromosomes.append(c2)
    # print(len(chromosomes))


    # Best 
    best_c = 0
    best_i = 0

    for i in range(population_size) :
        if chromosomes[i].count('1') > best_c :
            best_c = chromosomes[i].count('1')
            best_i = i
    print("Best : %s (f : %d)" %(chromosomes[best_i], best_c))