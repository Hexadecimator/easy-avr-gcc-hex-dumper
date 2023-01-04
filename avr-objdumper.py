import sys, getopt
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

#path_to_avr_objdump = "C:\\Users\\logans\\AppData\\Local\\Arduino15\\packages\\arduino\\tools\\avr-gcc\\7.3.0-atmel3.6.1-arduino7\\bin\\avr-objdump.exe"
path_to_avr_objdump = ""

#path_to_avr_obj     = "C:\\Users\\logans\\AppData\\Local\\Temp\\arduino-sketch-215C43F6D2ABE25B1AF923ED4CB974B3\\helloAssemblyLanguageUno.ino.hex"
path_to_avr_obj     = ""

#avr_output_file     = "C:\\Users\\logans\\AppData\\Local\\Temp\\arduino-sketch-215C43F6D2ABE25B1AF923ED4CB974B3\\py_out.txt"
avr_output_file     = ""


def printHelp():
    print("\n ================================================ ")
    print(" ============== AVR-OBJDUMPER HELP ============== ")
    print(" ================================================ ")
    print("\n -h")
    print("     --> Prints help menu")
    print("\n -p <full local path to avr-objdump.exe>")
    print("     --> Sets the local path to avr-objdump.exe")

def main(argv):

    try:
        opts, args = getopt.getopt(argv,"hp:",[])
    except getopt.GetoptError:
        print("\nException!! GetoptError")
        printHelp()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            printHelp()
            sys.exit()
        elif opt in ("-p"):
            path_to_avr_objdump = arg
            print("Received path: " + path_to_avr_objdump)

    if(path_to_avr_objdump == ""):
        print("Bad argument for path to AVR-OBJDUMP. Exiting")
        sys.exit(2)

    print("\n[INFO] Setting AVR-OBJDUMP path to: " + path_to_avr_objdump)

    # print("*DEBUG PRINT* Arguments Received: " + str(len(argv)) + " arguments")
    # for arg in argv:
    #    print(str(arg))

    print("\nStep 1: Select a .hex file to dump")
    path_to_avr_obj = filedialog.askopenfilename(title="Choose hex file")

    print("\nStep 2: Select where to store the output file")
    avr_output_file = filedialog.asksaveasfilename(title="Choose where to save output")


    # JUST FOR TESTING
    path_to_avr_obj     = "C:\\Users\\logans\\AppData\\Local\\Temp\\arduino-sketch-215C43F6D2ABE25B1AF923ED4CB974B3\\helloAssemblyLanguageUno.ino.hex"
    avr_output_file     = "C:\\Users\\logans\\Desktop\\out.txt"


    obj_file_size = Path(path_to_avr_obj).stat()
    try:
        with open(avr_output_file, "w") as outfile: #redirect all output to outfile
            print("\nAVR OBJ parameters... \n    --> Size=" + str(obj_file_size.st_size) + "Bytes, UID=" + str(obj_file_size.st_uid), ", GID=" + str(obj_file_size.st_gid) + "\n")
            subprocess.run([path_to_avr_objdump, '-s', '-m', 'ihex', path_to_avr_obj], stdout=outfile)
    except FileNotFoundError:
        print("\n\n[ERROR] Issue with hex or output file location!")
        print(" --> Hex Location: " + path_to_avr_obj)
        print(" --> Output File Location: " + avr_output_file + "\n")
        sys.exit(2)

if (__name__ == '__main__'):
    main(sys.argv[1:]) # pass ALL command-line arguments to main (except arg 0 which just self-references the current .py script)