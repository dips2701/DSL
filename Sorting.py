marks=[]
print ("Enter total no. of students")
n=int(input())
print("Enter marks of students")
for i in range(n):
    m=int(input())
    marks.append(m)
print(marks)
   
def Selection_sort(marks):
    for i in range(n):
       min_ind = i
       for j in range(i+1,n):
           if (marks[min_ind] > marks[j]):
                min_ind = j  
               
       marks[min_ind],marks[i]=marks[i],marks[min_ind]
   
    print("\nSelection Sort is : ")
    print(marks)
   
def Bubble_sort(marks):
    n=len(marks)
    for i in range(n):
       for j in range(0,n-i-1) :
          if (marks[j] > marks[j+1]) :
              marks[j],marks[j+1]=marks[j+1],marks[j]
   
    print("Bubble sort is : ")  
    print(marks)
   
flag = 1
while (flag==1):
       print("\nSelect an operation : ")
       print("1 = Selection sort")
       print("2 = Bubble sort")
       print("3 = Exit " )
       print("Enter your choice : ")
       ch = int(input())
       
       if (ch == 1):
           Selection_sort(marks)
           
       elif (ch == 2):
           Bubble_sort(marks)
           
       elif (ch == 3):
           flag = 0
           
       else :
          print("Invalid choice")