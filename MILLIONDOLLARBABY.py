import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("I ain't never rep a set, baby (tsk, tsk)", 0.06),
        ("I ain't do no wrong", 0.05),
        ("I could clean up good for you", 0.065),
        ("Oh, I know right from wrong,", 0.05),
        ("\u2018Cause I want make it, so badly", 0.09),
        ("I'm a million dollar baby", 0.07),
        ("Don't at me, yeah, hell nah", 0.11)
    ]

    delays = [0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.1]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
