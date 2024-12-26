import os
import sys


import mysql.connector

from mysql.connector import Error
from pycparser.c_ast import While

from init import logger
from typing import Optional

class DatabaseConnector:
    """
    
    Database Connector Class
    
    """
    
    #Class Attributes
    version = "0.1"
    db_host = ""
    db_user = ""
    db_password = ""
    db_database = ""
    db_instance_count = 0
    db_cursor = None
    row_count = 0
    user_info = []
    
        #Constructor
    def __init__(self, host: str, user: str, password: str, database: str, count: Optional[int] = None):
        """
        
        Initialize Database Connector
        
        """
        
        logger.info("Database Connector Initialized")
        DatabaseConnector.db_host = host
        DatabaseConnector.db_user = user
        DatabaseConnector.db_password = password
        DatabaseConnector.db_database = database
        self.db_instance_count = count
        
        #connection = mysql.connector.connect()
        if count == None:
            count = 1
            DatabaseConnector.db_instance_count += count

    @classmethod
    def initialize_database(cls):
        if DatabaseConnector.db_instance_count == 1:
            try:
                connection = mysql.connector.connect(
                    host = DatabaseConnector.db_host,
                    user = DatabaseConnector.db_user,
                    password = DatabaseConnector.db_password,
                    database = DatabaseConnector.db_database
                )

                # Check if connection is successful
                if connection.is_connected():
                    print("Connected to MySQL database")

                    logger.info("Connected to MySQL database")
                    return connection
                else:
                    print("Failed to connect to MySQL database")
                    logger.error(connection.error_message)
                    connection.close()
                    logger.error("Connection to MySQL database has been terminated")
                    return "Connection to MySQL database has been terminated"

            except Error as e:
                print("Error while connecting to MySQL", e)
                logger.error(e)
                connection.close()
                logger.error("Connection to MySQL database has been terminated")
                return e
            
    @classmethod
    def select_user_operations(self, user: str):
        """
        instance methods for class
    
        :param self: 
        :param Client's username: 
        :return: client's username, if available on the database else None
        """
    
        self.user = user
        iii = 0
    
        #logger.debug("Instance method called for name: %s", self.name)
    
        init = DatabaseConnector.initialize_database()
    
        #if init is not None or type(init) != Error or init != "Connection to MySQL database has been terminated":
        if init.is_connected():

                DatabaseConnector.db_cursor = init.cursor()

                # Create Connection/Execute Query
                DatabaseConnector.db_cursor.execute(f"SELECT * FROM table WHERE Username  = '{self.user}'")
                #Fecthing results
                rows = DatabaseConnector.db_cursor.fetchall()
                #Get row count
                DatabaseConnector.row_count = DatabaseConnector.db_cursor.rowcount
                #Check if there are any records returned
                if DatabaseConnector.db_cursor.rowcount > 0:
                    logger.info("User found")
                    for row in rows:
                        DatabaseConnector.user_info.append(row)

                    for rowss in rows:
                        print(rowss) 
                    
                else:
                    logger.error("User could not be found in the database")
        else:
            if type(init) is Error :
                logger.error(str(init) + " | Thus could not execute search on database for user")
            else:
                logger.error(str(init) + " | Thus could not execute search on database for user")
                
if __name__ == "__main__":
    """
    Testing purposes
    """
    obj = DatabaseConnector(host= "", user = "", password = "", database = "")
    #obj.initialize_database()
    obj.select_user_operations(user = "")