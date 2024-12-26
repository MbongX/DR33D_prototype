import mysql.connector

from init import logger

#establish connection
Connection = mysql.connector.connect(
    host="",  #host name
    user="",  #SQL User
    passwd="",  #SQL User Password 
    database=""  #The Name of the database to use
)

# Check if connection is successful
if Connection.is_connected():
    print("Connected to MySQL database")
    logger.info("Connected to MySQL database")

    # Create a cursor object
    cursor = Connection.cursor()
    logger.info("Course Created")
    
    cursor.execute("Select * From table")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
else:
    print("Failed to connect to MySQL database")
    logger.error(Connection.error_message)

if __name__ == "__main__":
    ""
    #Code for testing or demonstration purposes
    #obj = init(name="Disclaimer")
    #print(obj)
    #print(obj.class_initBanner())
    #print(obj.instance_menu())

    #print(obj.instance_method())
    #print(MyClass.static_method())
    #print(obj.class_method())
