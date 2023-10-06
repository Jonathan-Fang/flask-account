from flask import Flask, redirect, url_for, request, flash # request from Flask not Python library
from flask import render_template
# import requests
import pymysql # Python to connect to MySQL

app = Flask(__name__)
app.secret_key = 'why_is_this_necessary'

@app.route("/")
def home():
    # return "successful debug line 11"
    return render_template("home.html")

@app.route("/create_account/", methods=['POST', 'GET'])
def create_account():
    if request.method == 'POST':
        test_query = request.form
        print(test_query) # debug successful 23:30
        print('printing test_query')
        connectmysql_output = connectmysql(test_query)
        print(connectmysql_output) #debug
        print('printing connectmysql_output')
        return redirect(url_for("view_account", results = connectmysql_output))
    else:
        return render_template("create_account.html", results = '')

def connectmysql(test_query): # fname, lname, usrname, psword, favnum, favelement, email, currentmood
    # connect to the database
    # MAKE SURE YOUR DATABASE IS RUNNING AND DATABASE AND TABLE IS CREATED
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Tgbmysqlr!', # hardcoding password, development vs. production, could query password
        db='flask_database',
    )

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
    print(fname)
    print('printing fname')
    lname = test_query_list[1]
    username = test_query_list[2]
    password = test_query_list[3]
    favnum = test_query_list[4]
    favelement = test_query_list[5]
    email = test_query_list[6]
    currentmood = test_query_list[7]

    # yaish = f"{fname} lol {lname} lol {username} lol {password} lol {favnum} lol {favelement} lol {email} lol {currentmood}" # how to use f strings with Jinja
    # yaish = "{} l {} l {} l {} l {} l {} l {} l {}".format(fname, lname, username, password, favnum, favelement, email, currentmood)
    # yaish = "%s fname %s lname %s username %s password %s favnum %s favelement %s email %s currentmood" % (fname, lname, username, password, favnum, favelement, email, currentmood)
    # print(yaish)

    insert_sql_query = f"""INSERT INTO flask_table(fname, lname, username, password, favnum, favelement, email, currentmood)
                        VALUES({fname}, {lname}, {username}, {password}, {favnum}, {favelement}, {email}, {currentmood})"""
    # {fname}, {lname}, {username}, {password}, {favnum}, {favelement}, {email}, {currentmood}
    # \'fnameblah\', \'lnameblah\', \'usernameblah\', \'passwordblah\', 3, \'favelementblah\', \'emailblah\', \'currentmoodblah\'
    # record = ('fnameblah', 'lnameblah', 'usernameblah', 'passwordblah', 3, 'favelementblah', 'emailblah', 'currentmoodblah')
    # record = (fname, lname, usrname, psword, favnum, favelement, email, currentmood)
    with connection: #with is a python thing
        with connection.cursor() as cursor:
            cursor.execute(insert_sql_query) # , record
            connection.commit()
            # print debug
            result = cursor.fetchall()
            print(result)
            print('Added one account')

            cursor.execute('SELECT * FROM flask_table')
            connection.commit()
            result = cursor.fetchall()
            print(result)
            print('Showing current database status in console')

            return result #test_query, technically this is from user input, not the database
    # error handling

@app.route("/view_account/")
def view_account():
    # view_results = request.args.get('results')
    view_results = request.args.get('results')
    print(view_results) # debug
    print('showing results in console')
    return render_template("view_account.html", results = view_results)
    # need to render the information into here, start with string, can get table later

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application on the local development server
    app.run(debug=True)