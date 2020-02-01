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

class StudentOverlay:
    """
    The gui module of the system that will display four
    student names in the foreground. The user is able to
    select one of the students with left/right arrow keys
    and up/down keys to remove a student name, up
    with a flag, down without a flag.

    """
    def __init__(self):

        # tkinter widget root.
        root = Tk()
        root.attributes("-topmost", True)
        root.title("Selected students")
        root.focus_force()

        #File I/O
        file_io_inst = File_Input_Output()
        parser_inst = Parser()
        self.database = Class_Roster()
        self.queue = Queue()

        # Create canvas to draw student names to.
        canvas = Canvas(root, width=600, height=30)
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
        self.students = []
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
        self.drop_student_from_list(student, True)

    def on_press_down(self, event):
        student = self.students.pop(self.selected_index)
        self.drop_student_from_list(student, False)

    def add_student(self, student):
        student_widget = StudentWidget(student)
        self.students.append(student_widget)
        self.update()
        print("Added student:", student_widget, "to the GUI")
    
    def drop_student_from_list(self, student, flag: bool):
        if(flag):
            print("Dropped", student, "with a flag.")
        else:
            print("Dropped", student, "without a flag.")
        logstudent(student, flag)
        self.queue.randomize_queue()
        self.add_student(self.queue.queue[0])        
        
    def add_deck(self, database):
        """
        This is a simple example of how the gui
        would be used with the rest of the program.
        """
    ### Initialize the overlay gui with other objects:
    # overlay = StudentOverlay()                   
    ### Pass the students to the overlay with .add_student()                                 
    ### add_student() can take either a list of names as an argument or a string for one name
        self.database = database
        for student in self.database.class_roster:
            self.queue.push(student)
        # print("after", self.queue.queue)
        on_deck = self.queue.get_on_deck()
        on_deck = list(map(str, on_deck))
        self.add_student(on_deck)
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
        self.width = 150
        self.height = 30

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name

    def draw(self, canvas, index: int, selected_index: int):
        if(index == selected_index):
            canvas.create_rectangle(index * self.width, 0, (index + 1) * self.width, self.height, fill="gray", outline="gray")
        canvas.create_text(20 + index * self.width, 8, text=self.student.first_name, anchor=NW, fill="black", font="Helvetica")

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

