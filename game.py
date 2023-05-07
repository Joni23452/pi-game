from flask import session, render_template, redirect
import accounts
import hints
import datetime
import scores

index = 0
sofar = "3."
hints_used = 0
hints_dict = {}
user_id = ""
with open("pii.txt") as f:
    pii = str(f.read())

def reset_game():
    global index, sofar, hints_used, hints_dict, user_id
    index = 0
    sofar = "3."
    hints_used = 0
    user_id = accounts.get_user_id(session["username"])
    hints_dict = hints.get_hints(user_id)
    if hint_exists():
        return render_template("formhintavailable.html", answered = sofar)
    else:
        return render_template("form.html", answered = sofar)

def check_answer(answer):
    global index
    correct = str(pii[index])
    return answer==correct

def correct():
    global index, sofar
    sofar += str(pii[index])
    index += 1

def getpi():
    return pii

def index():
    return index

def play(answer):
    global index, sofar, hints_used, user_id, hints_dict
    if answer == "retry":
        if hint_exists():
            return render_template("formhintavailable.html", answered = sofar)
        else:
            return render_template("form.html", answered = sofar)
        
    if check_answer(answer):
        correct()
        if hint_exists():
            return render_template("formhintavailable.html", answered = sofar)
        else:
            return render_template("form.html", answered = sofar)
    else:
        timestamp = datetime.datetime.now()
        scores.add_score(str(user_id), str(index), str(hints_used), str(timestamp))
        if hint_exists():
            return render_template("failhint.html", correct = str(pii[index]), count = str(index), hint=hints.set_hint(hints_dict, index))
        return render_template("fail.html", correct = str(pii[index]), count = str(index))
    
def hint_exists():
    global hints_dict, index
    return hints.set_hint(hints_dict, index) != None

def gamehint():
    global index, sofar, hints_dict, hints_used
    hints_used += 1
    hint = hints.set_hint(hints_dict, index)
    return render_template("formhint.html", answered = sofar, hint = hint)
    
def retry():
    return render_template()