from ccs_file_io import File_Input_Output
from ccs_randomization import *
from ccs_argparser import INPUTFILE
#This is the first N% of the queue that cannot be touched
N = 1

class Queue:
    """
    This is a python implementation of a priority queue.
    This will be used for cold calling students. The queue
    contains tuples of student objects, their priority and their count in the 
    """
    def __init__(self):
        self.queue = list() #our queue list items
        self.count = 0 # count of queue contents
        self.first_n = N
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
    
    def pop(self):
        """
        self -> Student
        This function pops a student from the queue.
        It retrieves and returns the next highest priority student
        """
        #if there is no priority student print
        if(len(self.queue) == 0):
            print("No students are currently in the queue.")
            return
        #remove student from the queue
        student = self.queue[0]
        self.queue.remove(student)
        #deduct from the amount in the queue
        self.count += 1
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
        percentage = N/queue_len
        #calculate number of students
        len_of_first_n = int(queue_len * percentage)
        return len_of_first_n
    
    def reinsert_student(self, student):
        """
        Student obj -> None
        This function is in charge of putting the popped student back into the queue
        This cannot be done in the first n students
        """
        #calculate the number of the first n students 
        first_n = Queue.calculate_first_n_students(self)
        #create a list for the first n
        first_n_students = self.queue[:first_n]
        #create a list for the rest of the students in the queue
        rest_of_queue = self.queue[first_n:]
        #randomly place that student back into the queue
        rest_of_queue.insert(randrange(len(rest_of_queue)+1), student)
        #the queue is now the concatenated version of the two lists
        self.queue = first_n_students + rest_of_queue
        #save the queue state in the file
        File_Input_Output.write_to_file(self, INPUTFILE, self.queue)
        self.count += 1
        return
    
    def get_on_deck(self):
        """
        None -> list
        This function is in charge of getting the next 4 students
        who are on deck. A student will be poped, put in the list of on deck
        and placed back in the queue for the next time they will be on deck
        """
        on_deck = list()
        #get 4 students
        for i in range(0, 4):
            #pop the student
            student = Queue.pop(self)
            #add them to the on deck list
            on_deck.append(student)
            #randomly reinsert that student somewhere that is not in the first n% of the queue
            Queue.reinsert_student(self, student)
        return on_deck
            
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
    
    def randomize_queue(self):
        '''
        None -> None
        This Function randomizes the queue that is currently available
        '''
        temp = list() #temporary holder for new random list
        self.rand.set_size(self.count) #sets size of class for random object
        self.rand.randomize()
        for i in self.rand.order:
            temp.append(self.queue[i])
        self.queue = temp #set current non-randomized queue to new randomized queue
        return

queue = Queue()
i = 1
while i < 21:
    queue.push(i)
    i += 1
on_deck = queue.get_on_deck()
print(on_deck)