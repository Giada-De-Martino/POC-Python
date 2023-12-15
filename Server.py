
# classe Server
class Server:
    def __init__(self, id_server = "", credencials = "", port = 0, alias = ""):
        self.id_server = id_server
        self.credencials = credencials
        self.port = port
        self.alias = alias

    def __str__(self):
        return "IdServer : {}\nCredencials: {}\nPort: {}\nAlias: {}\n".format(self.id_server, self.credencials, self.port, self.alias)
