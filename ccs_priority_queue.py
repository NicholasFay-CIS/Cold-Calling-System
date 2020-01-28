from ccs_randomization import *

class Priority_Queue:
    """
    This is a python implementation of a priority queue.
    This will be used for cold calling students. The queue
    contains tuples of student objects, their priority and their count in the 
    """
    def __init__(self):
        self.queue = list() #our queue list items
        self.count = 0 # count of queue contents
        self.rand = Randomizer(0)

    def push(self, student, priority):
        """
        self, student (obj), int -> None
        This function is in charge of pushing to the current queue.
        It adds a new tuple of a priority with that student, a count of the queue
        and the student object.
        """
        #tuple with priority (int), student object
        student_tuple = (priority, student) 
        self.queue.append(student_tuple) #add the student to the queue
        self.count += 1 #add one to the count
        return

    def get_priority_student(self):
        """
        self -> student (obj) else upon failure None is returned
        This function is intended to return the highest priority student.
        Pop function uses this function
        """
        if(len(self.queue) == 0): # if the queue is empty return None
            return None
        else:
            priority = 0 #init the priority counter to be 0
            #iterate through the queue
            for student in self.queue:
                #get that students priority in the queue
                student_priority = student[0]
                #if the student has the highest priority, update the priority variable
                if(student_priority > priority):
                    priority = student_priority
            
            #iterate through the queue
            for student in self.queue:
                #find and return the first priority student
                if(student[0] == priority):
                    return student
    
    def pop(self):
        """
        self -> Student
        This function pops a student from the queue.
        It retrieves and returns the next highest priority student
        """
        #get the priority student
        student = Priority_Queue.get_priority_student(self)
        #if there is no priority student print
        if(student ==  None):
            print("No students are currently in the queue.")
            return
        #remove student from the queue
        self.queue.remove(student)
        #deduct from the amount in the queue
        self.count -= 1
        return student
    
    def printQueue(self):
        """
        None -> None
        prints everything currently in the priority queue
        """
        print(self.queue)
        return

    def print_queue_count(self):
        """
        None -> None
        This function prints the total number of students in the queue
        """
        print("{} studentsare currently in the queue".format(self.count))
        return
    
    def randomize_queue(self):
        '''
        This Function randomizes the queue that is currently available
        '''
        temp = list() #temporary holder for new random list
        self.rand.set_size(self.count) #sets size of class for random object
        self.rand.randomize()
        for i in self.rand.order:
            temp.append(self.queue[i])
        self.queue = temp #set current non-randomized queue to new randomized queue
