import math
import random

settings = {
    'gamble_per_repeat': 10,
    'repeats':10000,
    'options':[-1,1]
}

results = {
    'no_negative': 0,
    'end_zero': 0,
}

def do_one_repeat():

    #value_history = []
    start_value = 0
    current_value = start_value

    for i in range(settings['gamble_per_repeat']):
        change_val = settings['options'][random.randint(0,1)]
        current_value = current_value + change_val
        if current_value < 0:
            break
        else:
            pass
            #value_history = value_history.append(current_value)
    
    if current_value > 0:
        results['no_negative'] += 1
    if current_value == 0:
        results['no_negative'] += 1
        results['end_zero'] += 1

def exec():
    for i in range(settings['repeats']):
        do_one_repeat()
    
    print(results)

exec()