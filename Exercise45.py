# Write a program that reads a position from the user. 
# Use an if statement to determine if the column begins with a black square or a white square. 
# Then use modular arithmetic to report the color of the square in that row. 
# For example, if the user enters a1 then your program should report that the square is black. 
# If the user enters d5 then your program should report that the square is white. 
# Your program may assume that a valid position will always be entered. 
# It does not need to perform any error checking.
# blackLetters = ["a", "c", "e", "g"]
# whiteLetters = ["b", "d", "f", "h"]

letters = ["a", "b", "c", "d", "e", "f", "g"]


black = "Black"
white = "White" 

userInput = input("Please enter a letter (a-e) and number (1-8) in this format(a1): ")
userInputChar = userInput[:1]
userInputChar = userInputChar.lower
number = int(userInput[1:2])

for x in letters:
    if x == letters[:1] and number %2 != 0:
        print(black)
        continue
    if x == letters[1:2] and number %2 != 0:
        print(white)
        continue
    if x == letters[2:3] and number %2 != 0:
        print(black)
        continue
    if x == letters[3:4] and number %2 != 0:
        print(white)
        continue
    if x == letters[4:5] and number %2 != 0:
        print(black)
        continue
    if x == letters[5:6] and number %2 != 0:
        print(white)
        continue
    if x == letters[6:7] and number %2 != 0:
        print(black)
        continue
    if x == letters[7:8] and number %2 != 0:
        print(white)
    
    



# if userInputChar == blackLetters[:1] and userInputInt %2 != 0:
#     print(black)
# elif userInputChar == blackLetters[1:2] and userInputInt %2 != 0:
#     print(black)
# elif userInputChar == blackLetters[2:3] and userInputInt %2 != 0:
#     print(black)
# elif userInputChar == blackLetters[3:4] and userInputInt %2 != 0:
#     print(black)
# else:
#     print(white)

