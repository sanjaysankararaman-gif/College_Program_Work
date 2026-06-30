import pygame
import random
import time 
import sys
import select

pygame.mixer.init()

def input_available():
    return select.select([sys.stdin], [], [], 0)[0] != []

def case_generator():
    case=random.randint(1,2)
    if case==1:
        return 1
    else:
        return 2

def practice_mode():
    a=True
    while a:
        counter=0
        total=0
        end=True
        while end:
            letter=letter_generator()
            sound=sound_dict[letter]
            case_number=case_generator()
            if case_number==1:
                letter=letter.lower()
            else:
                letter=letter.upper()
            case=case_dict[case_number].play()
            while case.get_busy():
                time.sleep(0.1)
            channel=sound.play()
            while channel.get_busy():
                time.sleep(0.01)
            start=time.time()
            print("Type the letter you heard: ")
            while True:
                elapsed_time=time.time()-start
                if elapsed_time>=8:
                    case=case_dict[case_number].play()
                    while case.get_busy():
                        time.sleep(0.1)
                    channel=sound.play()
                    while channel.get_busy():
                        time.sleep(0.01)
                    start=time.time()

                if input_available():
                    user_input = sys.stdin.readline().strip()
                    if user_input==letter:
                        counter+=1
                        total+=1
                        break
                    elif user_input.lower()=="end":
                        a=False
                        end=False
                        print("Your score is: ", counter, "out of ", total)
                        break
                    else:
                        pygame.mixer.Sound("Try again.wav").play()
                        total+=1
                        continue

def test_mode():
    a=True
    while a:
        counter=0
        total=0
        end=True
        while end:
            letter=letter_generator()
            sound=sound_dict[letter]
            case_number=case_generator()
            if case_number==1:
                letter=letter.lower()
            else:
                letter=letter.upper()
            case=case_dict[case_number].play()
            while case.get_busy():
                time.sleep(0.1)
            channel=sound.play()
            while channel.get_busy():
                time.sleep(0.01)
            start=time.time()
            print("Type the letter you heard: ")
            while True:
                elapsed_time=time.time()-start
                if elapsed_time>=8:
                    case=case_dict[case_number].play()
                    while case.get_busy():
                        time.sleep(0.1)
                    channel=sound.play()
                    while channel.get_busy():
                        time.sleep(0.01)
                    start=time.time()

                if input_available():
                    user_input = sys.stdin.readline().strip()
                    if user_input==letter:
                        counter+=1
                        total+=1
                        break
                    elif user_input.lower()=="end":
                        a=False
                        end=False
                        print("Your score is: ", counter, "out of ", total)
                        break

def letter_generator():
    char=random.randint(97,122)
    return chr(char)

case_dict={1:pygame.mixer.Sound("lower.wav"),
           2:pygame.mixer.Sound("upper.wav")}

sound_dict={"a":pygame.mixer.Sound("a.wav"),
            "b":pygame.mixer.Sound("b.wav"),
            "c":pygame.mixer.Sound("c.wav"),
            "d":pygame.mixer.Sound("d.wav"),
            "e":pygame.mixer.Sound("e.wav"),
            "f":pygame.mixer.Sound("f.wav"),
            "g":pygame.mixer.Sound("g.wav"),
            "h":pygame.mixer.Sound("h.wav"),
            "i":pygame.mixer.Sound("i.wav"),
            "j":pygame.mixer.Sound("j.wav"),
            "k":pygame.mixer.Sound("k.wav"),
            "l":pygame.mixer.Sound("l.wav"),
            "m":pygame.mixer.Sound("m.wav"),
            "n":pygame.mixer.Sound("n.wav"),
            "o":pygame.mixer.Sound("o.wav"),
            "p":pygame.mixer.Sound("p.wav"),
            "q":pygame.mixer.Sound("q.wav"),
            "r":pygame.mixer.Sound("r.wav"),
            "s":pygame.mixer.Sound("s.wav"),
            "t":pygame.mixer.Sound("t.wav"),
            "u":pygame.mixer.Sound("u.wav"),
            "v":pygame.mixer.Sound("v.wav"),
            "w":pygame.mixer.Sound("w.wav"),
            "x":pygame.mixer.Sound("x.wav"),
            "y":pygame.mixer.Sound("y.wav"),
            "z":pygame.mixer.Sound("z.wav")}


print("Select Mode")
print("1. Practice Mode")
print("2. Test Mode")
mode=int(input("Enter 1 or 2: "))

if mode==1:
    practice_mode()
elif mode==2:
    test_mode()