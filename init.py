"""

Module init Docstring

This module will be the starting point of the program where it will control the initial runtime logic that is executed when the program launches
this module will serve to gather user data such as existing or new user

"""

import os
import sys
import logging
from typing import Optional

from jinja2.lexer import newline_re

#Logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class init:
    """

    class definition for the initial program logic

    """

    #Class Attributes
    version = "0.1"

    userType = 0
    exit = False
    createAccount = ''

    #Constructers

    def __init__(self, name: str, value: Optional[int] = None):
        """
        Initialize the MyClass object.

        Args:
            name (str): The name associated with the class instance.
            value (Optional[int]): An optional integer value (default: None).
        """
        self.name = name
        self.value = value
        logger.info("MyClass instance created with name: %s", name)

        #load disclaimer
        if self.name is "disclaimer" or self.name is "Disclaimer" or self.name is "DISCLAIMER":
            """print disclaimer"""
            print("-=:Print Disclaimer Here:=-")
        elif self.name is None:
            print("Nothing to print")

    @classmethod
    def class_initBanner(cls):
        """
        A class method that operates on the class itself.
        """

        print("=======================================================")
        print("||\t\t\tD\tR\t3\t3\tD\t(Prototype)\t\t\t ||")
        print("=======================================================")

    def instance_menu(self):
        """
        An instance method that operates on the object.
        """
        print("Are you a new or existing user ?")
        print("[1] New User")
        print("[2] Existing User")
        print("[3] Exit")

        while True:
            userType = int(input("Your input : "))
            if userType is not [1, 2, 3]:
                if userType == 1:
                    print("New Users are required to create/register an account before using the software")
                    createAccount = input("Create account [Y/N], 'N will terminate the program' ?  ")
                    
                    if createAccount.lower() == 'y':
                        print("exexute registration/account creation logic")
                        break
                    
                    if createAccount.lower() == 'n':
                        print("Terminating the program, Good Bye !")
                        sys.exit(0)
                
                if userType == 2:
                    "launching login terminal ..."
                    break
                
                if userType == 3:
                    "Exiting the program"
                    sys.exit(0)
                    

    #def instance_menuLogic(self, input: int):

# Main guard


if __name__ == "__main__":
    # Code for testing or demonstration purposes
    obj = init(name="Disclaimer")
    print(obj)
    print(obj.class_initBanner())
    print(obj.instance_menu())
    
    #print(obj.instance_method())
    #print(MyClass.static_method())
    #print(obj.class_method())
