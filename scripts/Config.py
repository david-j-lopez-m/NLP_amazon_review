import json

class Config:

    def __init__(self):

        #Read main config gile (config.json)
        with open('config/config.json') as json_file:
            config = json.load(json_file)
            self.id_col = eval(config["id_cols"]) if "id_col" in config else None
            self.target_col =  eval(config["target_col"]) if "id_col" in config else None