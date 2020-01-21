class PriorityQueue:
    """
    This is a python implementation of a priority queue
    """
    def __init__(self):
        self.queue = [] #our queue list items
        self.count = 0

    def push(self, student, priority):
        student_tuple = (priority, self.count, student)
        self.queue.append(student_tuple)
        self.count += 1
        return

    def get_priority_student(self):
        priority = 0
        if(len(self.queue) == 0):
            return None
             
        for student in self.queue:
            student_priority = student[0]
            if(student_priority > priority):
                priority = student_priority
        for student in self.queue:
            if(student[0] == priority):
                return student
    
    def pop(self):
        student = PriorityQueue.get_priority_student(self)
        print(student)
        if(student ==  None):
            print("No students are currently in the queue.")
        else:
            self.queue.remove(student)
            self.count -= 1
            return student
    
    def printQueue(self):
        print(self.queue)
        return

        