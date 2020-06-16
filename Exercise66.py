
####Exercise 51 included a table that shows the conversion from letter grades 
####to grade points at a particular academic institution. 

# In this exercise you will compute the grade point average of an arbitrary number of letter grades entered
# by the user. The user will enter a blank line to indicate that all of the grades have been provided. 
# For example, if the user enters A, followed by C+, followed by B, followed by a blank line then your program
# should report a grade point average of 3.1.


# Letter    Grade points
########    ############
# A+          4.0
# A           4.0
# A  −        3.7
# B+          3.3
# B           3.0
# B  −        2.7
# C+          2.3
# C           2.0
# C  −        1.7
# D+          1.3
# D           1.0
# F           0

gradeList = [] ### Empty list used to store values as user enters grade
gradeDict = { ### Used to store key:value pairs for logical comparison
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0
}    

##### Create a function to ask user to enter grades 
def askGrade():
    response = (input("Please enter a grade between A+ to F: ")).upper()
    for grade in gradeDict:
        if response == grade:
            gradeList.append(gradeDict[grade]) ## Append the value of each grade to gradeList
            return True ### Returns boolean value for comparison in the while loop
        elif response == "":
            return False ### Returns boolean value for comparison in the while loop
        
        

total = 0 ## Will be used to total all values in gradeList
totalGPA = 0 ## Will be used to store value of the individual's GPA
while askGrade() == True: ## Inititate while Loop to call askGrade Function
    askGrade()

for x in gradeList: ##Iterates through the values of gradeList and adds them together
    total += x
totalGPA = total / (len(gradeList)) ## divide the total of all the values in gradelist by number of values
print(totalGPA)                         ## to get and print the GPA
