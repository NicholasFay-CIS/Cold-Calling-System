"""
Group 2
2/3/2020
Majed Almazrouei, Justin Becker, Dylan Conway, Kyle Diodati, Nicholas Fay
"""
#imported lib
import sys
from tkinter import messagebox
#create the header string
#This is global as this code will only need to compile one time 
#rather than everytime the file i/o to output function is run
HEADER_STRING_TABS = "First name\tLast name\t95#\tEmail\n"
RANDOMIZATION_STRING_TABS = "RaNdOmIzEd\tRaNdOmIzEd\tRaNdOmIzEd\tRaNdOmIzEd\n"


class File_Input_Output:
    """
    This class is intended to be an object
    that handles all file I/O
    """
    def __init__(self):
        #the file inputs delimination of student attributes
        pass

    def obtain_file_obj(self, filepath):
        """
        self, file path (str) -> file obj, str
        This function is in charge of opening the file
        """
        #open the file to get the file obj
        #try to open the file
        while(True):
            try:
                #if you can open the file, 
                #open the filepath
                file = open(filepath, "r")
                break
            except:
                messagebox.showerror("ERROR", "Please provide a correct file path.\nCurrent path:\n" + filepath)
                file = None
                break
                #exit the program if there is no correct file to open
        return file
    
    def write_to_file(self, filepath, queue):
        """
        self, filepath (str) -> None
        This function takes a file and writes the necessary information 
        of a student to an output file so it can later be used
        as the next input file.
        ### I am using the database for now till things are more concrete ###
        """
        with open(filepath, "w") as file: #open the file
            #check if the file was tab deliminated
            file.write(HEADER_STRING_TABS) # write the file header
            file.write(RANDOMIZATION_STRING_TABS) 
                #iterate through whatever database or student set and write them to the file 
                #in the same order of the input file
            for student in queue:
                file.write("{}\t{}\t{}\t{}\n".format(student.first_name, student.last_name, student.id, student.email))
            return
        return
        