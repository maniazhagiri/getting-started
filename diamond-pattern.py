n=int(input("enter the number for diamond pattern :  "))
for i in range(n):
    j = n-i
    print(" "*j, " *"*i)
for i in range(n):
    l = n-i
    print(" "*i, " *"*l)
