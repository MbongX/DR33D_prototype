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
from database_connector import DatabaseConnector


#Logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Init:
    """

    class definition for the initial program logic

    """

    #Class Attributes
    version = "0.1"

    userType = 0
    sysExit = False
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
        if self.name == "disclaimer" or self.name == "Disclaimer" or self.name == "DISCLAIMER":
            """print disclaimer"""
            print("-=:Print Disclaimer Here:=-")
        elif self.name is None:
            print("Nothing to print")
    @staticmethod
    def terminate(self, value: bool):
        self.value = value
        if self.value is True:
            sys.exit(0)
        else:
            logger.log(self.value, "No termination code triggered")

    @classmethod
    def init_banner(cls):
        """
        A class method that operates on the class itself.
        """

        print("=======================================================")
        print("||\t\t\tD\tR\t3\t3\tD\t(Prototype)\t\t\t ||")
        print("=======================================================")

    def menu(self):
        """
        An instance method that operates on the object.
        """
        print("Are you a new or existing user ?")
        print("[1] New User")
        print("[2] Existing User")
        print("[3] Exit")

        while True:
            user_type = int(input("Your input : "))
            if user_type is not [1, 2, 3]:
                if user_type == 1:
                    print("New Users are required to create/register an account before using the software")
                    create_account = input("Create account [Y/N], 'N will terminate the program' ?  ")
                    
                    if create_account.lower() == 'y':
                        print("execute registration/account creation logic")
                        break
                    
                    if create_account.lower() == 'n':
                        print("Terminating the program, Good Bye !")
                        sys_exit = True
                        sys.exit(0)
                
                elif user_type == 2:
                    print("launching login terminal ...")
                    break
                
                elif user_type == 3:
                    print("Exiting the program")
                    sys_exit = True
                    sys.exit(0)
                    

    #def instance_menuLogic(self, input: int):

# Main guard


if __name__ == "__main__":
    # Code for testing or demonstration purposes
    data = database_connector()
    obj = init(name="Disclaimer")
    print(obj)
    print(obj.class_initBanner())
    print(obj.instance_menu())
    
    #print(obj.instance_method())
    #print(MyClass.static_method())
    #print(obj.class_method())
