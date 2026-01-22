a=int(input("enter the number"))
array=list(map(int,input("enter elements").split()))
max_val=array[0]
for i in range(1,a):
    if array[i]>max_val:
        max_val=array[i]
print("maximum element",max_val)
