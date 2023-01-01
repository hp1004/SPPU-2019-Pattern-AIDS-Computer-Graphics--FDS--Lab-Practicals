""" Write a Python program to store second year percentage of students in array. Write function
for sorting array of floating point numbers in ascending order using
a) Insertion sort
b) Shell Sort and display top five scores """

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j] :
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
print("\t")
print("----------- I N S E R T I O N   S O R T ---------------")
array=[]
n=int(input("Enter the total no of students: "))
for i in range(n):
    m=float(input("Enter the percentage of %i student: "%(i+1)))
    array.append(m)
insertionSort(array)
print("Percentage of student sorted in ascending order: ")
print(array)
print("Top 5 score")
print(array[-5:n])

def shellSort(array):
	n = len(array)
	gap = n/2
	while gap > 0:

		for i in range(gap,n):
			temp  = array[i]
			j = i
			while j >= gap and array[j-gap] >temp:
				array[j] = array[j-gap]
				j -= gap
			array[j] = temp 
		gap /= 2
print("----------- S H E E L  S O R T ---------------")
array=[]
N=int(input("Enter the total no of students: "))
for i in range(N):
    m=float(input("Enter the percentage of %i student: "%(i+1)))
    array.append(m)
shellSort(array)
for i in range(N):
    print("Percentage of student sorted in ascending order: ",array[i]),


