#pitch shift by -5, 5 octaves down (frequency and pitch decrease)
def pitchshiftdown():
    #main packages
    import librosa
    import librosa.display
    import IPython.display
    import numpy as np
    import matplotlib.pyplot as plt
    from IPython.display import display

    #loading the WAV file
    filename = librosa.example('nutcracker')
    y, sr = librosa.load(filename)
    
    #printing the waveform and the sampling rate
    print('waveform')
    print(y)
    print('\nsampling rate')
    print(sr)
    
    #ploting the original wave
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y, sr=sr)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
    
    #play the audio as an array
    display(IPython.display.Audio(data=y, rate=sr))
    
    #pitch shift by -5, 5 octaves down (frequency and pitch decrease)
    y_tritone = librosa.effects.pitch_shift(y, sr=sr, n_steps=-5)
    
    #play the shifted audio
    from IPython.display import Audio
    wave_audio1 = np.sin(y_tritone)
    display(Audio(wave_audio1, rate=20000))
    
    #save 1st shifted audio as a WAV file
    import soundfile as sf
    sf.write('wave_audio1.wav',wave_audio1,48000)
    
    #loading 1st the shifted WAV file
    filename = ('wave_audio1.wav')
    y1, sr1 = librosa.load(filename)
    
    #printing the Waveform, and Sampling Rate
    print('waveform')
    print(y1)
    print('\nsampling rate')
    print(sr1)
    
    #plot the audio's wave
    import librosa.display
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y1, sr=sr1)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
#%%
pitchshiftdown()
#%%
#pitch shift by 5, 5 octaves up (frequency and pitch increase)
def pitchshiftup():
     #main packages
    import librosa
    import librosa.display
    import IPython.display
    import numpy as np
    import matplotlib.pyplot as plt
    from IPython.display import display

    #loading the WAV file
    filename = librosa.example('nutcracker')
    y, sr = librosa.load(filename)
    
    #printing the waveform and the sampling rate
    print('waveform')
    print(y)
    print('\nsampling rate')
    print(sr)
    
    #ploting the original wave
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y, sr=sr)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
    
    #play the audio as an array
    display(IPython.display.Audio(data=y, rate=sr))
    
    #pitch shift by 5, 5 octaves up (frequency and pitch increase)
    y_third = librosa.effects.pitch_shift(y, sr=sr, n_steps=5)
    
    #play the 2nd shifted audio
    from IPython.display import Audio
    wave_audio2 = np.sin(y_third)
    display(Audio(wave_audio2, rate=20000))
    
    #save 2nd shifted audio as a WAV file
    import soundfile as sf
    sf.write('wave_audio2.wav',wave_audio2,48000)
    
    #loading 2nd the shifted WAV file
    filename = ('wave_audio2.wav')
    y2, sr2 = librosa.load(filename)
    
    #printing the Waveform, and Sampling Rate
    print('waveform')
    print(y2)
    print('\nsampling rate')
    print(sr2)
    
    #plot the audio's wave
    import librosa.display
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y2, sr=sr2)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
#%%
pitchshiftup()
#%%
#play the sped-up audio (compresses the pre-recorded audio to be twice as fast)
def fast():
    #main packages
    import librosa
    import librosa.display
    import IPython.display
    import numpy as np
    import matplotlib.pyplot as plt
    from IPython.display import display

    #loading the WAV file
    filename = ("PinkPanther30.wav")
    #filename = librosa.example('nutcracker')
    y, sr = librosa.load(filename)
    
    #printing the waveform and the sampling rate
    print('waveform')
    print(y)
    print('\nsampling rate')
    print(sr)
    
    #ploting the original wave
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y, sr=sr)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
    
    #play the audio as an array
    display(IPython.display.Audio(data=y, rate=sr))
    
    y_fast = librosa.effects.time_stretch(y, rate=2.0)
    
    from IPython.display import Audio
    wave_audio3 = np.sin(y_fast)
    display(Audio(wave_audio3, rate=20000))
    
    #save the sped-up audio as a WAV file
    import soundfile as sf
    sf.write('wave_audio3.wav',wave_audio3,48000)
    
    #loading the sped-up audio WAV file
    filename = ('wave_audio3.wav')
    y3, sr3 = librosa.load(filename)
    
    #plot the audio's wave
    import librosa.display
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y3, sr=sr3)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
#%%
fast()
#%%
#play the slowed-down audio (compresses the pre-recorded audio to half the original speed)
def slow():
     #main packages
    import librosa
    import librosa.display
    import IPython.display
    import numpy as np
    import matplotlib.pyplot as plt
    from IPython.display import display

    #loading the WAV file
    filename = librosa.example('nutcracker')
    y, sr = librosa.load(filename)
    
    #printing the waveform and the sampling rate
    print('waveform')
    print(y)
    print('\nsampling rate')
    print(sr)
    
    #ploting the original wave
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y, sr=sr)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
    
    #play the audio as an array
    display(IPython.display.Audio(data=y, rate=sr))
    
    y_slow = librosa.effects.time_stretch(y, rate=0.5)
    
    from IPython.display import Audio
    wave_audio4 = np.sin(y_slow)
    display(Audio(wave_audio4, rate=20000))
    
    #save the slowed-down audio as a WAV file
    import soundfile as sf
    sf.write('wave_audio4.wav',wave_audio4,48000)
    
    #loading the slowed-down audio WAV file
    filename = ('wave_audio4.wav')
    y4, sr4 = librosa.load(filename)
    
    #plot the audio's wave
    import librosa.display
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y4, sr=sr4)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
#%%
slow()
#%%
#remix audio
def remix():
    #main packages
    import librosa
    import librosa.display
    import IPython.display
    import numpy as np
    import matplotlib.pyplot as plt
    from IPython.display import display

    #loading the WAV file
    filename = librosa.example('nutcracker')
    y, sr = librosa.load(filename)
    
    #printing the waveform and the sampling rate
    print('waveform')
    print(y)
    print('\nsampling rate')
    print(sr)
    
    #ploting the original wave
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y, sr=sr)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
    
    #play the audio as an array
    display(IPython.display.Audio(data=y, rate=sr))
    
    #compute beats
    _, beat_frames = librosa.beat.beat_track(y=y, sr=sr,
                                             hop_length=512)
    #convert from frames to sample indices
    beat_samples = librosa.frames_to_samples(beat_frames)
    
    #generate intervals from consecutive events
    intervals = librosa.util.frame(beat_samples, frame_length=2,
                                   hop_length=1).T
    
    #reverse the beat intervals
    y_out = librosa.effects.remix(y, intervals[::-1])
    
    #play the remix audio
    from IPython.display import Audio
    wave_audio_remix = np.sin(y_out)
    display(Audio(wave_audio_remix, rate=20000))
    
    #save the sped-up audio as a WAV file
    import soundfile as sf
    sf.write('wave_audio_remix.wav',wave_audio_remix,48000)
    
    #loading the sped-up audio WAV file
    filename = ('wave_audio_remix.wav')
    y5, sr5 = librosa.load(filename)
    
    #plot the audio's wave
    import librosa.display
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y5, sr=sr5)
    ax.set(title='Envelope view, mono')
    ax.label_outer()
#%%
remix()
#%%
