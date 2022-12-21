case = int(input())
number_lists = input().split()
number_lists = list(map(int, number_lists))


count1 = 0
count2 = 0
bak_lists = number_lists[0:]
for i in range(len(number_lists)) :
    j = i +1
    if i // 2 > len(number_lists) :
        break
    if number_lists[i] != number_lists[-jㅎㅎ] :
        number_lists.insert(len(number_lists) - i, number_lists[i] )
        count1 += 1
#  print(number_lists)

number_lists = bak_lists[0:]
for i in range(len(number_lists)) :
    j = i + 1
    if i // 2 > len(number_lists) :
        break
    if number_lists[i] != number_lists[-j] :
        number_lists.insert(i, number_lists[-j] )
        count2 +=1
#  print(number_lists)


print(min(count2,count1))

