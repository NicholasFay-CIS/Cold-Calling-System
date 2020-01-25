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
        root.title("Selected students")
        root.focus_force()

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
        name = self.students.pop(self.selected_index)
        drop_student(name, 1)

    def on_press_down(self, event):
        name = self.students.pop(self.selected_index)
        drop_student(name, 0)

    def add_student(self, name: str):
        student = StudentWidget(name)
        self.students.append(student)
        self.update()
        print("Added student:", student)

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
    def __init__(self, name: str):
        self.name = name
        self.width = 150
        self.height = 30

    def __str__(self):
        return self.name

    def draw(self, canvas, index: int, selected_index: int):
        if(index == selected_index):
            canvas.create_rectangle(index * self.width, 0, (index + 1) * self.width, self.height, fill="gray")
        canvas.create_text(20 + index * self.width, 8, text=self.name, anchor=NW, fill="black", font="Impact")

overlay = StudentOverlay()

def main():
    """
    This is a simple example of how the gui
    would be used with the rest of the program.
    """

    ### Initialize the overlay gui with other objects:
    # overlay = StudentOverlay()

    ### Pass the students to the overlay with .update_students()
    students = [
        "Bird",
        "Frog",
        "Fish",
        "Worm"
    ]
    for name in students:
        overlay.add_student(name)

    ### Call .loop() to start it's draw loop
    overlay.loop()

def drop_student(name: str, flag: bool):
    if(flag):
        print("Dropped", name, "with a flag.")
    else:
        print("Dropped", name, "without a flag.")
    overlay.add_student("Bill")


if __name__ == "__main__":
    main()

