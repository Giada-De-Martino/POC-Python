
# classe AutoBackup
class AutoBackup:

    def __init__(self, id_backup = "", frequency = 0, path = "", timestamp = 0, id_server = ""):
        self.id_backup = id_backup
        self.frequency = frequency
        self.path = path
        self.timestamp = timestamp
        self.id_server = id_server

    def __str__(self):
        return "IdBackUp : {}\nFrequency: {}\nPath: {}\nTimestamp: {}\nIDServer: {}\n".format(self.id_backup, self.frequency, self.path, self.timestamp, self.id_server)
