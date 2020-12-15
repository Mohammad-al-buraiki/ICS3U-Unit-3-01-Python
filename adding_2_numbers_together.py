#!/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program asks the user for 2 numbers and then adds the 2 number together


def main():
    # this function asks the user for 2 numbers and then adds the 2 number together

    # input
    First = input("Enter first number:")
    Second = input("Enter second number:")
    
    # process
    result = ((int(First))+(int(Second)))
    
    # output
    print("The result of the addition process of {0} and {1} is: {0} + {1} = {2}".
          format(First, Second, result))
    
if __name__ == "__main__":
    main()
