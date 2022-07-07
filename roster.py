import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite3')

# like a file handle to the dtb server.
# Send sql commands thru cursor and read the cursor
# to get the data back.
cur = conn.cursor()

# do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name        TEXT UNIQUE

);

CREATE TABLE Course (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title       UNIQUE
);


CREATE TABLE Member(
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)

''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

str_data = open(fname).read()

#parsing json to get an array of arrays
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0];
    title = entry[1];

# print it out as a tuple
    print((name, title))

#ignore lets you try to put in the same name twie
# ? is a pladce holder
# name will substitute in for the ?
# avoiding sql injection

#insert if it doesn't exist
    cur.execute(''' INSERT OR IGNORE INTO User (name)
    VALUES ( ? )''', (name, ) )

    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))

    #fetch one record from the cursor to assign to user_id
    #get the new or the original id field
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
    VALUES ( ? )''', ( title, ) )

    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    course_id= cur.fetchone()[0]

#effectively becomes an update statements if the primary key is already there
    cur.execute('''INSERT OR REPLACE INTO Member
    (user_id, course_id) VALUES ( ?, ? )''',
    (user_id, course_id) )

#write to disk
    conn.commit()
