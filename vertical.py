import sys


class MicroprogrammedControl(object):
    numRegisters = 0
    numALUFunctions = 0
    instruction = None
    numBuses = 0

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
            input("Select implementation type:")
        )
        while not is_valid(choice):
            print("Invalid implementation type selected.")
            choice = int(
                input("Select implementation type: (1) Horizontal or (2) Vertical")
            )

        # User provides specifications for the processor
        print("Enter number of registers: ")
        MicroprogrammedControl.numRegisters = input()
        print("Enter number of supported ALU functions: ")
        MicroprogrammedControl.numALUFunctions = input()
        input()
        # clear buffer
        print("Enter instruction to execute: ")
        MicroprogrammedControl.instruction = input()
        print("Enter number of buses (3, 2, or 1): ")
        MicroprogrammedControl.numBuses = input()
        # Show sequence of microoperations for the given instruction
        print("Sequence of microoperations: ")
        microoperations = MicroprogrammedControl.executeInstruction(
            MicroprogrammedControl.instruction
        )
        for operation in microoperations:
            print(operation)
        # Display final control word
        print("Final control word: ")
        controlWord = MicroprogrammedControl.generateControlWord(microoperations)
        print(controlWord)

    # Example method for executing instruction
    @staticmethod
    def executeInstruction(instruction):
        microoperations = [
            "Fetch instruction",
            "Decode instruction",
            "Execute instruction",
        ]
        return microoperations

    # Example method for generating control word
    @staticmethod
    def generateControlWord(microoperations):
        controlWord = ""
        for operation in microoperations:
            controlWord += "1"
        return controlWord


if __name__ == "__main__":
    MicroprogrammedControl.main(sys.argv)
