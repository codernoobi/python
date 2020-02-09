import pygame

# pygame.mixer.music.load('foo.mp3')
# pygame.mixer.music.play(0)  #play once. -1 play infiniti times

# pygame.mixer.music.queue('next_song.mp3') #queueing songs
# pygame.mixer.music.stop()   #stop song

# #randomly play songs
# _songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3', 'song_5.mp3']
# _currently_playing_song = None

# import random

# def play_a_different_song():
#     global _currently_playing_song, _songs
#     next_song = random.choice(_songs)
#     while next_song == _currently_playing_song:
#         next_song = random.choice(_songs)
#     _currently_playing_song = next_song
#     pygame.mixer.music.load(next_song)
#     pygame.mixer.music.play()

# #same sequence
# def play_next_song():
#     global _songs
#     _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
#     pygame.mixer.music.load(_songs[0])
#     pygame.mixer.music.play()

_sound_library = {}

def play_sound(path):
    global _sound_library
    sound = _sound_library.get(path)
    if sound == None:
        # canonicalized_path = path.replace('/', os.sep).replace('', os.sep)
        sound = pygame.mixer.Sound(path)
        _sound_library[path] = sound
    sound.play()

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            play_sound(r"C:\Users\I353296\Documents\git VS\python\Python\pygame_eg\bird.wav")