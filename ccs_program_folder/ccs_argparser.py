"""
Group 2
2/3/2020
Majed Almazrouei, Justin Becker, Dylan Conway, Kyle Diodati, Nicholas Fay
"""
import argparse
import os
#FIX ME:
#PUT REAL DEFAULT FILE PATHS!!!!!!
QUEUEFILE = os.path.expanduser("~/Library/Application Support/CCS/Students.tsv")
LOGFOLDER = os.path.expanduser("~/Library/Application Support/CCS/logging/")

def obtain_command_line_args():
    """
    None -> Namespace
    This function is in charge of collecting input via command line. 
    """
    #create argparser
    argparser = argparse.ArgumentParser()
    #add the two arguments we want
    argparser.add_argument('--queuefile', nargs=1, required=False, help="This is the input file with all students information to populate the queue.")
    argparser.add_argument('--logfolder', nargs=1, required=False, help="This is the folder that shows which students have or have not participated.")
    #create the namespace
    program_options = argparser.parse_args()
    return program_options

def argparse_helper(options):
    """
    Namespace -> Namespace
    This function adjusts the values of the program options.
    Since nargs is set to 1, each options value is a list of the args, so
    since we only have one argument we take the first index of that list.
    If the options were not specified default to hard set input file and saved state file
    """
    #check if input file was given
    if(options.queuefile != None):
        options.queuefile = options.queuefile[0]
    else:
        #if not result to default
        options.queuefile = QUEUEFILE
    #check if savedstate file was given
    if(options.logfolder != None):
        options.logfolder = options.logfolder[0]
    else:
        #if not result to default 
        options.logfolder = LOGFOLDER
    return options

def collect_and_return_args():
    """
    None -> Namespace
    This function ties the two functions above together.
    """
    #obtain the options for the program
    options = obtain_command_line_args()
    #adjust value types
    options = argparse_helper(options)
    return options
