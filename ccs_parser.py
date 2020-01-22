#imported lib
from collections import namedtuple

class Student:
    """
    This class is intended to initialize a student object with the attributes
    that have been parsed
    """
    def do_local(self, first=None, last=None, ID=None, email=None):
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
    
    def parse_and_store_input(self, file, database):
        """
        file obj, class.attribute -> None
        This function iterates through an input file
        """
        file.readline()
        lines = file.readlines()
        for line in lines:
            line_list = line.strip("\n").split("\t")
            new_student = Student()
            new_student.first_name = line_list[0]
            new_student.last_name = line_list[1]
            new_student.id = line_list[2]
            new_student.email = line_list[3]
            database.add(new_student)
        return
    

