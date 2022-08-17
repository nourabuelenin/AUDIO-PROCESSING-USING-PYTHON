def recordaudio():
    import sounddevice
    from scipy.io.wavfile import write
    from playsound import playsound
    #44100 or 48000 is used frequently in CDs and computer audio , there are other more commom frequency samples
    fs = 44100
    
    #duration of record
    second = 15
    
    print("recording....")
    
    #sounddevice.rec records an audio and save it in a form of numpy array
    record_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
    sounddevice.wait()
    
    #write(filnename,rate,data) which converts a numpy array into a wav file
    write('record.wav',fs,record_voice)
    
    print("playing record....")

    
    #Play record saved as wav file
    playsound('C:/Users/Hla Dawoud/Desktop/Python Project/record.wav')
