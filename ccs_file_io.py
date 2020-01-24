#imported lib
import sys

#create the header string
#This is global as this code will only need to compile one time 
#rather than everytime the file i/o to output function is run
HEADER_STRING = "First name\tLast name\t95#\tEmail\n"


class File_Input_Output:
    """
    This class is intended to be an object
    that handles all file I/O
    """
    def __init__(self):
        pass

    def obtain_file_obj(self, filepath):
        """
        self, file path (str) -> file obj
        This function is in charge of opening the file
        """
        #open the file to get the file obj
        #try to open the file
        try:
            #if you can open the file, 
            #open the filepath and return the file object
            file = open(filepath, "r")
            return file
        except:
            print("ERROR: File not found. Please provide a correct file path")
            #exit the program if there is no correct file to open
            sys.exit()
        return
    
    def write_to_file(self, filepath, database):
        """
        self, filepath (str) -> None
        This function takes a file and writes the necessary information 
        of a student to an output file so it can later be used
        as the next input file.
        ### I am using the database for now till things are more concrete ###
        """
        with open(filepath, "w") as file: #open the file
            file.write(HEADER_STRING) # write the file header
            #iterate through whatever database or student set and write them to the file 
            #in the same order of the input file
            for student in database:
                file.write("{}\t{}\t{}\t{}\n".format(student.first_name, student.last_name, student.id, student.email))
        return
            
            
        