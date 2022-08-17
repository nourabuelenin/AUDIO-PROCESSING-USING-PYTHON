def noisereduction():
    #importing main packages
    import librosa
    import numpy as np
    import scipy as sp
    import librosa.display
    import IPython.display
    from IPython.display import display
    from scipy import signal
    from scipy.io import wavfile
    import noisereduce as nr
    #loading the pre-recorded WAV file
    filename = ('record.wav')
    y0, sr0 = librosa.load(filename)
    
    #play pre-recorded audio as an array
    display(IPython.display.Audio(data=y0, rate=sr0))
    
    #reduce noise by median
    def reduce_noise_median(y, sr):
        y = sp.signal.medfilt(y,3)
        return (y)
    wavfile.write("mywav_reduced_noise1.wav", sr0, reduce_noise_median(y0, sr0))
    
    #loading the 1st noise reduced WAV file
    filename = ('mywav_reduced_noise1.wav')
    y1, sr1 = librosa.load(filename)
    
    #perform 2nd noise reduction by noisereduce
    reduced_noise = nr.reduce_noise(y=y1, sr=sr1, thresh_n_mult_nonstationary=2,stationary=False)
    noise_reduced = nr.reduce_noise(y=y1, sr=sr1, prop_decrease=0, stationary=False)
    reduced_noise = nr.reduce_noise(
        y=y1,
        sr=sr1,
        thresh_n_mult_nonstationary=2,
        stationary=False,
        n_jobs=2,
    )
    wavfile.write("mywav_reduced_noise2.wav", sr1, reduced_noise)
    
    #loading the final noise reduced WAV file
    filename = ('mywav_reduced_noise2.wav')
    y2, sr2 = librosa.load(filename)
    
    #play pre-recorded audio after clarification as an array
    display(IPython.display.Audio(data=y2, rate=sr2))
#%%
noisereduction()
#%%
def trimsilence():
    #importing main packages
    import librosa
    import numpy as np
    import scipy as sp
    import librosa.display
    import IPython.display
    from IPython.display import display
    
    #loading the WAV file
    filename = ('mywav_reduced_noise.wav')
    y2, sr2 = librosa.load(filename)
    
    #trim the beginning and ending silence
    yt, index = librosa.effects.trim(y2)
    #print the durations
    print(librosa.get_duration(y2), librosa.get_duration(yt))
    from IPython.display import Audio
    wave_audio_trim = np.sin(yt)
    display(Audio(wave_audio_trim, rate=20000))
#%%
trimsilence()
