#!/usr/bin/python
import sys
from random import randint

n_door = int(sys.argv[1])
n_repetitions = int(sys.argv[2])

'''
    #0 close door
    #1 open door
    #2 chosen door
'''
won = 0
lost = 0

for repetition in range(n_repetitions):
    doors = [0] * n_door
    choosen_door = randint(0, n_door - 1)
    doors[choosen_door] = 2
    selected_door = randint(0, n_door - 1)
    count = 0
    for i in range(0, n_door):
        if i != choosen_door and i != selected_door:
            doors[i] = 1
            count += 1
        if count == len(doors) - 2:
            break
    for i in range(0, n_door - 1):
        if doors[i] == 0:
            choosen_door = i
            doors[choosen_door] = 2
            break

    if choosen_door == selected_door:
        won += 1
    else:
        lost += 1

    if repetition % 100 == 0 and repetition != 0:
        print 'repetition {}; won {}; lost {}; medium {}'.format(
            str(repetition), str(won), str(lost),
            str(float(won)/float(repetition))
        )
