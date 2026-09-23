

import flask
import werkzeug.security

import database
app = flask.Flask(__name__)
@app.route('/')
def index():
    return flask.render_template("Title.html")






#ok so this is the flask route for the signup page that allows me to make a path to the other pages.
#the function below for the sign up page will take in the inputs for the password and username and then will check if the password is long enough, before it runs another function i made to input these values into the users table in my database
#after the function is ran it should send you to the dashboard
@app.route("/SignUp", methods=['GET', 'POST'])
def signup():
    if flask.request.method == "POST":
        username = flask.request.form.get('username')
        password = flask.request.form.get('password')
        if len(password) < 8 :
            return "error"
        else:
            database.create_user(username, password)
            return flask.redirect(flask.url_for("Dashboard"))
    else:

        return flask.render_template('SignUp.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if flask.request.method == "POST":
        username = flask.request.form.get('username')
        password = flask.request.form.get('password')
# code here doesnt currently work if the username is nothing, (row = none if it cant find the username????)
        row = database.fetch_users(username)

        password_hash = row[2]
        if werkzeug.security.check_password_hash(password_hash, password):
            return flask.redirect(flask.url_for("Dashboard"))
        else:
            return flask.render_template('Login.html')
    else:
        return flask.render_template('Login.html')

#this is the flask route i made for the dashboard page, which is necessary as it needs to be rendered here for the functions to work
@app.route("/dashboard", methods=['GET', 'POST'])
def Dashboard ():
    return flask.render_template("Dashboard.html")



#ok so while testing this out i realised i needed two different routes for the calendar:
# one for the page itself, and another for each timeslot you flip between (like switching every month/week)
import calendar
from datetime import date
@app.route("/calendar", methods=['GET', 'POST'])
def Calendar ():
    today = date.today()
    return flask.redirect(flask.url_for("CalendarMonth", year = today.year, month=today.month))


@app.route("/calendar/<int:year>/<int:month>", methods=['GET', 'POST'])
def CalendarMonth (year,month):
    today = date.today()
    cal = calendar.Calendar(firstweekday=0) #0 is monday on weekday
    weeks = cal.monthdayscalendar(year,month)#this lists every week which is like another list in itself (so im doing like a 2d array n that to make a grid get it)

    monthname = calendar.month_name[month]
#then write out the system to decide w3hat the next and prior month is, so that when a user tries to flip between months the correct one gets given
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year

    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

#calendar system works like this
#browser gets the /calender which only takes the current month and redirects the system to that
#this will make sure that the calenmdar system wont be stuck to one date or time, and will try to track time well
# [0,  1,  2,  3,  4,  5,  6],   #so the grid should be similar to this kind of design i think
# [7,  8,  9,  10, 11, 12, 13],
# [14, 15, 16, 17, 18, 19, 20],
# [21, 22, 23, 24, 25, 26, 27],
# [28, 29, 30, 0,  0,  0,  0],

#now at the end i have to pass a bunch of variables so i can use them in the actual http file later so like i can display the right dates and stuff
    return flask.render_template(
            "Calendar.html",
            weeks=weeks,
            month_name=monthname,
            year=year, month=month,
            prev_month=prev_month, prev_year=prev_year,
            next_month=next_month, next_year=next_year,
            today= today.day if (year, month) == (today.year, today.month) else None
        )
@app.route("/viewbookings", methods=['GET', 'POST'])
def ViewBookings ():
    return flask.render_template("ViewBookings.html")



@app.route ("/book/<int:year>/<int:month>/<int:day>", methods=['GET', 'POST'])
def BookClassroom (year,month,day):
    today = date.today()
    return flask.render_template("BookClassroom.html", year=year, month=month, day=day)








if __name__ == "__main__":
    app.run(debug=True)

