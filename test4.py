import random

population_size = 30
length = 10
population = []
fiteness = []
parents = []
parents_f = []
t = 1


for i in range(population_size):
    chromosome = ""
    for j in range(length):
        rand = random.randint(0,1)
        if rand > 0.5 :
            chromosome += "1"
        else :
            chromosome += "0"
    population.append(chromosome)

for i in range(population_size):
    count = 0
    for j in population[i] :
        if j == "1" :
            count += 1
    fiteness.append(count)
    print(i, ": ", population[i], "(f: ", fiteness[i], ")")


for i in range(4):
    numbers = list(range(30))
    random_numbers = random.sample(numbers, 4)
    parents.append([population[random_numbers[i]]])
    parents_f.append([fiteness[random_numbers[i]]])

print(parents[0], parents_f[0])

win_index1 = 0
win_index2 = 0

if parents_f[0] > parents_f[1] :
    win_index1 = 0
else :
    win_index1 = 1

if parents_f[2] > parents_f[3] :
    win_index2 = 2
else :
    win_index2 = 3


print(" - Tournament selection")
print("Parent 1 : ", parents[win_index1], "(f : ", parents_f[win_index1], ")")
print("Parent 2 : ", parents[win_index2], "(f : ", parents_f[win_index2], ")")

answer = ""

for i in range(length):
    random_uniform = random.random()
    if (random_uniform > 0.5) :
        answer += str(parents[win_index1])[i+2]
    else :
        answer += str(parents[win_index2])[i+2]

answer_count = 0
for i in range(length) :
    if answer[i] == "1" :
        answer_count += 1
print(answer_count)

print(" - Uniform crossover")
# print(str(answer))
print("offstring : %s  (f : %d) " %(answer, answer_count))
