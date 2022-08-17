from tkinter import *
import pygame
from pygame.locals import *
import os
from os import path
import librosa
import librosa.display
import IPython.display
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
from IPython.display import Audio
import sounddevice
from scipy.io.wavfile import write
from playsound import playsound
import scipy as sp
from IPython.display import display
from scipy import signal
from scipy.io import wavfile
import noisereduce as nr
import subprocess
os.getcwd()
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.
root = Tk() 
class MusicPlayer(object):
    def __init__(self,root):
        self.root = root
        # Title of the window
        self.root.title("Nour & Hla's Music Player")
        # Window Geometry
        self.root.geometry("1000x250+250+250")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()

        # Creating the Track Frames for Song label & status label
        trackframe = LabelFrame(self.root,text="Song Track",font=("Helvetica",14,"bold"),bg="#1f7a8c",fg="white",bd=5,relief=RAISED)
        trackframe.place(x=0,y=0,width=600,height=80)
        # Inserting Song Track Label
        songtrack = Label(trackframe,textvariable=self.track,width=30,font=("Helvetica",15,"bold"),bg="#053c5e",fg="white").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("Helvetica",14,"bold"),bg="#a31621",fg="white").grid(row=0,column=1,padx=10,pady=5)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root,text="Control Panel",font=("Helvetica",14,"bold"),bg="#053c5e",fg="white",bd=5,relief=RAISED)
        buttonframe.place(x=0,y=80,width=600,height=170)
        # Inserting Play Button
        playbtn = Button(buttonframe,text="Play",command=self.playsong,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#1f7a8c").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Pause Button
        playbtn = Button(buttonframe,text="Pause",command=self.pausesong,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#1f7a8c").grid(row=0,column=1,padx=10,pady=5)
        # Inserting Stop Button
        playbtn = Button(buttonframe,text="Stop",command=self.stopsong,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#1f7a8c").grid(row=0,column=2,padx=10,pady=5)
        # Inserting Fast Button
        playbtn = Button(buttonframe,text="Fast",command=self.fast,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#1f7a8c").grid(row=0,column=3,padx=10,pady=5)
        # Inserting Slow Button
        playbtn = Button(buttonframe,text="Slow",command=self.slow,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#1f7a8c").grid(row=1,column=0,padx=10,pady=5)
        # Inserting Pitch Shift Down Button
        playbtn = Button(buttonframe,text="Pitch Down",command=self.pitchshiftdown,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#1f7a8c").grid(row=1,column=2,padx=10,pady=5)
        # Inserting Pitch Shift Up Button
        playbtn = Button(buttonframe,text="Pitch Up",command=self.pitchshiftup,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#1f7a8c").grid(row=1,column=1,padx=10,pady=5)
        # Inserting Remix Button
        playbtn = Button(buttonframe,text="Remix",command=self.remix,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#1f7a8c").grid(row=1,column=3,padx=10,pady=5)
        # Inserting Record Button
        playbtn = Button(buttonframe,text="Record Audio",command=self.recordaudio,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#a31621").grid(row=2,column=0,padx=10,pady=5)
        # Inserting Noise Reduction Button
        playbtn = Button(buttonframe,text="Noise Reduction",command=self.noisereduction,width=13,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#a31621").grid(row=2,column=2,padx=10,pady=5)
        # Inserting Trim Button
        playbtn = Button(buttonframe,text="Trim Silence",command=self.trimsilence,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#a31621").grid(row=2,column=3,padx=10,pady=5)
        # Inserting Play Record Button 
        playbtn = Button(buttonframe,text="Play Record",command=self.playrecord,width=10,height=1,font=("Helvetica",12,"bold"),fg="white",bg="#a31621").grid(row=2,column=1,padx=10,pady=5)

        # Creating Playlist Frame
        songsframe = LabelFrame(self.root,text="Song Playlist",font=("Helvetica",14,"bold"),bg="#1f7a8c",fg="white",bd=5,relief=RAISED)
        songsframe.place(x=600,y=0,width=400,height=250)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="#BD1120",selectmode=SINGLE,font=("Helvetica",12,"bold"),bg="#053c5e",fg="white",bd=5,relief=RAISED)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("C:/Users/Hla Dawoud/Desktop/Python Project")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
         self.playlist.insert(END,track)
        
    def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        #sound = pygame.mixer.Sound(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()
        #sound.play()
        
    def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()
        #sound = pygame.mixer.Sound(self.playlist.get(ACTIVE))
        #sound.stop()
        
    def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()
        #sound = pygame.mixer.Sound(self.playlist.get(ACTIVE))
        #sound.pause()
        
    def fast(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Speeding Up")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        y, sr = librosa.load(self.playlist.get(ACTIVE))
        y_fast = librosa.effects.time_stretch(y, rate=0.5)
        wave_audio = np.sin(y_fast)
        Audio(wave_audio, rate=20000)
        import soundfile as sf
        sf.write('wave_audio.wav',wave_audio,48000)
        # Playing Selected Song
        file = "wave_audio.wav"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()      
        
    def slow(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Slowing Down")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        y, sr = librosa.load(self.playlist.get(ACTIVE))
        y_slow = librosa.effects.time_stretch(y, rate=0.2)
        wave_audio1 = np.sin(y_slow)
        Audio(wave_audio1, rate=20000)
        import soundfile as sf
        sf.write('wave_audio1.wav',wave_audio1,48000)
        # Playing Selected Song
        file = "wave_audio1.wav"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play() 
        
    def pitchshiftdown(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Pitch Down")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        y, sr = librosa.load(self.playlist.get(ACTIVE))
        #pitch shift by -10, 10 octaves down (frequency and pitch decrease)
        y_tritone = librosa.effects.pitch_shift(y, sr=sr, n_steps=-10)
        wave_audio2 = np.sin(y_tritone)
        Audio(wave_audio2, rate=20000)
        import soundfile as sf
        sf.write('wave_audio2.wav',wave_audio2,48000)
        # Playing Selected Song
        file = "wave_audio2.wav"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play() 
        
    def pitchshiftup(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Pitch Up")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        y, sr = librosa.load(self.playlist.get(ACTIVE))
        #pitch shift by 10, 10 octaves up (frequency and pitch increase)
        y_third = librosa.effects.pitch_shift(y, sr=sr, n_steps=10)
        wave_audio3 = np.sin(y_third)
        Audio(wave_audio3, rate=20000)
        import soundfile as sf
        sf.write('wave_audio3.wav',wave_audio3,48000)
        # Playing Selected Song
        file = "wave_audio3.wav"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play() 
        
    def remix(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Remix")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        y, sr = librosa.load(self.playlist.get(ACTIVE))
        #compute beats
        _, beat_frames = librosa.beat.beat_track(y=y, sr=sr,
                                                 hop_length=512)
        #convert from frames to sample indices
        beat_samples = librosa.frames_to_samples(beat_frames)

        #generate intervals from consecutive events
        intervals = librosa.util.frame(beat_samples, frame_length=2,
                                       hop_length=1).T

        #reverse the beat intervals
        y_out = librosa.effects.remix(y, intervals[::-2])
        wave_audio4 = np.sin(y_out)
        Audio(wave_audio4, rate=20000)
        import soundfile as sf
        sf.write('wave_audio4.wav',wave_audio4,48000)
        # Playing Selected Song
        file = "wave_audio4.wav"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play() 
        
    def recordaudio(self):
        # Displaying Status
        self.status.set("-Recording Done")
        #44100 or 48000 is used frequently in CDs and computer audio , there are other more commom frequency samples
        fs = 44100
        #duration of record
        second = 15
        #sounddevice.rec records an audio and save it in a form of numpy array
        record_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
        sounddevice.wait()
        #write(filnename,rate,data) which converts a numpy array into a wav file
        write('record.wav',fs,record_voice)
        write('record.mp3',fs,record_voice)
        # Displaying Selected Song title
        self.track.set("record.wav")

        
    def playrecord(self):
        # Displaying Status
        self.status.set("-Playing Record")
        # Displaying Selected Song title
        self.track.set("record.mp3")
        # Loading Selected Song
        file = "record.mp3"
        sound = pygame.mixer.Sound(file)
        sound.play()
    
    def noisereduction(self):
        # Displaying Status
        self.status.set("-Noise Reducing")
        #loading the pre-recorded WAV file
        filename = ('record.wav')
        y0, sr0 = librosa.load(filename)
        #reduce noise by median
        def reduce_noise_median(y, sr):
            y = sp.signal.medfilt(y,3)
            return (y)
        wavfile.write("mywav_reduced_noise1.wav", sr0, reduce_noise_median(y0, sr0))
        #loading the 1st noise reduced WAV file
        filename = ('mywav_reduced_noise1.wav')
        y1, sr1 = librosa.load(filename)
        #perform 2nd noise reduction by noisereduce
        #reduced_noise = nr.reduce_noise(y=y1, sr=sr1, thresh_n_mult_nonstationary=2,stationary=False)
        #noise_reduced = nr.reduce_noise(y=y1, sr=sr1, prop_decrease=0, stationary=False)
        reduced_noise = nr.reduce_noise(
            y=y1,
            sr=sr1,
            thresh_n_mult_nonstationary=2,
            stationary=False,
            n_jobs=2,
        )
        wavfile.write("mywav_reduced_noise2.wav", sr1, reduced_noise)
        write("mywav_reduced_noise2.mp3",sr1,reduced_noise)
        #loading the final noise reduced WAV file
        file = "mywav_reduced_noise2.mp3"
        sound = pygame.mixer.Sound(file)
        sound.set_volume(1.0)
        sound.play()
        
    def trimsilence(self):
        # Displaying Status
        self.status.set("-Trimming Silence")
        #loading the WAV file
        filename = ('mywav_reduced_noise2.wav')
        y2, sr2 = librosa.load(filename)
        #trim the beginning and ending silence
        yt, index = librosa.effects.trim(y2)
        from IPython.display import Audio
        wave_audio_trim = np.sin(yt)
        Audio(wave_audio_trim, rate=20000)
        import soundfile as sf
        wavfile.write('wave_audio_trim.wav',sr2,wave_audio_trim)
        #write("wave_audio_trim.mp3",sr2,wave_audio_trim)
        # Playing Selected Song
        file = "wave_audio_trim.wav"
        sound = pygame.mixer.Sound(file)
        sound.set_volume(1.0)
        sound.play()
        
# Passing Root to MusicPlayer Class
MusicPlayer(root)

root.mainloop()
#%%

