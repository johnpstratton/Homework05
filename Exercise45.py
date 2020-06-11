# Write a program that reads a position from the user. 
# Use an elif statement to determine elif the column begins with a black square or a white square. 
# Then use modular arithmetic to report the color of the square in that row. 
# For example, elif the user enters a1 then your program should report that the square is black. 
# elif the user enters d5 then your program should report that the square is white. 
# Your program may assume that a valid position will always be entered. 
# It does not need to perform any error checking.

userInput = input("Please enter a letter (a-e) and number (1-8) in this format(a1): ") # asks user for input
char = userInput[:1] #assigns letter of userInput to string variable
number = int(userInput[1:2]) #assigns number of userInput to integer variable
black = "Black"
white = "White" 

#Checks to see if user is on black square based on black square starting value
if ("a" == char or "c" == char or "e" == char or "f" == char) and number %2 != 0: 
    print(black)
#Checks to see if user is on white square based on black square starting value
elif ("a" == char or "c" == char or "e" == char or "g" == char) and number %2 == 0:
    print(white)
#Checks to see if user is on a white square based on white square starting value
elif ("b" == char or "d" == char or "f" == char or "h" == char) and number %2 != 0:
    print(white)
#Checks to see if user is on a black square based on white square starting value
elif ("b" == char or "d" == char or "f" == char or "h" == char) and number %2 == 0:
    print(black)
else:
    print("Enter a new number combo")




