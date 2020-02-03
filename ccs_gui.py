from tkinter import Tk, Canvas, NW
from tkinter import messagebox
from ccs_parser import *
from ccs_file_io import *
from ccs_queue import *
from ccs_main import *
from ccs_argparser import *
from ccs_file_io import File_Input_Output
from ccs_logging_io import logstudent

OUTPUT_FILE = "Sampleoutput.txt"

root = Tk()

class StudentOverlay:
    """
    The gui module of the system that will display four
    student names in the foreground. The user is able to
    select one of the students with left/right arrow keys
    and up/down keys to remove a student name, up
    with a flag, down without a flag.

    """
    def __init__(self, options):

        # tkinter widget root.
        #root = Tk()
        root.attributes("-topmost", True)
        root.title("Selected students")
        root.focus_force()
        root.geometry("+{xPos}+{yPos}".format(xPos = -7, yPos=0)) #

        #File I/O
        self.options = options
        file_io_inst = File_Input_Output()
        parser_inst = Parser()
        self.database = Class_Roster()
        self.queue = Queue(options)

        # Create canvas to draw student names to.
        #canvas = Canvas(root, width=600, height=30)
        canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight() * .05)
        canvas.pack()
        #canvas.place(relx=0.5, rely=0.0)

        # Bind event handlers.
        root.bind("<Motion>", self.on_mousemove)
        root.bind("<Button-1>", self.on_click)
        root.bind("<Left>", self.on_press_left)
        root.bind("<Right>", self.on_press_right)
        root.bind("<Up>", self.on_press_up)
        root.bind("<Down>", self.on_press_down)

        # Assign class attributes.
        self.root = root
        self.canvas = canvas
        self.students = list()
        self.selected_index = 0

        # self.errors("Something is wrong with the program, plz uninstall.")

    def error_popup(self, error_string):
        messagebox.showerror("Error", error_string)

    def on_mousemove(self, event):
        pass

    def on_click(self, event):
        pass

    def on_press_left(self, event):
        if(self.selected_index > 0):
            self.selected_index -= 1
        self.update()

    def on_press_right(self, event):
        if(self.selected_index < 3):
            self.selected_index += 1
        self.update()

    def on_press_up(self, event):
        student = self.students.pop(self.selected_index)
        student = self.queue.queue[self.selected_index]
        self.drop_student_from_list(student, True)

    def on_press_down(self, event):
        student = self.students.pop(self.selected_index)
        student = self.queue.queue[self.selected_index]
        #print(student)
        self.drop_student_from_list(student, False)

    def add_student(self, student, index):
        student_widget = StudentWidget(student)
        checker = False
        #Below checks if the student we are adding is already ondeck
        for index in self.students:
            if student_widget.student == index.student:
                checker = True
                #print("FOUND DUPLICATE                    FOUND DUPLICATE")
        if checker == True: #If student was ondeck, attempts to add next student in queue
            self.add_student(self.queue.queue[index + 1], index + 1)
        else:
            self.students.append(student_widget)
            self.update()
            print("Added student:", student_widget, "to the GUI")
    
    def drop_student_from_list(self, student, flag: bool):
        if(flag):
            print("Dropped", student.first_name, "with a flag.")
        else:
            print("Dropped", student.first_name, "without a flag.")
        logstudent(student, flag, self.options)
        self.queue.pop(self.selected_index)
        #self.queue.randomize_queue() #Commented out because unnecessary to randomize again
        self.add_student(self.queue.queue[4], 4)        
        
    def add_deck(self, queue):
        """
        This is a simple example of how the gui
        would be used with the rest of the program.
        """
    ### Initialize the overlay gui with other objects:
    # overlay = StudentOverlay()                   
    ### Pass the students to the overlay with .add_student()                                 
    ### add_student() can take either a list of names as an argument or a string for one name
        #self.database = database
        #for student in self.database.class_roster:
        #    self.queue.push(student)
        # print("after", self.queue.queue)
        #on_deck = self.queue.get_on_deck()
        #on_deck = list(map(str, on_deck))
        self.queue = queue
        for index in range(0, 4):
            self.add_student(self.queue.queue[index], index)
        self.loop()

    def update(self):
        # Clear the canvas
        self.canvas.delete("all")
        # Redraw all the students
        for index, student in enumerate(self.students):
            student.draw(self.canvas, index, self.selected_index)

    def loop(self):
        self.root.mainloop()


class StudentWidget:
    """
    Student widget that is displayed in the overlay.
    """
    def __init__(self, student):
        self.student = student
        #self.width = 150
        self.width = root.winfo_screenwidth() * .25
        #self.height = 30
        self.height = root.winfo_screenheight() * .05

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name

    def draw(self, canvas, index: int, selected_index: int):
        if(index == selected_index):
            canvas.create_rectangle(index * self.width, 0, (index + 1) * self.width, self.height, fill="gray", outline="gray")
        canvas.create_text(20 + index * self.width, self.height / 2 - 12, text=self.student.first_name + " " + self.student.last_name, anchor=NW, fill="black", font=("Helvetica", 20))

# class FileNotFoundWidget:
#     def __init__(self):
#         self.text = "Input file not found"
#         self.window = 
#print("here is bug")
#overlay = StudentOverlay()


#def main():

    """
    This is a simple example of how the gui
    would be used with the rest of the program.
    """

    ### Initialize the overlay gui with other objects:
    # overlay = StudentOverlay()

    ### Pass the students to the overlay with .add_student()
    ### add_student() can take either a list of names as an argument or a string for one name
#    students = [
#        "Bird",
#        "Frog",
#        "Fish",
#        "Worm"
#    ]
#    overlay.add_student(students)

    ### Call .loop() to start it's draw loop
#    overlay.loop()

"""
def drop_student_from_list(name: str, flag: bool):
    if(flag):
        print("Dropped", name, "with a flag.")
    else:
        print("Dropped", name, "without a flag.")
    overlay.add_student("Bill")
"""

#if __name__ == "__main__":
#    main()

