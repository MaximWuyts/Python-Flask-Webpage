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
        return redirect(url_for("list"))
    naam = g.user
    return render_template("index.html", naam = naam)

@app.route('/list')
def list():
    if g.user:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from products1")
   
        rows = cur.fetchall()
        return render_template("list.html",rows = rows)

    return redirect(url_for("index"))
   
@app.before_request
def before_request():
    g.user = ""
    if "user" in session:
        g.user = session["user"]

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'

@app.route('/list/<string:count>/')
def list_product(count):
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from products1 where count = " + count)
    row = cur.fetchone()
    print(row)
    return render_template('list_id.html', row=row)

@app.route("/visits")
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return "Total visits: {}".format(session.get('visits'))