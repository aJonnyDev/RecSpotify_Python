import pygetwindow as gw
import psutil

# Obtener una lista de todas las ventanas abiertas
windows = gw.getAllWindows()
spotifyOpen = 'Spotify Premium'
contador = 0

# Imprimir información sobre cada ventana
for window in windows:
    if( window.title == spotifyOpen):
        contador += 1

print("ha encontrado ",contador," aplicaciones de spotify")



# print("Título:", window.title)
# print("Clase:", window._hWnd)
# print("Rectángulo:", window.left, window.top, window.width, window.height)
# print("Estado:", window.isMinimized, window.isMaximized)
# print("------------------------")


# Esto es lo que devuelve:

# Título: Spotify Premium
# Clase: 526454
# Rectángulo: -25600 -25600 159 27
# Estado: True False
