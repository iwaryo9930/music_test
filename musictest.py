import pygame
import RPi.GPIO as GPIO
from time import sleep
import glob



def my_callback(channel):
    global btnState
    global pauseState
    global song_index
    global passlist
    if channel==27 and pauseState%2==0:
        btnState = not btnState
        if btnState==GPIO.HIGH:
           pygame.mixer.music.unpause()
           pauseState = pauseState+1
    elif channel==27:
        btnState = not btnState
        if btnState==GPIO.HIGH:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(passlist[song_index])
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.pause()
            pauseState = pauseState+1
            

def next_music():
    global passlist
    global song_index
    while True:
        try:
            for event in pygame.event.get():
                if event.type == MUSIC_ENDED:
                    song_index += 1
                    pygame.mixer.music.load(passlist[song_index])
                    pygame.mixer.music.play()
    
            
next_music()
#try:
    #while True:
        #sleep(0.01)

thread_001 = threading.Thread(target=nextmusic)
thread_001.start()

            
