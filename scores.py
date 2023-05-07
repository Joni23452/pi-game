from db import db
from sqlalchemy.sql import text

def add_score(user_id, score, hints_used, timestamp):
    sql = text("INSERT INTO scores (owner_id, score, hints, timestamp) VALUES (:user_id, :score, :hints_used, :timestamp)")
    db.session.execute(sql, {"user_id":user_id, "score":score, "hints_used":hints_used, "timestamp":timestamp})
    db.session.commit()

def scores_of_user(user_id):
    sql = text("SELECT score, timestamp FROM scores WHERE owner_id=:user_id ORDER BY timestamp DESC")
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def max_score_nohints(user_id):
    sql = text("SELECT MAX(score) FROM scores WHERE owner_id=:user_id, hints=0")
    return db.session.execute(sql, {"user_id":user_id}).fetchone()[0]

def leaderboard_nohints():
    sql = text("SELECT users.username, MAX(scores.score) FROM users, scores WHERE users.user_id=scores.owner_id, hints=0 ORDER BY MAX(scores.score) DESC")
    return db.session.execute(sql)