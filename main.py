##CAITLIN PESTANA
##ALL DONE, FINALLY
##WHEN PROMPTED, THE FORTUNES ARE IN FILE "FORTUNES.TXT"

import random


#define load_fortunes function
def load_fortunes(which_file):
    #open the file to read
    user_file = open(which_file, 'r')
    #read the lines
    all_lines = user_file.readlines()
    #return the function
    return all_lines

#define display_fortunes function with parameter
def display_fortune(all_lines):
    #create for loop 
    for fortunes in all_lines:
        response = ""
        no = ["no"]
        #create while loop to quit if they say no
        while response != "no":
            fortunes = random.choice(all_lines)
            all_lines.remove(fortunes)
            response = str(input("Do you want a fortune?"))
            #create if statement to print the random fortune if response is lowercase or uppercase yes
            if(response.lower() == "yes"):
                print(fortunes)

            response = response.lower()
        print("Thank you for playing!")
        quit()

        
#define main function 

def main():
    #call which_file and ask the user which file to open
    which_file = str(input("Which File Would You Like To Open?"))
    #call all__lines function passing which_file as a parameter
    all_lines = load_fortunes(which_file)
    #call display_fortunes function using the returned value from all_lines as a parameter
    display_fortune(all_lines)

main()
