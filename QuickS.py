per=[]
n=int(input("Enter number of students:"))
for i in range(0,n):
    p=float(input("enter percentage:"))
    per.append(p)

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            (arr[i],arr[j])=(arr[j],arr[i]) 
    (arr[i+1],arr[high])=(arr[high],arr[i+1])   
    return (i+1)


def quick_sort(arr,low,high):
    if low<high:
        par=partition(arr,low,high)
        quick_sort(arr,low,par-1)           
        quick_sort(arr,par+1,high)
    return arr
    
l=len(per)
quick_sort(per,0,l-1)
print("sorted array:",per)

print("Top 5 Maximum Percentages Are : ",per[-1:-6:-1])



