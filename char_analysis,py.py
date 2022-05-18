#Name: Jose Melquiades Escobar

#Define main():
def main ():

    #Declare Local variables
    uppercase_letters = 0
    lowercase_letters = 0
    digits = 0
    spaces = 0
    problem = 0 

    #Open file text.txt for reading. Use 'text.txt' file attached under module.
    input_file = open ('text.txt', 'r')

    #User for loop to step through each character in the file.
    #Determine if the character is uppercase, lowercase, a digit, or space,
    #and keep a running total of each.
    for line in input_file:     #seperate the text file into seperate lines
        for char in line:       #look at each individual character of each line
            if char.isupper() == True:
                uppercase_letters += 1
            elif char.islower() == True:
                lowercase_letters += 1
            elif char.isdigit() == True:
                digits += 1
            elif char.isspace() == True:
                spaces += 1

    #Close the file.
    input_file.close()

    #Display the totals of uppercase, lowercase, digits, spaces.
    print ('Uppercase letters:', uppercase_letters)
    print ('Lowercase letters:', lowercase_letters)
    print ('Digits:', digits)
    print ('Spaces:', spaces)
    

main()
