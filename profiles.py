import scores
import accounts
from flask import session, render_template

def create_profile():
    user_id = accounts.get_user_id(session["username"])
    max_score = str(scores.max_score_nohints(user_id))
    total_played = str(scores.total_games(user_id))
    return render_template("profile.html", max=max_score, total=total_played)

