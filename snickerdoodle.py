import pygame
from pygame.locals import *
import random
import math
import time
import spotify
import time
import getpass

session = spotify.Session()
loop = spotify.EventLoop(session)
loop.start()
audio = spotify.PortAudioSink(session) #change to AlsaSink for GNU/Linux environment
print 'Please log in to Spotify'
User=raw_input('Username/Email: ')
Pass=getpass.getpass('Password: ')
session.login(User,Pass)
time.sleep(3) #TODO: add detection

print '\nChoose a Playlist:'
for i in range(len(session.playlist_container)):
    if not session.playlist_container[i].name: time.sleep(.1) #TODO: add detection
    print str(i+1)+'. '+session.playlist_container[i].name
print ''
playlist = session.playlist_container[int(raw_input('Playlist number: '))-1]
playlist.load()
tracks = playlist.tracks
raw_input('Start?')

screen_width=1280
screen_height=960
pygame.init()
pygame.display.set_caption(playlist.name)
screen = pygame.display.set_mode((screen_width,screen_height))
font_big = pygame.font.SysFont("menlo", 100)
font_small = pygame.font.SysFont("menlo", 20)
screen.fill((255,255,255))
pygame.display.update()

running=True
playing=True
start=0
num=0

while playing:
    for event in pygame.event.get():
        if event.type == QUIT: playing = False
    if running and time.time()-start >= 60:
        start=time.time()
        num+=1
        track = tracks[num-1]
        print str(num)+'. '+str(track.name)
        session.player.load(track)
        session.player.play()
        screen.fill((255,255,255))
        screen.blit(font_big.render(str(num), 1, (0,0,0)), (screen_width/2-25,screen_height/2-100))
        screen.blit(font_small.render(str(track.name), 1, (0,0,0)), (screen_width/2-5*len(str(track.name)),screen_height/2+40))
        screen.blit(font_small.render(str(track.artists[0].name), 1, (0,0,0)), (screen_width/2-5*len(str(track.artists[0].name)),screen_height/2+80))
        pygame.display.update()
        if num==60: running=False
    time.sleep(.1) #event handling slows everything down
