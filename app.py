#imports
from flask import Flask, render_template, request, redirect, url_for, session, redirect, g, flash
import sqlite3

app = Flask(__name__)

#session key
app.secret_key = "super secret key"

#connect to db
conn = sqlite3.connect('wuyts_maxim.db', check_same_thread=False)
cursor = conn.execute("SELECT * from products")

#login
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session.pop("user", None)
        session["user"] = request.form['username']
        session["color"] = request.form["color"]
        return redirect(url_for("list"))
    try:
        return render_template("index.html", name = g.user)
    except Exception as e:
        return (str(e))
    
#show list if logged in
@app.route('/list')
def list():
    if g.user:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from products")
   
        rows = cur.fetchall()
        if 'visits' in session:
            total_visits = session['visits'] = session.get('visits') + 1 
        else:
            session['visits'] = 1 
            total_visits = session.get('visits')
        try:
            return render_template("list.html",rows = rows, color = g.color, total_visits = total_visits)
        except Exception as e:
            return (str(e))
    return redirect(url_for("index"))

#show product details
@app.route('/list/<string:count>/')
def list_product(count):
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from products where count = " + count)
    row = cur.fetchone()
    try:
        return render_template('list_id.html', row=row, color = g.color)
    except Exception as e:
        return (str(e))

#sessions
@app.before_request
def before_request():
    g.user = ""
    g.color = None
    if "user" in session:
        g.user = session["user"]
    if "color" in session:
        g.color = session["color"]

#delete the session
@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    session.pop('visits', None)
    return 'Dropped!'

#Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html")

if __name__ == "__main__":
    app.run()