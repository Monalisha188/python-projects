#find the fibonacci series
n = int(input("enter a number:"))
a = 0
b = 1
for i in range(n):
  print(a, end=" ")
  temp=a
  a=b
  b=temp+b


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

