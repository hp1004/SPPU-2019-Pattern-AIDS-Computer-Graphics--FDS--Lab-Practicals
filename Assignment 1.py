'''Write a Python program to store marks scored in subject “Fundamental of Data Structure” by
N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency '''

marklist=[]
n=int(input("Enter Number of Students: "))

#Taking Marks of an Students...
print("\t")
print("*NOTE:  Take 0 for absent students")
print("\t\t")
for i in range(n):
    marks=int(input(f"Enter Marks of {i+1} students: "))
    marklist.append(marks)
print("-------------------------------------")
print("Marklist of ",n, "Student: ")
print(marklist)
print("-------------------------------------")


# a) The average score of class
average = sum(marklist)/len(marklist)
print("a) The average score of class: ", round(average,2))
print("-------------------------------------")


#b) Highest score and lowest score of class
min_value=marklist[0]
max_value=marklist[0]

for marks in marklist:
    if marks<min_value:
        min_value=marks
    if max_value<marks:
        max_value=marks

print("b)Highets Score of the class: ",max_value)
print("b)Lowest Score of the class: ",min_value)

print("-------------------------------------")

#c) Count of students who were absent for the test
absent_student=0
for marks in marklist:
    if marks== 0:
        absent_student += 1

print("C) Number of absent students for test: ",absent_student)

print("-------------------------------------")

#d) Display mark with highest frequency
freq={}
for marks in marklist:
    if marks != None:
        if freq.get(marks)==None:
            freq[marks]=1
        else:
            freq[marks] +=1
print("d) Marks with highest frequency || ", freq)
        