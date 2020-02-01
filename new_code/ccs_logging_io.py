# imported lib
import os.path
from os import path
import fileinput
import datetime

from ccs_parser import Student

def logstudent(student, flagged):
    """
    This function completes all necessary logging operations.
    """
    currentdate = datetime.datetime.today().isoformat().split('T')[0]

    if flagged:
        flagchar = "X"
    else:
        flagchar = ""

    daylog(student, flagchar, currentdate)
    termlog(student, flagged, currentdate)
    pass

def daylog(student, flagged, currentdate):
    """
    This function must APPEND a line to the applicable daily log file.
    """

    f = ""
    if(not path.exists(currentdate + ".tsv")):
        # Create file
        f = open(currentdate + ".tsv", "a+")
        f.write("Response\tFirst\tLast\tEmail\n")
    else:
        # Open existing file
        f = open(currentdate + ".tsv", "a+")
    f.write("{}\t{}\t{}\t<{}>\n".format(flagged, student.first_name, student.last_name, student.email))

    f.close()

def termlog(student, flagged, currentdate):
    """
    This function must REPLACE a line in the term log file.
    """

    # global scope for f
    f = ""
    if(not path.exists("Term.tsv")):
        # Create file
        f = open("Term.tsv", "a+")
        f.write("TotalCalls\tTotalFlags\tFirstName\tLastName\tUOID\tEmailAddress\tDatesCalled\n")
    else:
        # Open existing file
        f = open("Term.tsv", "a+")
    # close f in case fileinput is needed
    f.close()

    # checking if the student already has an entry
    studentExists = False
    for line in fileinput.input("Term.tsv", inplace=True):

        splitline = line.split("\t")

        try:
            if(student.id in splitline[4]):
                # Student already exists

                # Total calls
                splitline[0] = str(int(splitline[0]) + 1)

                # Total flags
                if flagged:
                    splitline[1] = str(int(splitline[1]) + 1)

                # Dates called
                if currentdate not in splitline[6]:
                    splitline[6] = splitline[6].strip("\n") + ", " + currentdate + "\n"

                # printing to line
                print('\t'.join(map(str, splitline)), end='')

                # showing student exists
                studentExists = True
            else:
                print(line, end='')
        except(IndexError):
            print(line, end = '')

            
    if not studentExists:
        f = open("Term.tsv", "a+")
        flag = 0
        if flagged:
            flag = 1
        f.write("{}\t{}\t{}\t{}\t{}\t<{}>\t{}\n".format(1, flag, student.first_name, student.last_name, student.id, student.email, currentdate))
        f.close()

def main():
    """
    If this has been executed, something has gone terribly wrong.
    """
    print("If you are seeing this, get some help.")
    example = Student("First", "Last", "950000001", "none@uoregon.edu")
    logstudent(example, True)

if (1==1):
    main()