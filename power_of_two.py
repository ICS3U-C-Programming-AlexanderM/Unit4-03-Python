#!/usr/bin/env python3
# Created By: Alex M
# Date: nov 5, 2023
# This program gives the sum of user input
def main():
    # get number from user
    user_number_as_str = input(" enter a positive number")
    # convert str to an int
    try:
        user_number = int(user_number_as_str)

    except ValueError:
        print (f"{user_number_as_str} is not a valid input ")
        print("")
    else:
        if user_number <0:
            print(f"{user_number}is not a positive number")
        else:
            count = 0
            answer = 0
            while True:
                count = count + 1
                answer = count **2
                print (f"{count} ** 2 = {answer}")
                
                if count >= user_number  :
                    break
            
        

    finally:
        print ("")

if __name__ == "__main__":
        main()