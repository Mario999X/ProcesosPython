import subprocess
import sys


def comprobar_so():
    controller = False
    os = sys.platform.lower()
    if os.__contains__("linux") or os.__contains__("mac"):
        controller = True
    print(os)
    return controller


def ping(url):
    # Comprobamos el so
    os = comprobar_so()

    if not os:
        # Windows
        process_1 = subprocess.Popen(["cmd.exe", "/c", f"ping {url}"], stdout=subprocess.PIPE,
                                     universal_newlines=True)
        output = process_1.communicate()[0]
        print(output)
    else:
        # Linux
        process_1 = subprocess.Popen(["bash", "-c", f"ping -c 5 {url}"], stdout=subprocess.PIPE,
                                     universal_newlines=True)
        output = process_1.communicate()[0]
        print(output)


def dir_ls(path):
    os = comprobar_so()

    if not os:
        # Windows
        process_1 = subprocess.Popen(["cmd.exe", "/c", f"dir {path}"], stdout=subprocess.PIPE,
                                     universal_newlines=True)
        output = process_1.communicate()[0]
        print(output)

    else:
        # Linux
        process_1 = subprocess.Popen(["bash", "-c", f"ls {path}"], stdout=subprocess.PIPE,
                                     universal_newlines=True)
        output = process_1.communicate()[0]
        print(output)


def ps_tasklist():
    os = comprobar_so()

    if not os:
        # Windows
        process_1 = subprocess.Popen(["cmd.exe", "/c", "tasklist"], stdout=subprocess.PIPE,
                                     universal_newlines=True)
        output = process_1.communicate()[0]
        print(output)

    else:
        # Linux
        process_1 = subprocess.Popen(["bash", "-c", "ps"], stdout=subprocess.PIPE,
                                     universal_newlines=True)
        output = process_1.communicate()[0]
        print(output)


def ejecucion():
    opcion = int(input("""
    Escoge la opcion que quiera ejecutar:
    1. Ping
    2. Dir/Ls
    3. PS/TaskList
    """))
    if opcion == 1:
        url = input("Introduzca una url/IP valida: ")
        ping(url)

    elif opcion == 2:
        path = input("Introduzca una ruta valida: ")
        dir_ls(path)

    elif opcion == 3:
        ps_tasklist()

    else:
        print("OPCION INCORRECTA")


ejecucion()
