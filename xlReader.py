import pandas as pd
import json

eletricCauses = pd.read_excel("causes.xlsx")
mecanicCauses = pd.read_excel("causes.xlsx", "Mecânica")

eletricJson = (eletricCauses.to_json())
mecanicJson = (mecanicCauses.to_json())

formattedEletric = json.dumps(eletricJson, indent=4)
formattedmecanic = json.dumps(mecanicJson, indent=4)
jsonFile = open("data.json", "w")
jsonFile.write(formattedmecanic)