__author__ = 'phil'

# sql.py - Create a SQLite3 table and populate it with data


import _sqlite3


# create a new db if the db doesn't exist already
with _sqlite3.connect("blog.db") as connection:

    # get a cursor object so's I can execute SQL commands
    c = connection.cursor()


    # create the table
    c.execute("CREATE TABLE posts (title TEXT, post TEXT)")


    # insert dummy data into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')