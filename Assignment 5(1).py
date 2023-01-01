def insertion(a): 
    n=len(a) 
    for i in range(0,n-1): 
        j=i+1 
        while(a[i]>a[j] and i>=0): 
            temp=a[j] 
            a[j]=a[i] 
            a[i]=temp 
            i=i-1 
            j=j-1 
    print(a)
    print("Top Five Scores are : ") 
    for i in range(n-1,n-6,-1): 
        print(a[i]) 
 
def shell(a): 
    n=len(a) 
    gap=int(n/2+0.5) 
    while(gap>=1): 
        i=0 
        j=gap 
        while(j<n): 
            if(a[j]<a[i]): 
                temp=a[i] 
                a[i]=a[j] 
                a[j]=temp 
            i=i+1 
            j=j+1 
        if(gap==1): 
            gap=0 
        gap=int(gap/2+0.5) 
    print(a)
    print("Top Five Scores are : ") 
    for i in range(n-1,n-6,-1): 
        print(a[i]) 
 
b=[] 
s=int(input("Enter the no. of Students : ")) 
for i in range(0,s): 
    m=int(input("Enter the marks of %dth student : "%(i+1))) 
    b.append(m) 
print("1. insertion   2. shell") 
ch=int(input("Enter choice : ")) 
if(ch==1): 
    insertion(b) 
if(ch==2): 
    shell(b)