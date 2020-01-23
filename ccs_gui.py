from tkinter import *

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
        root.focus_set()

        # Create canvas to draw student names to.
        canvas = Canvas(root, width=0, height=0)

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

    def on_mousemove(self, event):
        print(event.x, event.y)

    def on_click(self, event):
        print(event.x, event.y)

    def on_press_left(self, event):
        self.canvas.create_line(0, 0, 100, 100, fill="blue")
        self.canvas.config(width=100, height=100)
        self.canvas.pack()
        print("pressed left!")

    def on_press_right(self, event):
        print("pressed right!")

    def on_press_up(self, event):
        print("pressed up!")

    def on_press_down(self, event):
        print("pressed down!")

    def update_students(self, students):
        for student in students:
            self.students.append(student)

    def loop(self):
        self.root.mainloop()


def main():
    """
    This is a simple example of how the gui
    would be used with the rest of the program.
    """

    ### Initialize the overlay gui with other objects:
    overlay = StudentOverlay()

    ### Pass the students to the overlay with .update_students()
    students = [
        "Bird",
        "Frog",
        "Fish",
        "Worm"
    ]
    overlay.update_students(students)

    ### Call .loop() to start it's draw loop
    overlay.loop()


if __name__ == "__main__":
    main()
