"""Write a Python program to store first year percentage of students in array. Write function for
sorting array of floating point numbers in ascending order using
a Selection Sort
b Bubble sort and display top five scores """

def selectionSort(array, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[i], array[min_index]) = (array[min_index], array[i])
def bubblesort(marks):
    for i in range(len(marks)-1, 0, -1):
        for j in range(i):
            if marks[j]>marks[j+1]:
                #SWAPPING 
                temp = marks[j]
                marks[j]=marks[j+1]
                marks[j+1]=temp
print("\t")
#print("----------- B U B B L E  S O R T ------------------")
marks = []
n = int(input("Enter the total no of students: "))
for i in range(n):
    m = float(input("Enter the percentage of %i student: " % (i+1)))
    marks.append(m)

print("1. selection sort   2. bubble sort")
ch = int(input("Enter choice : "))
if (ch == 1):
    selectionSort(marks, n)
    print("Percentage of student sorted in ascending order: ")
    print(marks)
    print("Top 5 score")
    print(marks[-5:n])

if (ch == 2):
    bubblesort(marks)
    print("Percentage of student sorted in ascending order: ")
    print(marks)
    print("Top 5 score")
    print(marks[-5:n])
