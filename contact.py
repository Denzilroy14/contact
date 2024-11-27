'''                                         Project-3
Name:Contact Book
Author:Denzil Roy.I
@copyright reserved by Denzil Roy.I

About:A contact book that can save contact of persons with their name and mobile numbers.
'''
from flask import*
import os
import sqlite3
app=Flask(__name__)
PERSISTENT_DIR='/persistent'
if not os.path.exists(PERSISTENT_DIR):
    os.makedirs(PERSISTENT_DIR)
DATABASE_PATH=os.path.join(PERSISTENT_DIR,'contact.db')
def init_db():
    con=sqlite3.connect(DATABASE_PATH)
    con.row_factory=sqlite3.Row
    return con
def get_db():
    if not os.path.exists(DATABASE_PATH):
        con=sqlite3.connect(DATABASE_PATH)
        con.execute('CREATE TABLE IF NOT EXISTS contactlist(name TEXT,contact TEXT)')
        con.commit()
get_db()
@app.route('/')
@app.route('/home')
def index():
    return render_template('welcomepage.html')
@app.route('/entry',methods=['GET','POST'])
def entry():
    if request.method=='POST':
        name=request.form['name']
        contact=request.form['contact']
        con=init_db()
        con.execute('INSERT INTO contactlist(name,contact)VALUES(?,?)',(name,contact))
        con.commit()
        return render_template('welcomepage.html')
    else:
        return render_template('contact.html')
@app.route('/view')
def viewing():
    con=init_db()
    datas=con.execute('SELECT * FROM contactlist').fetchall()
    return render_template('viewpage.html',values=datas)
if __name__=='__main__':
    app.run(debug=True)






    