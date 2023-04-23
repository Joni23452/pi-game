from flask import session
import accounts
import hints

index = 0
sofar = "3."
hints_used = 0
hints_dict = {}
with open("pii.txt") as f:
    pii = str(f.read())

def reset_game():
    global index, sofar, hints_used, hints_dict
    index = 0
    sofar = "3."
    hints_used = 0
    user_id = accounts.get_user_id(session["username"])
    hints_dict = hints.get_hints(user_id)
    hint = hints.set_hint(hints_dict, index)
    
    return (sofar, hint)

def check_answer(answer):
    global index, sofar, hints_dict
    correct = str(pii[index])
    if answer == correct:
        index += 1
        sofar += correct
        hint = hints.set_hint(hints_dict, index)
        result = (True, sofar, hint)
        return result
    else:
        result = (False, correct, index)
        return result

def correct():
    global index, sofar
    index += 1
    sofar += str(correct)

def getpi():
    return pii

def index():
    return index