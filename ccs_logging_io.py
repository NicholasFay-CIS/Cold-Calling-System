# imported lib
from os import path
from os import mkdir
import fileinput
import datetime

from ccs_parser import Student

def logstudent(student, flagged, options):
    """
    This function completes all necessary logging operations.
    """
    currentdate = datetime.datetime.today().isoformat().split('T')[0]

    if flagged:
        flagchar = "X"
    else:
        flagchar = ""

    daylog(student, flagchar, currentdate, options)
    termlog(student, flagged, currentdate, options)
    pass

def daylog(student, flagged, currentdate, options):
    """
    This function must APPEND a line to the applicable daily log file.
    """

    f = ""
    if(not path.exists(options.logfolder + currentdate + ".tsv")):
        # Create file
        try:
            mkdir(options.logfolder)
        except FileExistsError:
            pass
        f = open(options.logfolder + currentdate + ".tsv", "a+")
        f.write("Response\tFirst\tLast\tEmail\n")
    else:
        # Open existing file
        f = open(options.logfolder + currentdate + ".tsv", "a+")
    f.write("{}\t{}\t{}\t<{}>\n".format(flagged, student.first_name, student.last_name, student.email))

    f.close()

def termlog(student, flagged, currentdate, options):
    """
    This function must REPLACE a line in the term log file.
    """
    # global scope for f
    f = ""
    if(not path.exists(options.logfolder + "Term.tsv")):
        # Create file
        try:
            mkdir(options.logfolder)
        except FileExistsError:
            pass
        f = open(options.logfolder + "Term.tsv", "a+")
        f.write("TotalCalls\tTotalFlags\tFirstName\tLastName\tUOID\tEmailAddress\tDatesCalled\n")
    else:
        # Open existing file
        f = open(options.logfolder + "Term.tsv", "a+")
    # close f in case fileinput is needed
    f.close()

    # checking if the student already has an entry
    studentExists = False
    for line in fileinput.input(options.logfolder + "Term.tsv", inplace=True):

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
        f = open(options.logfolder + "Term.tsv", "a+")
        flag = 0
        if flagged:
            flag = 1
        f.write("{}\t{}\t{}\t{}\t{}\t<{}>\t{}\n".format(1, flag, student.first_name, student.last_name, student.id, student.email, currentdate))
        f.close()