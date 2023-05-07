from app import app
from flask import render_template, request, redirect, session, abort
from db import db
import accounts
import game
import hints
import profiles
import scores
import secrets


@app.route("/")
def mainpage():
    return render_template("page.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login",methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]
    if len(username)>16 or len(username)<1 or len(password)<6 or len(password)>99:
        return render_template("loginerror.html")
    return accounts.login_or_create(username, password)

@app.route("/logout")
def logout():
    del session["username"]
    del session["csrf_token"]
    return redirect("/")

@app.route("/play")
def play():
    if not session.get("username"):
        return redirect("/login")
    return game.reset_game()

@app.route("/play", methods=["POST"])
def play_post():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

    if request.form["hint_requested"] == "True":
        if game.hint_exists():
            return game.gamehint()
        
    answer = request.form["given"]
    if len(answer)!=1:
        return game.play("retry")
    return game.play(answer)

@app.route("/createhint", methods=["POST"])
def createhint():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    hint = request.form["hint"]
    decimal = request.form["decimal"]
    user_id = accounts.get_user_id(request.form["username"])
    hints.create_hint(user_id, decimal, hint)
    return redirect("/")

@app.route("/leaderboard")
def leaderboard():
    lb = scores.leaderboard_nohints()
    lb2 = scores.leaderboardalize(lb)

    return render_template("leaderboardglobal.html", leaderboard=lb2)

@app.route("/profile")
def profile():
    return profiles.create_profile()

@app.route("/history")
def history():
    return "history"

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