"""
Group 2
2/3/2020
Majed Almazrouei, Justin Becker, Dylan Conway, Kyle Diodati, Nicholas Fay
"""
from ccs_file_io import File_Input_Output
from ccs_randomization import *
#This is the first N% of the queue that cannot be touched
N = 10

INPUTFILE = "Sampleinput.txt"

class Queue:
    """
    This is a python implementation of a priority queue.
    This will be used for cold calling students. The queue
    contains tuples of student objects, their priority and their count in the 
    """
    def __init__(self, options):
        self.options = options
        self.queue = list() #our queue list items
        self.count = 0 # count of queue contents
        self.first_n = N
        self.io = File_Input_Output()
        self.rand = Randomizer(0)

    def push(self, student):
        """
        self, student (obj), int -> None
        This function is in charge of pushing to the current queue.
        It adds a new tuple of a priority with that student, a count of the queue
        and the student object.
        """
        self.queue.append(student) #add the student to the queue
        self.count += 1 #add one to the count
        return
    
    def pop(self, index):
        """
        self -> Student
        This function pops a student from the queue.
        It retrieves and returns the next highest priority student
        """
        #if there is no priority student print
        if(len(self.queue) == 0):
            print("No students are currently in the queue.")
            return
        #if there are less students in queue than index print
        elif(len(self.queue) < index):
            print("No students are currently in the queue.")
            return
        #remove student from the queue
        student = self.queue[index]
        self.queue.remove(student)
        self.reinsert_student(student)
        File_Input_Output.write_to_file(self.io, self.options.queuefile, self.queue)
        return student
    
    def calculate_first_n_students(self):
        """
        None -> int
        This function determines the number of
        first n% of students in the queue
        """
        #get the length of the queue
        queue_len = len(self.queue)
        #get the percentage of n in that queue for ex. if n = 10 and len = 100, percentage = .1
        #percentage = N/queue_len
        percentage = N
        #calculate number of students
        len_of_first_n = int(queue_len * (1 / percentage))
        return len_of_first_n
    
    def reinsert_student(self, student):
        """
        Student obj -> None
        This function is in charge of putting the popped student back into the queue
        This cannot be done in the first n students
        """
        #calculate the number of the first n students 
        first_n = self.calculate_first_n_students()
        #create a list for the first n
        first_n_students = self.queue[:first_n]
        #create a list for the rest of the students in the queue
        rest_of_queue = self.queue[first_n:]
        #randomly place that student back into the queue
        rest_of_queue.insert(randrange(len(rest_of_queue)+1), student)
        #the queue is now the concatenated version of the two lists
        self.queue = first_n_students + rest_of_queue
        return
            
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
        print("{} students are currently in the queue".format(self.count))
        return

    def randomize_nth(self):
        '''
        None -> None
        This function randomizes the first nth positions of the queue that is currently available
        '''
        temp = list() #temporary holder for new random list

        #Below randomizes front nth part of list
        self.rand.set_size(self.calculate_first_n_students()) #sets number of first n students for random class
        self.rand.randomize() #creates a randomized integer list of nth indexes in the queue

        for i in range(0, self.calculate_first_n_students()):
            temp.append(self.queue[self.rand.order[i]])

        #Below randomizes back nth part of list
        self.rand.set_size(len(self.queue)) #sets number of students left after first n for random class
        self.rand.randomize_back(self.calculate_first_n_students()) #creates a randomized integer list of length - nth indexes in the queue

        for i in range(0, len(self.queue) - self.calculate_first_n_students()):
            temp.append(self.queue[self.rand.order[i]])

        self.queue = temp #set current queue to new randomized first nth queue
        return

    
    def randomize_queue(self):
        '''
        None -> None
        This Function randomizes the queue that is currently available
        '''
        temp = list() #temporary holder for new random list
        self.rand.set_size(self.count) #sets number of students for random class
        self.rand.randomize() #creates a randomized integer list of indexes in the queue

        for i in self.rand.order:
            temp.append(self.queue[i])

        self.queue = temp #set current non-randomized queue to new randomized queue
        return

