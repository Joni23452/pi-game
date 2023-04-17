index = 0
sofar = "3."
with open("pii.txt") as f:
    pii = str(f.read())

def reset_game():
    global index, sofar
    index = 0
    sofar = "3."
    hints_used = 0
    return sofar

def check_answer(answer):
    global index, sofar
    correct = str(pii[index])
    if answer == correct:
        index += 1
        sofar += correct
        result = (True, sofar)
        return result
    else:
        result = (False, correct, index)
        return result

def correct():
    global index, sofar
    index += 1
    sofar += str(correct)