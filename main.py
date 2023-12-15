# Creation d'un POC pour la lecture d'un fichier poc.conf
# Importation des classes
from Server import Server
from AutoBackup import AutoBackup


# on lis le fichier
def parsingFile():
    fichier = open("poc.conf", "r")
    ligne = fichier.readlines()
    name_class = ""

    for oneLine in ligne:
        if oneLine[0] == "[":
            name_class = nameClass(oneLine)
        else:
            list_element = parsingLine(oneLine)
            createClass(name_class, list_element)


# on lis la ligne du fichier passée en paramètre et on la divise
def parsingLine(ligne):
    list_element = []
    ligne = ligne.strip()
    i = 0
    while True:
        if ligne[i] != "\n":
            list_element = ligne.split(", ")
            i += 1
        break
    return list_element


# on renvoie la classe associé au texte passé en paramètres
def nameClass(texte):
     return "".join(filter(str.isalnum, texte))


# on crée les objects et on les sauvgardes dans les listes
def createClass(name_class, list_element):
    if name_class == "server":
        name_class = Server(list_element[0], list_element[1], list_element[2], list_element[3])
        list_server.append(name_class)
    if name_class == "autobackup":
        name_class = AutoBackup(list_element[0], list_element[1], list_element[2], list_element[3], list_element[4])
        list_auto_backup.append(name_class)


# main
if __name__ == '__main__':
    list_server = []
    list_auto_backup = []

    parsingFile()

    for auto_backup in list_auto_backup:
        print(auto_backup)

    for server in list_server:
        print(str(server))
