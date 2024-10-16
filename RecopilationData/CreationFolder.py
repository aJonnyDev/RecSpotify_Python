import os

def roadToSave():
    nameUser = os.getlogin()
    roadToDesktop = os.path.join("C:\\Users", nameUser, "Desktop")
    return roadToDesktop


def CreationFolder():
    
    nameFolder = input("¿Nombre de la carpeta a crear?\n")
    roadFull = os.path.join(roadToSave(), nameFolder)
    os.makedirs(roadFull)
    return roadFull

