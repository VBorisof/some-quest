import distutils.text_file
import json

from context import Context 
from typing import List

class Scenario:
    contexts=[]

    def __init__(self, filePath):
        text_file = distutils.text_file.TextFile(filePath)
        current_line=text_file.readline()
        all_text = ""
        while current_line != "" and current_line is not None:
            all_text += current_line
            current_line=text_file.readline()

        print(json.loads(all_text))
        self.contexts = Scenario.from_json(json.loads(all_text))
        

    @classmethod
    def from_json(cls, data):
        print("[Scenario] Got some data : " + str(data) + "\n")
        return list(map(Context.from_json, data["scenario"]))

