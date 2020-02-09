"""
Group 2
2/3/2020
Majed Almazrouei, Justin Becker, Dylan Conway, Kyle Diodati, Nicholas Fay
"""
#imported modules
from ccs_queue import *
from ccs_parser import *
from ccs_file_io import *
from ccs_gui import *
from ccs_argparser import *
#global variables for file io

def main():
    """
    None -> None
    This is the primary function of our cold calling system. This is in charge of tying
    each file together into one main function which can be called and run our whole program.
    """
    student_count = 1
    print("Start up")
    print("Grabbing arguments")
    options = collect_and_return_args()
    print("Arguments obtained")
    print("Obtaining file object")
    file_io_inst = File_Input_Output()
    print("File object obtained.")
    parser_inst = Parser()
    database = Class_Roster()
    print("Filling database with parsed data")
    file_obj = file_io_inst.obtain_file_obj(options.queuefile)
    if(file_obj != None):
        randomized = parser_inst.parse_and_store_input(file_obj, database.class_roster)
        print("Database filled with {} students".format(len(database.class_roster)))
        for student in database.class_roster:
            print("Student {}: First Name: {} Last Name: {} 95 Number: {} Email: {}".format(student_count, student.first_name, 
            student.last_name, student.id, student.email))
            student_count += 1
        print("Writing remaining students to new file")
        file_io_inst.write_to_file(options.queuefile, database.class_roster)
        print("File {} has been updated.".format(options.queuefile))
        print("End.")
        
        gui = StudentOverlay(options)
        queue = Queue(options)
        
        for student in database.class_roster:
            queue.push(student)
        if randomized == False:
            queue.randomize_queue()
        gui.add_deck(queue)
    else:
        print("Exiting...")
    return

#call to main upon execution of this module
if __name__ == "__main__":
    main()
