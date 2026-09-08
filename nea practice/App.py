import flask
import database
app = flask.Flask(__name__)
@app.route('/')
def index():
    return flask.redirect(flask.url_for("signup"))






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




#this is the flask route i made for the dashboard page, which is necessary as it needs to be rendered here for the functions to work
@app.route("/dashboard", methods=['GET', 'POST'])
def Dashboard ():
    return flask.render_template("Dashboard.html")





@app.route("/calendar", methods=['GET', 'POST'])
def Calendar ():
    return flask.render_template("Calendar.html")





@app.route("/viewbookings", methods=['GET', 'POST'])
def ViewBookings ():
    return flask.render_template("ViewBookings.html")













if __name__ == "__main__":
    app.run(debug=True)

