order_based = input("Order-based: ")

# 입력 받은 숫자를 배열로 변환
int_array = [int(char) for char in order_based]
# print(int_array)
locus = []

length = len(int_array)
for i in range(0, length) :
    next = int_array.index(i)
    # print(next)
    if next+1 >= length :
        locus.append(int_array[0])
    else :
        locus.append(int_array[next+1])

locus_based = int(''.join(map(str, locus)))
print(locus_based)