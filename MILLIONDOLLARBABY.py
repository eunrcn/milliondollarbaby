import sys
from time import sleep
import time 


def print_lyrics():
    lines = [
        ("I ain't never rep a set, baby (tsk, tsk)", 0.05),
        ("longpause", 0.2),
        ("I ain't do no wrong", 0.05),
        ("longpause", 0.2),
        ("I could clean up good for you", 0.06),
        ("longpause", 0.22),
        ("Oh, I know right from wrong,", 0.045),
        ("longpause", 0.2),
        ("\u2018Cause I wanna make it, so badly", 0.07),
        ("longpause", 0.6),
        ("I'm a million dollar baby", 0.05),
        ("longpause", 0.6),
        ("Don't at me, yeah, hell nah", 0.1),
        ("longpause", 0.6),
        ("You rep my city for so damn long", 0.08),
        ("longpause", 0.9),
        ("But you still don't notice me, my sound next", 0.06),
        ("longpause", 0.8),
        ("Va next,", 0.07),
        ("longpause", 1.35),
        ("I'm at they neck", 0.06),
        ("longpause", 0.5),
        ("I'm runnin' up a check", 0.05),
        ("longpause", 2),
        ("I see a bad lil' mama, she a diva", 0.06),
        ("longpause", 1.3),
        ("No matter what happens, he cannot come between us again", 0.048),
        ("longpause", 2.6),
        ("I know we're better than friends", 0.04),
        ("longpause", 2.9),
        ("I took her to Queen's Gambit, showed around my friends", 0.06),
        ("longpause", 0.8),
        ("Tried to pick some energy up, it don't matter", 0.045),
        ("longpause", 0.7),
        ("I know you never moved on if you tried", 0.06),
        ("longpause", 1.2),
        ("I don't believe it, baby, I know you lied", 0.04),
        ("longpause", 1.5),
        ("All night long,", 0.06),
        ("longpause", 1.6),
        ("what you mean, 'I changed'?", 0.04),
        ("longpause", 0.2),
        ("Haven't stayed the same", 0.05),
        ("longpause", 0.8),
        ("I've been losin' my mind", 0.07),
        ("longpause", 1.6),
        ("I said, 'The city is mine'", 0.06)
    ]

    for line, char_delay in lines:
        if line == "longpause":
            time.sleep(char_delay)
        else:
            for char in line:
                print(char, end='')
                sys.stdout.flush()
                sleep(char_delay)
            print('')



print_lyrics()
