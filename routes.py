from app import app
from flask import render_template, request, redirect, session, abort
from db import db
import accounts, game, hints, profiles, scores


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

@app.route("/edithint", methods=["POST"])
def edithint():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    newhint = request.form["hint"]
    decimal = request.form["decimal"]
    user_id = accounts.get_user_id(request.form["username"])
    hints.edit_hint(user_id, decimal, newhint)
    return redirect("/")
    
@app.route("/leaderboard")
def leaderboard():
    lb = scores.leaderboard_nohints()
    lb2 = scores.leaderboardalize(lb)

    return render_template("leaderboardglobal.html", leaderboard=lb2)

@app.route("/leaderboard/mostgames")
def leaderboard_mostgames():
    lb = scores.leaderboard_mostgames()
    lb2 =scores.leaderboardalize(lb)

    return render_template("leaderboardgames.html", leaderboard=lb2)

@app.route("/leaderboard/mostplayed")
def leaderboard_mostplayed():
    lb = scores.leaderboard_mostplayed()
    lb2 =scores.leaderboardalize(lb)

    return render_template("leaderboardmostanswers.html", leaderboard=lb2)


@app.route("/profile")
def profile():
    return profiles.create_profile()