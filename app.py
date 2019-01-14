from flask import Flask, render_template, request, redirect, url_for, session, redirect, g
import sqlite3

app = Flask(__name__)
app.secret_key = "super secret key"

conn = sqlite3.connect('products1.db', check_same_thread=False)
cursor = conn.execute("SELECT * from products1")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session.pop("user", None)
        session["user"] = request.form['username']
        session["color"] = request.form["color"]
        return redirect(url_for("list"))
   
    return render_template("index.html", name = g.user)

#show list if logged in
@app.route('/list')
def list():
    if g.user:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from products1")
   
        rows = cur.fetchall()
        if 'visits' in session:
            total_visits = session['visits'] = session.get('visits') + 1 
        else:
            session['visits'] = 1 
            total_visits = session.get('visits')
        return render_template("list.html",rows = rows, color = g.color, total_visits = total_visits)

    return redirect(url_for("index"))

#show product details
@app.route('/list/<string:count>/')
def list_product(count):
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from products1 where count = " + count)
    row = cur.fetchone()
    return render_template('list_id.html', row=row, color = g.color)


#sessions
@app.before_request
def before_request():
    g.user = ""
    g.color = None
    if "user" in session:
        g.user = session["user"]
    if "color" in session:
        g.color = session["color"]

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'
