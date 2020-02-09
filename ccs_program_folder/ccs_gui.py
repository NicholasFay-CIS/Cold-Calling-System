"""
Group 2
2/3/2020
Majed Almazrouei, Justin Becker, Dylan Conway, Kyle Diodati, Nicholas Fay
"""
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
        '''
        Namespace -> None
        Initializes a StudentOverlay Class to have a tkinter object root and a tkinter canvas,
        and setup the class to contain modules of file io, parser, and queue. 
        '''

        # tkinter widget root.
        root.attributes("-topmost", True)
        root.title("Selected students")
        root.focus_force()
        root.geometry("+{xPos}+{yPos}".format(xPos = -7, yPos=0))

        #File I/O
        self.options = options
        file_io_inst = File_Input_Output()
        parser_inst = Parser()
        self.database = Class_Roster()
        self.queue = Queue(options)

        # Create canvas to draw student names to.
        canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight() * .05)
        canvas.pack()

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

    def on_mousemove(self, event):
        '''
        tkinter event object -> None
        on moving the mouse, do nothing.
        '''
        pass

    def on_click(self, event):
        '''
        tkinter event object -> None
        on clicking the mouse, do nothing.
        '''
        pass

    def on_press_left(self, event):
        '''
        tkinter event object -> None
        on pressing the left arrow key, move selected student left on gui.
        '''
        if(self.selected_index > 0):
            self.selected_index -= 1
        self.update()

    def on_press_right(self, event):
        '''
        tkinter event object -> None
        on pressing the right arrow key, move selected student right on gui.
        '''
        if(self.selected_index < 3):
            self.selected_index += 1
        self.update()

    def on_press_up(self, event):
        '''
        tkinter event object -> None
        on pressing the up arrow key, remove the student from the deck and flag them.
        '''
        student = self.students.pop(self.selected_index)
        student = self.queue.queue[self.selected_index]
        self.drop_student_from_list(student, True)

    def on_press_down(self, event):
        '''
        tkinter event object -> None
        on pressing the down arrow key, remove the student from the deck and don't flag them.
        '''
        student = self.students.pop(self.selected_index)
        student = self.queue.queue[self.selected_index]
        self.drop_student_from_list(student, False)

    def add_student(self, student, index):
        '''
        student object, integer -> None
        adds a student to the on screen display, and checks if they are not already in deck.
        '''
        student_widget = StudentWidget(student)
        checker = False
        #Below checks if the student we are adding is already ondeck
        for s in self.students:
            if student_widget.student == s.student:
                checker = True
        if checker == True: #If student was ondeck, attempts to add next student in queue
            self.add_student(self.queue.queue[index + 1], index + 1)
        else:
            self.students.append(student_widget)
            self.update()
            print("Added student:", student_widget, "to the GUI")
    
    def drop_student_from_list(self, student, flag: bool):
        '''
        student object, boolean -> None
        removes a student from list and logs them with or without a flag for day and term.
        '''
        if(flag):
            print("Dropped", student.first_name, "with a flag.")
        else:
            print("Dropped", student.first_name, "without a flag.")
        logstudent(student, flag, self.options)
        self.queue.pop(self.selected_index)
        self.add_student(self.queue.queue[3], 3)        
        
    def add_deck(self, queue):
        """
        queue object -> None
        sets the deck to be displayed in the gui on startup.
        """
        self.queue = queue
        for index in range(0, 4):
            self.add_student(self.queue.queue[index], index)
        self.loop()

    def update(self):
        '''
        None -> None
        updates the canvas to have the most current students and highlighting.
        '''
        # Clear the canvas
        self.canvas.delete("all")
        # Redraw all the students
        for index, student in enumerate(self.students):
            student.draw(self.canvas, index, self.selected_index)

    def loop(self):
        '''
        None -> None
        runs the tkinter mainloop
        '''
        self.root.mainloop()


class StudentWidget:
    """
    Student widget that is displayed in the overlay.
    """
    def __init__(self, student):
        '''
        student object -> None
        initializes the creation of a StudentWidget with a student object, and sets
        the size of each StudentWidget object for placement on the tkinter canvas.
        '''
        self.student = student
        self.width = root.winfo_screenwidth() * .25
        self.height = root.winfo_screenheight() * .05

    def __str__(self):
        '''
        None -> string
        returns the represenation of a StudentWidget as a string.
        '''
        return self.student.first_name + " " + self.student.last_name

    def draw(self, canvas, index: int, selected_index: int):
        '''
        tkinter canvas, integer, integer -> None
        draws the student object onto the tkinter canvas, and writes the student class.
        '''
        if(index == selected_index):
            canvas.create_rectangle(index * self.width, 0, (index + 1) * self.width, self.height, fill="gray", outline="gray")
        canvas.create_text(20 + index * self.width, self.height / 2 - 12, text=self.student.first_name + " " + self.student.last_name, anchor=NW, fill="black", font=("Helvetica", 20))


