#imported modules
from ccs_queue import *
from ccs_parser import *
from ccs_file_io import *
from ccs_gui import *
#global variables for file io
INPUT_FILE = "Sampleinput.txt"
OUTPUT_FILE = "Sampleoutput.txt"

def main():
    """
    None -> None
    ####W.I.P#####
    (Work in progress, temp main function)
    """
    student_count = 1
    print("Start up")
    print("Obtaining file object")
    file_io_inst = File_Input_Output()
    print("File object obtained.")
    parser_inst = Parser()
    database = Class_Roster()
    print("Filling database with parsed data")
    file_obj = file_io_inst.obtain_file_obj(INPUT_FILE)
    parser_inst.parse_and_store_input(file_obj, database.class_roster)
    print("Database filled with {} students".format(len(database.class_roster)))
    for student in database.class_roster:
        print("Student {}: First Name: {} Last Name: {} 95 Number: {} Email: {}".format(student_count, student.first_name, 
        student.last_name, student.id, student.email))
        student_count += 1
    print("Writing remaining students to new file")
    file_io_inst.write_to_file(OUTPUT_FILE, database.class_roster)
    print("File {} has been updated.".format(OUTPUT_FILE))
    print("End.")
    
    gui = StudentOverlay()
    queue = Queue()
    
    #for student in database.class_roster:
    #    queue.push(student.first_name)
    #print(queue.queue)
    #on_deck = queue.get_on_deck()
    #print(on_deck)
    gui.add_deck(database)
    return

#call to main upon execution of this module
if __name__ == "__main__":
    main()
