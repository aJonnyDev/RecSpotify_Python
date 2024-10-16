import os
import pyaudio
from pydub import AudioSegment
from CreationFolder import CreationFolder

# Ruta de la carpeta en el escritorio donde deseas guardar el archivo
folderDesktop = CreationFolder()

# Crear la carpeta si no existe
if not os.path.exists(folderDesktop):
    os.makedirs(folderDesktop)

# Nombre del archivo
fileName = "soundTest.wav"

# Ruta completa del archivo
file_path = os.path.join(folderDesktop, fileName)


# Tienes que instalar en el cmd de vsCode esto:
# -> pip install pyaudio
# -> pip install pydub
# -> pip install PyGetWindow 
# -> pip install psutil

# Configuración de la grabación de audio
FORMAT = pyaudio.paInt24
CHANNELS = 2
RATE = 48000
CHUNK = 1024
RECORD_SECONDS = 5


# Abre el stream de grabación
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Grabando...")

frames = []

# Lee el audio desde el stream
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("La grabacion esta bien chingona escuchala CORREEEE!!!!")

# Cierra el stream
stream.stop_stream()
stream.close()
audio.terminate()

sound = AudioSegment(data=b''.join(frames), sample_width=audio.get_sample_size(FORMAT), channels=CHANNELS, frame_rate=RATE)

sound.export(file_path, format="wav")

print(f"Grabación guardada como {file_path}")
