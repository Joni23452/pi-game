from db import db
from sqlalchemy.sql import text

def add_score(user_id, score, hints_used, timestamp):
    sql = text("INSERT INTO scores (owner_id, score, hints, timestamp) VALUES (:user_id, :score, :hints_used, :timestamp)")
    db.session.execute(sql, {"user_id":user_id, "score":score, "hints_used":hints_used, "timestamp":timestamp})
    db.session.commit()

def scores_of_user(user_id):
    sql = text("SELECT score, hints, timestamp FROM scores WHERE owner_id=:user_id ORDER BY timestamp DESC")
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def max_score_nohints(user_id):
    sql = text("SELECT MAX(score) FROM scores WHERE owner_id=:user_id AND hints=0")
    return db.session.execute(sql, {"user_id":user_id}).fetchone()[0]

def total_answered(user_id):
    sql = text("SELECT SUM(score) FROM scores WHERE owner_id=:user_id")
    return db.session.execute(sql, {"user_id":user_id}).fetchone()[0]

def leaderboard_nohints():
    sql = text("SELECT users.username, MAX(scores.score) FROM users, scores WHERE users.id=scores.owner_id AND hints=0 GROUP BY users.username ORDER BY MAX(scores.score) DESC")
    return db.session.execute(sql).fetchall()

def leaderboard_mostgames():
    sql = text("SELECT users.username, COUNT(scores.score) FROM users, scores WHERE users.id=scores.owner_id GROUP BY users.username ORDER BY COUNT(scores.score) DESC")
    return db.session.execute(sql).fetchall()

def leaderboard_mostplayed():
    sql = text("SELECT users.username, SUM(scores.score) FROM users, scores WHERE users.id=scores.owner_id GROUP BY users.username ORDER BY SUM(scores.score) DESC")
    return db.session.execute(sql).fetchall()

def total_games(user_id):
    sql = text("SELECT COUNT(score) FROM scores WHERE owner_id=:user_id")
    return db.session.execute(sql, {"user_id":user_id}).fetchone()[0]

def leaderboardalize(leaderboard):
    lb = []
    counter=1
    for i in leaderboard:
        lb.append((counter, i[0], i[1]))
        counter+=1
    return lb