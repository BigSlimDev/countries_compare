import json
import os


class LocalStorage:
    def __init__(self, filename="data.json"):
        self.filename = filename
        # if file does not exit, create it
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump({}, file)

    # save the data with the key
    def save(self, key, data):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = json.load(file)
            content[key] = data
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(content, file, indent=4, ensure_ascii=False)
        except Exception:
            raise IOError("Error saving data.")

    # load a specific data with the key
    def load(self, key):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = json.load(file)
            return content.get(key)
        except Exception:
            raise IOError("Error loading data.")

    # load all the data in the json file
    def load_all(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return {}
        




        





    
class Localsave:
    def __init__(self, filename="data.txt"):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8"):
                pass

    def save(self, ke, value):
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"{ke}: {value}\n\n")
        except Exception:
            raise IOError("Error saving data.")

    def load_all(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return file.read()
        except Exception:
            return ""
        



