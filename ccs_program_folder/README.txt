
#### Cold Calling System ####

This is a system to automate "On Deck Cold Calling" as commissioned by Prof. Anthony Hornof.

Authors: Majed Almazrouei, Justin Becker, Dylan Conway, Kyle Diodati, and Nicholas Fay

Created: 01/21/2020

### Installation ###

Pre-Requirements
    - For additional information, please see the “Required Versions of Components” section of
      the Programmer Documentation.
    - This installation requires you to have pyinstaller installed via pip3. You can read more
      about installing and using pyinstaller here. Please use pip3 to install the program instead
      of pip, to prevent using a deprecated version of Python.
    - Due to OS X permissions, it may be necessary to run the command chmod +x <filename> on
      each .command file mentioned in these instructions.

Procedure
    1) Open a terminal window and navigate to this directory using the cd command.
    2) Use terminal to execute the file ./build.command. This will build a .app directory
       that OS X will recognise. You may have to confirm to overwrite existing files.
       Type y then Enter when prompted.
    3) Use terminal to execute the file ./install.command. This will copy the newly created
       ccs_main.app to your Applications folder, and provide the necessary sample Student roster
       to the ~/Library/Application Support/CCS folder. The file Sampleinput.tsv may be modified
       to include a custom class roster before running ./install.command for convenience. If a student
       roster is already imported, this will not overwrite it.
    4) The program ccs_main should now be executable via Spotlight Search.

### Alternate Installation ###
    - Your particular installation of OS X may fail to execute the app correctly due to a non-standard
      or developer python installation. Currently, there is no known fix for this issue.
      A workaround is provided here:

        1) Open a terminal window and navigate to this directory using the cd command.
        2) Run install.command to copy students to the running location.

This program can now be executed from the folder using the command python3 ccs_main.py.
While this prevents spotlight searching for the program, it allows the user to operate
the program when the primary python environment prevents operation. It will also preserve
data and operate alongside the .app installation, when a fix becomes available.


### Directory descriptions ###
    - Root directory:
        - This directory contains all modules for the system.
        - There is also the installation script, logging data, and some UML diagrams.
