from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('products1.db', check_same_thread=False)
cursor = conn.execute("SELECT * from products1")

@app.route("/")
def index():
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from products1")

    rows = cur.fetchall()
    return render_template("index.html",rows = rows)

@app.route('/list')
def list():
   conn.row_factory = sqlite3.Row
   cur = conn.cursor()
   cur.execute("select * from products1")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

@app.route('/list/<string:count>/')
def list_product(count):
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from products1 where count = " + "count")
    row = cur.fetchone()
    print(row)
    return render_template('list_id.html', row=row)

