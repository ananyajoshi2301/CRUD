from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("indexcrud.html");  
 
@app.route("/add")  
def add():  
    return render_template("addcrud.html") 
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            address = request.form["address"]  
            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (name, email, address) values (?,?,?)",(name,email,address))  
                con.commit()  
                msg = "Employee successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("successcrud.html",msg = msg)  
            con.close()  
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Employees")  
    rows = cur.fetchall()  
    return render_template("viewcrud.html",rows = rows)  
 
 
@app.route("/delete")  
def delete():  
    return render_template("deletecrud.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("employee.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Employees where id = ?",id)  
            msg = "Record successfully deleted"  
        except:  
            msg = "Can't be deleted"  
        finally:  
            return render_template("deleterecordcrud.html",msg = msg)  

@app.route("/update")
def update():  
    return render_template("updatecrud.html") 

@app.route("/updaterecord",methods = ["POST", "GET"])
def updaterecord():    
    msg = "msg"
    if request.method == "POST":  
        try:  
            id = request.form["id"]
            name = request.form["name"]  
            email = request.form["email"]  
            address = request.form["address"]  
            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute(" UPDATE Employees set name=?, email=?, address=? where id=?",(name,email,address,id)) 
                con.commit()  
                msg = "Employee successfully updated"  
        except:  
            con.rollback()  
            msg = "We can not update the employee in the list"  
        finally:  
            return render_template("updaterecordcrud.html",msg = msg)  
            con.close()  
  
if __name__ == "__main__":  
    app.run(debug = True) 
