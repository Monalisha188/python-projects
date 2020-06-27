#to print all positive numbers in a range

l=[]
a = int(input())
for i in range(a):
  i = int(input())
  if i not in l:
    l.append(i)
print("list1 =", l)
my_list = l
for j in my_list:
  if j>=0:
    print(j, end=" ")
