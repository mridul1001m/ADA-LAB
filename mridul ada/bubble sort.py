n=int(input("enter the number"))
arr=list(map(int,input("enter sorted elements").split()))
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
print("sorted array:",arr)