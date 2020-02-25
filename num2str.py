# A simple python script that converts a number into a string
# @author Fabio Sabbion

def num2str(number):
    units = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    dozens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"]
    magnitudes = ["","thousand","million","billion"]
    
    groups = []
    while number > 0:
        # Splitting the number in groups of three digits
        groups.append(number % 1000)
        number = int(number / 1000)

    res = []
    magnitude = 0
    for group in groups:
        # converting to string each group of digits
        if group > 0:
            temp = []
            if(int(group%100) < 20):
                temp.append(units[int(group%100)])
                group = int(group/100)
            else:
                unit = units[int(group%10)] # calculating the unit digit
                group = int(group/10)
                dozen = dozens[int(group%10)] # calculating the dozen digit
                group = int(group/10)
                temp.append(dozen+" "+unit)
            if(group > 0): # if a digit is remained, then it will be the hundred digit
                temp.append(units[group] + " hundred")
            temp.reverse() # reversing the array 'cause i started from the end of the number
            temp.append(magnitudes[magnitude]) # adding the magnitude of the group of digits (thousand, million, etc.)
            res.append(" ".join(temp)) 
        magnitude = magnitude + 1
    res.reverse() # reversing the final result 'cause i started from the last group of digits
    return " ".join(res).title()

# here is the result
string = num2str(12345) # output: "Twelve Thousand Three Hundred Forty Five"
