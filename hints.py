from db import db
from sqlalchemy.sql import text

def check_content(content):
    return len(content)<=20

def create_hint(user_id, decimal, content):
    #TODO check if hint exists already
    if check_content(content):
        sql = text("INSERT INTO hints (owner_id, decimal, content) VALUES (:user_id, :decimal, :content)")
        db.session.execute(sql, {"user_id":user_id, "decimal":decimal, "content":content})
        db.session.commit()
        return True
    else:
        return False

def get_hint(user_id, decimal):
    sql = text("SELECT content FROM hints WHERE owner_id=:user_id, decimal=:decimal")
    hint = db.session.execute(sql, {"user_id":user_id, "decimal":decimal}).fetchone()[0]
    return hint

def get_hints(user_id):
    sql = text("SELECT decimal, content FROM hints WHERE owner_id=:user_id")
    hints = db.session.execute(sql, {"user_id":user_id}).fetchall()
    dict={}
    for decimal, hint in hints:
        dict.setdefault(decimal,[]).append(hint) #https://www.geeksforgeeks.org/python-convert-a-list-of-tuples-into-dictionary/
    return dict

def set_hint(hints_dict, decimal):
    try:
        hint = hints_dict[decimal][0]
    except:
        hint = None
    return hint