import pandas as pd
import json

with open('text.json', encoding="UTF-8") as json_file:
    json_data = json.loads(json_file)
    json_string = json_data["BYLINE"]
    print(json_data)

