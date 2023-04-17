from app import app
from flask import render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from sqlalchemy.sql import text
import accounts

index = 0
sofar = "3."
with open("pii.txt") as f:
    pii = str(f.read())

@app.route("/")
def mainpage():
    return render_template("page.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if accounts.user_exists(username):
        if accounts.check_password(username, password):
            session["username"] = username
        else:
            return render_template("wrongpassword.html")
    else:
        accounts.create_account(username, password)
        session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/play")
def play():
    global index, sofar
    index = 1
    sofar = "3."
    hints = 0
    return render_template("form.html", answered = sofar)

@app.route("/play", methods=["POST"])
def play_post():
    global index, sofar
    answer = request.form["given"]
    correct = str(pii[index-1])
    #correct = str(db.session.execute(text("SELECT digit FROM pi WHERE id = (:index)"), {"index":index}).fetchone()[0])
    if answer == correct:
        index += 1
        sofar += str(correct)
        return render_template("form.html", answered = sofar)
    else:
        return render_template("fail.html", correct = correct, count = str(index-1))


@app.route("/pi")
def pi():
    return pii
    #TODO make template
    digits = db.session.execute(text("SELECT digit FROM pi")).fetchall()
    content = "3."
    for i in digits:
        content += str(i[0])
    
    return content
        



#@app.route("/setpi")
def setpi():
    
    db.session.execute(text("DROP TABLE IF EXISTS pi;"))
    db.session.execute(text("CREATE TABLE pi (id SERIAL PRIMARY KEY, digit INT);"))
    for i in pii:
        sql = text("INSERT INTO pi (digit) VALUES (:i)")
        db.session.execute(sql, {"i":str(i)})
    db.session.commit()
    return "ok"