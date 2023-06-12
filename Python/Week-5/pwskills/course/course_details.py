import os, sys
# Python OS module provides the facility to establish the interaction between the user and the operating system. It offers many useful OS functions that are used to perform OS-based tasks and get related information about operating system.

from os.path import dirname, join , abspath

# The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. It lets us access system-specific parameters and functions. import sys. First, we have to import the sys module in our program before running any functions.

sys.path.insert(0,abspath(join(dirname(__file__),'..')))
from payment import payment_details

def course():

    print("This is course details")

payment_details.payment()
