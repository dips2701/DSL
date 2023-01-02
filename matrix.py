def getmatrix(r,c,mat):
    print("Enter elements : ")
    for i in range(r):
        a=[]
        for j in range(c):
            ele=int(input())
            a.append(ele)
        mat.append(a)

def display(r,c,mat):
    for i in range(r):
        for j in range(c):
            print(mat[i][j],end="\t")
        print()

def add(r,c,mat1,mat2):
    res=[]
    for i in range(r):
        a=[]
        for j in range(c):
            a.append(mat1[i][j]+mat2[i][j])
        res.append(a)

    print("Addition of 2 matrices : ")
    display(r,c,res)

def sub(r,c,mat1,mat2):
    res=[]
    for i in range(r):
        a=[]
        for j in range(c):
            a.append(mat1[i][j]-mat2[i][j])
        res.append(a)

    print("Subtraction of 2 matrices : ")
    display(r,c,res)

def transpose(r,c,mat):
    res=[]
    for i in range(r):
        a=[]
        for j in range(c):
            a.append(mat[j][i])
        res.append(a)

    print("Transpose : ")
    display(r,c,res)

def mul(r1,c1,r2,c2,mat1,mat2):
    res=[]
    for i in range(r1):
        a=[]
        for j in range(c2):
            mul=0
            for k in range(c1):
                mul=mul+mat1[i][k]*mat2[k][j]
            a.append(mul)
        res.append(a)

    print("Multiplication : ")
    display(r1,c2,res)



print("For 1st matrix : ")
r1=int(input("Enter num of rows : "))
c1=int(input("Enter num of columns : "))

print("For 2nd matrix : ")
r2=int(input("Enter num of rows : "))
c2=int(input("Enter num of columns : "))

mat1=[]
mat2=[]

getmatrix(r1,c1,mat1)
getmatrix(r2,c2,mat2)

print("1st matrix : ")
display(r1,c1,mat1)
print("2nd matrix : ")
display(r2,c2,mat2)

if(r1==r2 and c1==c2):
    add(r1,c1,mat1,mat2)
else:
    print("addition is not possible")

if(r1==r2 and c1==c2):
    sub(r1,c1,mat1,mat2)
else:
    print("subtraction is not possible")

transpose(r1,c1,mat1)
transpose(r2,c2,mat2)

if(c1 == r2):
    mul(r1,c1,r2,c2,mat1,mat2)
else:
    print("Multiplication is not possible : ")
