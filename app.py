from flask import Flask, redirect, url_for, request, flash # request from Flask not Python library
from flask import render_template
# import requests
import pymysql # Python to connect to MySQL

app = Flask(__name__)
app.secret_key = 'why_is_this_necessary'
global totaldb

@app.route("/")
def home():
    # return "successful debug line 11"
    return render_template("home.html")

@app.route("/create_account/", methods=['POST', 'GET']) # rendering the page itself is a get request, post for form submission; 
def create_account():
    if request.method == 'POST':
        test_query = request.form
        # print(test_query) # debug successful 23:30
        print('printing test_query')
        insertintodb(test_query)
        return redirect(url_for("view_account")) # , results = connectmysql_output, dynamically generates URL
    else:
        return render_template("create_account.html", results = '')

def connectmysql(): # fname, lname, usrname, psword, favnum, favelement, email, currentmood # this is a helper function, don't call them on their own, used to help other functions
    # connect to the database
    # ------------------------------------------------------------------- #
    # MAKE SURE YOUR DATABASE IS RUNNING AND DATABASE AND TABLE IS CREATED
    # ------------------------------------------------------------------- #

    sqlcreds = open("sqlcreds.txt", "r")
    credsls = []
    for line in sqlcreds:
        line = line.rstrip() # removes \n in text files
        line = line.split('=') # creating 4 lists, two things in each
        credsls.append(line[1])

    # print(credsls) # debug
    # print(type(credsls[0])) # debug type
    connection = pymysql.connect(
        host = credsls[0], # asking for str, connecting to sql vs. sql call
        user = credsls[1],
        password = credsls[2],
        db = credsls[3],

        # host='localhost',
        # user='root',
        # password='Tgbmysqlr!', # hardcoding password, development vs. production, could query password
        # db='flask_database',
    )

    return connection

def insertintodb(test_query):
    global totaldb
    connection = connectmysql()
    #i need python to somehow take user input and feed it to the server
    # first print input fields successfully in the console
    # turn input fields into var
    # input fields into the pymysql
    # take those values and spit it back into view_account

    # do i need to loop through the list and get the values and spit it into the string?
    # convert test_query to list to index?
    test_query_list = list(test_query.values())
    print(test_query_list)
    print('printing list')
    fname = test_query_list[0]
    # print(fname)
    # print('printing fname')
    # print(type(fname)) # debug fname var type
    lname = test_query_list[1]
    username = test_query_list[2]
    password = test_query_list[3]
    favnum = test_query_list[4]
    favelement = test_query_list[5]
    email = test_query_list[6]
    currentmood = test_query_list[7]

    insert_sql_query = f"INSERT INTO flask_table(fname, lname, username, password, favnum, favelement, email, currentmood) VALUES('{fname}', '{lname}', '{username}', '{password}', {favnum}, '{favelement}', '{email}', '{currentmood}')" # SQL wants quotes for strings, SQL thought it was a variable, Python thought it was string
    
    with connection: #with is a python thing
        with connection.cursor() as cursor:
            cursor.execute(insert_sql_query) # , record
            connection.commit()
            # print debug
            result = cursor.fetchall()
            # print(result)
            print('Added one account')

            cursor.execute('SELECT * FROM flask_table')
            connection.commit()
            result = cursor.fetchall()
            print(result)
            print('Showing current database status in console')

            # print(type(result[3][2])) # debug
            # print(result[3][2]) # debug lname
            # print(len(result)) # debug
            totaldb = result

            return result #test_query, technically this is from user input, not the database
    # error handling

@app.route("/view_account/") # it's default doing a GET request to even render the page when the user sees it
def view_account():
    view_results = totaldb
    print(view_results) # debug
    print('showing results in console')
    return render_template("view_account.html", results = view_results)
    # need to render the information into here, start with string, can get table later

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application on the local development server
    app.run(debug=True)