import sys


class MicroprogrammedControl(object):
    @staticmethod
    def main(args):
        # Allow user to select implementation type
        def print_menu():
            print("1. Horizontal")
            print("2. Vertical")

        print_menu()

        def is_valid(choice):
            if choice == 1 or choice == 2:
                return True
            else:
                return False

        choice = int(
            input("Select implementation type: (1) Horizontal or (2) Vertical")
        )
        while not is_valid(choice):
            print("Invalid implementation type selected.")
            choice = int(
                input("Select implementation type: (1) Horizontal or (2) Vertical")
            )
        choice = int(
            input("Select implementation type: (1) Horizontal or (2) Vertical")
        )
        # Verify user input
        if choice != 1 and choice != 2:
            print("Invalid implementation type selected.")
            return
        # Get processor specifications from user
        print("Enter number of registers: ")
        numRegisters = input()
        print("Enter number of supported ALU functions: ")
        numALUFunctions = input()
        input()
        # Clear input buffer
        print("Enter instruction to execute: ")
        instruction = input()
        # Optionally, allow user to select number of buses
        numBuses = 3
        print("Enter number of buses (3, 2, or 1): ")
        userNumBuses = input()
        if userNumBuses == 3 or userNumBuses == 2 or userNumBuses == 1:
            numBuses = userNumBuses
        # Show sequence of microoperations for the given instruction
        print("Microoperations for instruction " + instruction + ": ")
        if instruction == "ADD":
            print("Fetch instruction from memory")
            print("Decode instruction")
            print("Fetch operands from registers")
            print("Execute ADD operation using ALU")
            print("Store result in register")
        elif instruction == "SUB":
            print("Fetch instruction from memory")
            print("Decode instruction")
            print("Fetch operands from registers")
            print("Execute SUB operation using ALU")
            print("Store result in register")
        else:
            print("Invalid instruction.")
        # Display final control word
        print("Final control word: ")
        print("Num registers: " + str(numRegisters))
        print("Num ALU functions: " + str(numALUFunctions))
        print("Num buses: " + str(numBuses))


if __name__ == "__main__":
    MicroprogrammedControl.main(sys.argv)
