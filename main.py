
from datetime import datetime
currentDateAndTime = datetime.now()
datef=currentDateAndTime.strftime("%Y:%m:%d:%H:%M:%S")
import sounddevice as sd
from scipy.io.wavfile import write
filename=datef.replace(":","-")+".wav"

fs = 44100

rec = True
flag = True

while rec == True:
    seconds = 3
    try:
        seconds = int(input("Kayıt almak istediğiniz süreyi sayı olarak giriniz: "))
    except ValueError:
        flag = False

    if flag:
        print("Girilen değer bir sayı")

        break
    else:
        print("Girilen değer bir sayı değil!")

if rec == True:
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(filename, fs, myrecording)
    print(f"Kaydınız {filename} adlı dosyaya kaydedildi.")