from app import app
from flask import render_template, request, redirect, session
from db import db
import accounts
import game
import hints


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
    result = game.reset_game()
    if result[1] == None:
        return render_template("form.html", answered = result[0])
    else:
        return render_template("formhint.html", answered = result[0], hint = result[1])

@app.route("/play", methods=["POST"])
def play_post():
    answer = request.form["given"]
    result = game.check_answer(answer)
    if result[0] and result[2]!=None:
        return render_template("formhint.html", answered = result[1], hint = result[2])
    elif result[0] and result[2]==None:
        return render_template("form.html", answered = result[1])
    else:
        return render_template("fail.html", correct = result[1], count = str(result[2]))

@app.route("/createhint", methods=["POST"])
def createhint():
    hint = request.form["hint"]
    decimal = request.form["decimal"]
    user_id = accounts.get_user_id(request.form["username"])
    hints.create_hint(user_id, decimal, hint)
    return redirect("/")



@app.route("/pi")
def pi():
    return game.getpi()
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