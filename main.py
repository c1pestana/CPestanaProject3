import random

def load_fortunes(which_file):
    user_file = open(which_file, 'r')
    all_lines = user_file.readlines()
    return all_lines

def display_fortune(all_lines):
    for fortunes in all_lines:
        response = ""
        no = ["no"]
        while response != "no":
            fortunes = random.choice(all_lines)
            all_lines.remove(fortunes)
            response = str(input("Do you want a fortune?"))
            if(response.lower() == "yes"):
                print(fortunes)

            response = response.lower()
        print("Thank you for playing!")
        quit()

def main():
    which_file = str(input("Which File Would You Like To Open?"))
    all_lines = load_fortunes(which_file)
    display_fortune(all_lines)

main()
