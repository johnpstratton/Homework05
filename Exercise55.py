# Name                Frequency range (Hz)   
#############         ##############################  
# Radio waves         Less than   3×109 
# Microwaves          3×10^9  to less than   3×10^12 
# Infrared light      3×10^12  to less than   4.3×10^14 
# Visible light       4.3×10^14  to less than   7.5×10^14 
# Ultraviolet light   7.5×10^14  to less than   3×10^17 
# X-Rays              3×10^17  to less than   3×10^19 
# Gamma rays          3×10^19  or more

# Write a program that reads the frequency of the radiation from the user and displays the appropriate name.

# store user response as string
response = (input("Please enter your frequency of radiation in this format (3.0*10**9): ")) 
# converts the first three numbers to a float from response string
num = float(response[:3])
#converts the second two numbers to float from response string
num1 = float(response[4:6])
#converts last number to int
num2 = int(response[8:10])
# peforms calculation of user input to compare to actual values of frequencies
total = num*num1**num2

rFreq = 3.0*10**9 #stores upper limit of Radio Waves
radiowave = "Your frequency: {0}, is in the Radio wave spectrum.".format(response)

mFreq = 3.0*10**12 #stores upper limit of Microwaves
microwave = "Your frequency: {0}, is in the Microwaves spectrum.".format(response)

iFreq = 4.3*(10**14) #stores upper limit of Infrared Light
infrared = "Your frequency: {0}, is in the Infrared light spectrum.".format(response)

vFreq = 7.5*(10**14) #stores upper limit of Visible Light
visible = "Your frequency: {0}, is in the Visible light spectrum.".format(response)

uFreq = 3.0*10**17 #stores upper limit of Ultraviolet Light
ultraviolet = "Your frequency: {0}, is in the Ultraviolet light spectrum.".format(response)

xfreq = 3.0*10**19 #stores upper limit of X-Rays
xray = "Your frequency: {0}, is in the X-Ray spectrum.".format(response)

gFreq = 3.0*10**19 #stores lower limit of Gamma Rays
gamma = "Your frequency: {0}, is in the Gamma Ray spectrum.".format(response)

if total < rFreq and total >= 0: # compare user value entered to values in frequency band and prints if true
    print(radiowave)
elif total >= rFreq and total < mFreq: # compare user value entered to values in frequency band and prints if true
    print(microwave)
elif total >= mFreq and total < iFreq: # compare user value entered to values in frequency band and prints if true
    print(infrared)
elif total >= iFreq and total < vFreq: # compare user value entered to values in frequency band and prints if true
    print(visible)
elif total >= vFreq and total < uFreq: # compare user value entered to values in frequency band and prints if true
    print(ultraviolet)
elif total >= uFreq and total < xfreq: # compare user value entered to values in frequency band and prints if true
    print(xray)
elif total >= xfreq: # compare user value entered to values in frequency band and prints if true
    print(gamma)
else:
    print("Unsure")
    
    