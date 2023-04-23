from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


def user_exists(username):
    usernametuple = (username,)
    users = db.session.execute(text("SELECT username FROM users")).fetchall()
    return usernametuple in users

def check_password(username, password):
    sql=text("SELECT password FROM users WHERE username=:username")
    hash_value=str(db.session.execute(sql, {"username":username}).fetchone()[0])
    return check_password_hash(hash_value, password)

def create_account(username, password):
    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users (username, password, admin) VALUES (:username, :password, False)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()
    return 

def get_user_id(username):
    sql = text("SELECT id FROM users WHERE username=:username")
    return db.session.execute(sql, {"username":username}).fetchone()[0]