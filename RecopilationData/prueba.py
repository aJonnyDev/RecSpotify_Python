import psutil
import pygetwindow as gw

def get_windows_in_processes():
    windows_in_processes = {}


    # Obtener todos los procesos en ejecución
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Obtener las ventanas abiertas en el proceso
            windows = gw.getWindowsWithTitle(proc.info['name'])
            if windows:
                windows_in_processes[proc.info['name']] = [win.title for win in windows]
        except psutil.AccessDenied:
            # Ignorar los procesos a los que no se puede acceder
            pass

    return windows_in_processes

if __name__ == "__main__":
    windows_in_processes = get_windows_in_processes()
    for process, windows in windows_in_processes.items():
        print(f"Proceso: {process}")
        for window in windows:
            print(f"- Ventana: {window}")