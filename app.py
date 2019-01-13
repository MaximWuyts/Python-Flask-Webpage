from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

conn = sqlite3.connect('wuyts_maxim.db', check_same_thread=False)
cursor = conn.execute("SELECT * from wuyts_maxim")

for row in cursor:
    print("Brand = ", row[0])
    print("Product Name = ", row[1])
    print("Old Price = ", row[2])
    print("Current Price  = ", row[3])
    print("Total ratings = ", row[4])

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/list')
def list():
   conn.row_factory = sqlite3.Row
   cur = conn.cursor()
   cur.execute("select * from wuyts_maxim")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)
