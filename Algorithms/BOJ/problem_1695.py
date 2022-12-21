case = int(input())
number_lists = input().split()
number_lists = list(map(int, number_lists))
n = len(number_lists)
half_num2 =half_num1 = n // 2
if n % 2 :
    half_num2 += 1

list_1 = number_lists[0:half_num1]
list_2 = number_lists[half_num2 :]
count = 0
for i in range(len(number_lists)) :
    if i // 2 > len(number_lists) :
        break
    if number_lists[i] != number_lists[-i] :
        number_lists.insert(-i, number_lists[i] )
        count +=1


print(count)

