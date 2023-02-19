import os
import time
os.system("cls")
print("----------------------------------------------------------------------------------------")
print(" _____  _      ______            _      _____  ____  _____  _____ _______ _    _ __  __")
print("|  __ \| |    |  ____|     /\   | |    / ____|/ __ \|  __ \|_   _|__   __| |  | |  \/  |")
print("| |__) | |    | |__       /  \  | |   | |  __| |  | | |__) | | |    | |  | |__| | \  / |")
print("|  _  /| |    |  __|     / /\ \ | |   | | |_ | |  | |  _  /  | |    | |  |  __  | |\/| |")
print("| | \ \| |____| |____   / ____ \| |___| |__| | |__| | | \ \ _| |_   | |  | |  | | |  | |")
print("|_|  \_\______|______| /_/    \_\______\_____|\____/|_|  \_\_____|  |_|  |_|  |_|_|  |_| simple")
print()

sequence = input("Enter the sequence of characters to compress('help'): ")  #input string sequence
while sequence.lower() != "quit": 
    if(sequence.lower() == "help"):
        print("\t- clear : clears the screen")
        print("\t- about : about the developper")
        print("\t- quit : exit program")
        print("\tHow to use the program?")
        print("\t  Type a string of characters and let the algorithm work its magic to compress the given data.\n")
    elif(sequence.lower() == "clear"):
        os.system("cls")
        print("----------------------------------------------------------------------------------------")
        print(" _____  _      ______            _      _____  ____  _____  _____ _______ _    _ __  __")
        print("|  __ \| |    |  ____|     /\   | |    / ____|/ __ \|  __ \|_   _|__   __| |  | |  \/  |")
        print("| |__) | |    | |__       /  \  | |   | |  __| |  | | |__) | | |    | |  | |__| | \  / |")
        print("|  _  /| |    |  __|     / /\ \ | |   | | |_ | |  | |  _  /  | |    | |  |  __  | |\/| |")
        print("| | \ \| |____| |____   / ____ \| |___| |__| | |__| | | \ \ _| |_   | |  | |  | | |  | |")
        print("|_|  \_\______|______| /_/    \_\______\_____|\____/|_|  \_\_____|  |_|  |_|  |_|_|  |_| simple")
        print()

    elif(sequence.lower() == "about"):
        print("\nAbout:\n")
        print("\tHow to use the program?")
        print("\t  Type a string of characters and let the algorithm work its magic to compress it.\n\t\tNote, however that the algorithm is not 100% efficient.\n\t  We here at @mellowboy are doing our best to improve the algorithm.\n\t  This is just a side project that we have been working on.")
        print("\tSpecial Thanks to:")
        print("\t  @Ishfaq253951 who is the lead developper on this project.\n\t  He has been serving @mellowboy with passion and enthusiasm.\n\t  Thank You!")
        print("\tYou can find the source code on github.com at:")
        print("\t\thttps://github.com/Ishfaq253951/RLE-Algorithm")
        print("  Thank You again for using our software. We appreciate your support")
        print("\t\t©2023 mellowboy")
        print("-------------------------------------------------------------------------\n")
    else:
        length = len(sequence)
        repeated_count = 0
        compressed_value = ""
        compressed_data = []
        temp = sequence[0]
        for i in range(0, length):
            if temp == sequence[i]:
                repeated_count += 1
            else:
                compressed_value = str(repeated_count) + " " + temp
                compressed_data.append(compressed_value)
                temp = sequence[i]
                repeated_count = 1
        compressed_value = str(repeated_count) + " " + temp
        compressed_data.append(compressed_value)

        for i in range(0, len(compressed_data)):
            print(compressed_data[i], end="\t")

        print()
        original_size = length
        print("Size before compression: {0} bytes".format(original_size))
        new_size = len(compressed_data) * 2 #file size after compression
        print("Size after compression: {0} bytes".format(new_size))
        percentage_reduction = ((original_size - new_size)/original_size) * 100 #calculates how much the file was reduced in percentage
        rounded_percentage = round(percentage_reduction, 2)
        print("{0}% reduced".format(rounded_percentage))
        print()
    sequence = input("Enter the sequence of characters to compress('help'): ")  #input string sequence