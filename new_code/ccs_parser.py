#imported lib
from collections import namedtuple

class Student:
    """
    This class is intended to initialize a student object with the attributes
    that have been parsed
    """
    def __init__(self, first=None, last=None, ID=None, email=None):
        """
        self, first (str), last (str), ID (str), email (str) -> None
        Initialize a student with a first and last name,
        a 95 number and their student email.
        """
        self.first_name = first
        self.last_name = last
        self.id = ID
        self.email = email
    
class Class_Roster:
    """
    This class is intended to act as a database for 
    the students that are available for queue access.
    """
    def __init__(self):
        """
        self -> None
        Init the Class_Roster class to have a empty set attribute.
        This is optimal when dynamically creating the database.
        A new class can be instantiated each loop of the main program
        """
        #initialize the class "roster" to a set
        #created the set is much quicker in compile/run time.
        self.class_roster = set()

class Parser:
    """
    This is the parser class. Its main role is to parse input
    files to file in the database.
    """

    def __init__(self):
        pass

    def handle_poor_input_file(self, Student, line_list):
        """
        student obj, list -> student obj
        This function is in charge of handling poor input lines.
        This allows the program to proceed parsing and filling the database as best as possible.
        Some attributes may not be correct but it eliminates index errors in the parser that 
        would cause a crash in the program.
        """
        #set nine_five_number and email to be none 
        nine_five_number = None
        email = None
        used = list()
        #loop through the list and check if there is a 95 number or an email
        for item in line_list:
            #if there is a 95 number set that to the students id attribute
            if("95" in item):
                nine_five_number = item
                Student.id = item
                used.append(item)
            #if there is an email set the student email attribute (ex. check for .com or .edu)
            if(".com" in item or ".edu" in item):
                email = item
                Student.email = email
                used.append(item)
        #removed all used items from the line_list
        for item in used:
            line_list.remove(item)
        #if no email was found set the attribute to unknown 
        if(email == None):
            Student.email = "Unknown"
        #same for the nine five number 
        if(nine_five_number == None):
            Student.id = "Unknown"
        #check the remaining items in the list
        if(len(line_list) == 0):
            #if nothing is left set the first and last name to be unknown 
            Student.first_name = "Unknown"
            Student.last_name = "Unknown"
        #if one item is left set that to be the first name
        elif(len(line_list) == 1):
            Student.first_name = line_list[0]
            Student.last_name = "Unknown"
        else:
            #otherwise set the first two items in the list to be first or last
            Student.first_name = line_list[0]
            Student.last_name = line_list[1]
        return Student
    
    def parse_and_store_input(self, file, database, char_split):
        """
        file obj, class.attribute -> None
        This function iterates through an input file
        """
        lines = file.readlines()
        for line in lines:
            #split by comma or by tab
            line_list = line.strip("\n").split(char_split)
            new_student = Student()
            #check for edge cases in file input
            if(len(line_list) < 4 or len(line_list) > 4):
                new_student = self.handle_poor_input_file(new_student, line_list)
                database.add(new_student)
                continue
            #set all student attributes if there is no wrong order 
            new_student.first_name = line_list[0]
            new_student.last_name = line_list[1]
            new_student.id = line_list[2]
            new_student.email = line_list[3]
            database.add(new_student)
        file.close()
        return 

