work_hour=input('How long have you worked?')
work_hour=int(work_hour)
if work_hour <=35:
    pay=51.45*work_hour
else:
    pay=88.9*(work_hour-35)+35*51.45
print('Your weekly pay is', pay)

numbers=[-2,3,9,1,5,7,2,11,0,3,12,3,15,10]
temp_largest = numbers[0]
for number in numbers:
 if number > temp_largest:
    temp_largest = number
print(f'The largest value is {temp_largest}')
a=0
while a<=len(numbers):
    b=1+a
    if b==len(numbers):
        break
    if numbers[b]>=numbers[a]:
        max_=numbers[b]
    else:
        max_=numbers[a]
    a+=1
print(f'The largest number is {max_}')


for i in range(1, 4):
 for j in range(1, 4):
  if i <= j:
    print(i, j)