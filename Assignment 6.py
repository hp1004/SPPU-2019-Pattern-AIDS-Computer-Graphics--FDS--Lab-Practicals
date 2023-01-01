""" Write a Python program to store first year percentage of students in array. Write function for
sorting array of floating point numbers in ascending order using quick sort and display top
five scores """

def partition(marks,low,high):
    pivot=marks[high]
    i=low-1
    for j in range(low,high):
        if marks[j]<=pivot:
            i=i+1
            (marks[i],marks[j])=(marks[j],marks[i])
    (marks[i+1], marks[high])=(marks[high],marks[i+1])
    return i+1
def quickSort(marks,low,high):
    if(low<high):
        pi = partition(marks,low,high)
        quickSort(marks, low, pi - 1)
        quickSort(marks, pi + 1, high)
marks=[]
n=int(input("Enter the total no of students: "))
for i in range(n):
    m=float(input("Enter the percentage of %i student: "%(i+1)))
    marks.append(m)
 
quickSort(marks,0,n-1)
print("Percentage of student sorted in ascending order: ")
print(marks)
print("Top 5 score")
print(marks[-5:n])