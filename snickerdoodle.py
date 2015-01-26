import spotify
import time
import getpass
session = spotify.Session()
loop = spotify.EventLoop(session)
loop.start()
audio = spotify.PortAudioSink(session)
User=raw_input('Username: ')
Pass=getpass.getpass('Password: ')
session.login(User,Pass)
time.sleep(3) #TODO: add detection
start=0
running=True
num=0
print '\nChoose a Playlist:'
for i in range(len(session.playlist_container)):
    print str(i+1)+'. '+session.playlist_container[i].name
print ''
playlist = session.playlist_container[int(raw_input('Playlist number: '))-1]
playlist.load()
tracks = playlist.tracks
track = tracks[0]
session.player.load(track)
dummy=raw_input('Start?')
while running:
    if time.time()-start >= 60:
        num=num+1
        start=time.time()
        print str(num)+'. '+str(track.name)
        session.player.load(track)
        session.player.play()
        track = tracks[num]
        if num==60: running=False
