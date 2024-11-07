# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play="", opponent_history=[], name_history=[], my_history=[], play_order=[{"RR":0, "RP":0, "RS":0, "PP":0, "PR":0, "PS":0, "SS":0, "SR":0, "SP":0}]):
    opponent_history.append(prev_play)

    guess = "R"
    iteriate = len(opponent_history)
    ideal_responce = {'P': 'S', 'R': 'P', 'S': 'R'}

    #Here we will reset the count after 1000 iteriations 

    if iteriate == 1001:
        opponent_history.clear()
        opponent_history.append(prev_play)
        name_history.clear()
        name_history.append('')
        my_history.clear()

    #Lets find who we are playing in the first 3 iterations 

    if iteriate <= 4:

        if iteriate == 1:
            my_history.append("R")
            return "R"
        elif iteriate == 2:
            my_history.append("P")
            return "P"
        elif iteriate == 3:
            my_history.append("S")
            return "S"
        else:
            if len(opponent_history) >= 3:
                opponent_code = "".join(opponent_history[-3:])
                code_to_bot = {"RPP":"quincy", "PPP":"abbey", "PPS":"kris", "RRR":"mrugesh"}
                opponent = code_to_bot.get(opponent_code, "unknown") # here unknown handels a possible key error
                name_history.append(opponent)
        

    if name_history:
        opponen_type = name_history[-1] # here we check that we have atleast one record in the list before checking name_history

        if name_history[-1]== 'quincy':
            choices = ["R","R","P","P","S"]
            next_move = choices[iteriate % len(choices)]
            guess = ideal_responce[next_move]

        elif name_history[-1]=='abbey':
            if len(my_history) >= 2:
                last_two = "".join(my_history[-2:])
                if len(last_two) == 2:
                    play_order[0][last_two] += 1

            
                potential_plays = [
                    my_history[-1] + "R",
                    my_history[-1] + "P",
                    my_history[-1] + "S",

                ]

                sub_order = {
                    k : play_order[0][k]
                    for k in potential_plays if k in play_order[0]
                }

                prediction = max(sub_order, key=sub_order.get)[-1:]

                next_move = ideal_responce[prediction]
                guess = ideal_responce[next_move]

        elif name_history[-1] == 'kris':
            if my_history:
                next_move = ideal_responce[my_history[-1]]
                guess = ideal_responce[next_move]

        elif name_history[-1] == 'mrugesh':
            if len(my_history) >= 10: # we are checking that there is atleast 10 items in the list 
                last_ten = my_history[-10:]
                most_frequent = max(set(last_ten), key=last_ten.count)

            else: 
                most_frequent = "S"

            ideal_responce = {'P': 'S', 'R': 'P', 'S': 'R'}
            next_move = ideal_responce[most_frequent]
            guess = ideal_responce[next_move]

    my_history.append(guess)
    return guess


