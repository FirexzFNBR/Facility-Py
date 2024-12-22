import webbrowser
from colorama import *

def open():
    try:
        print(Fore.CYAN + "Bem - Vindo ao Facility Py!")
        print(Fore.YELLOW + "Escolha uma opção:")
        print(Fore.WHITE + "(1) Instalar Epic Games")
        print("(2) Instalar Steam")

        choice = input(">> ")

        if choice == "1":
            url = "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi"
        elif choice == "2":
            url = "https://cdn.fastly.steamstatic.com/client/installer/SteamSetup.exe"

        else:
            print("Opção inválida. Por favor escolha as opções acima.")
            return

        webbrowser.open(url)
        print(Fore.GREEN + f"O link {url} foi aberto no navegador.")
    except Exception as e:
        print(Fore.RED + f"Ocorreu um erro ao abrir o link: {url} -- Erro: {e}")

if __name__ == "__main__":
    open()             