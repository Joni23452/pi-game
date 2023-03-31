from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"
db = SQLAlchemy(app)
index = 0
sofar = "3."


@app.route("/")
def mainpage():
    return render_template("page.html")


@app.route("/play")
def play():
    global index, sofar
    index = 0
    sofar = "3."
    return render_template("form.html", answered = sofar)

@app.route("/play", methods=["POST"])
def play_post():
    global index, sofar
    index += 1
    answer = request.form["given"]
    correct = str(db.session.execute(text("SELECT digit FROM pi WHERE id = (:index)"), {"index":index}).fetchone()[0])
    if answer == correct:
        sofar += str(correct)
        return render_template("form.html", answered = sofar)
    else:
        fail = f"You failed. The correct digit was {correct}. You got {index-1} correct."
        return fail


@app.route("/pi")
def pi():
    digits = db.session.execute(text("SELECT digit FROM pi")).fetchall()
    content = "3."
    for i in digits:
        content += str(i[0])
    
    return content
        

with open("pii.txt") as f:
    pii = str(f.read())


@app.route("/setpi")
def setpi():
    
    db.session.execute(text("DROP TABLE IF EXISTS pi;"))
    db.session.execute(text("CREATE TABLE pi (id SERIAL PRIMARY KEY, digit INT);"))
    for i in pii:
        sql = text("INSERT INTO pi (digit) VALUES (:i)")
        db.session.execute(sql, {"i":str(i)})
    db.session.commit()
    return "ok"