def qan_tic(): # (1)
    tic = "QAN.AX" # (2)
    print(f'inside the function{tic}') # (3)
    return tic # (4)
res=qan_tic()
print(res)
print('~'*20)
qan_tic()
tic='WES.AX'
print(f'global scope:{tic}')
#Exercise 1
l=[0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
def even_number(lis):
    new_list=[]
    for i in lis:
        if i % 2 ==0:
            new_list.append(i)
    return new_list
print(even_number(l))

#Exercise 2
lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
lst1 = [i**2 for i in lst if i ** 2 > 150]
print(f'the new list is {lst1}')

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
s_numbers = set(numbers)
lst2 = [j for j in s_numbers if j % 2 == 0]
print(f'the list with unique number is {lst2}')
