import distutils.text_file
import json.decoder

class Scenario:
    contexts=[]

    def __init__(self, filePath):
        text_file = distutils.text_file.TextFile(filePath)
        current_line=text_file.readline()
        all_text = ""
        while current_line != "" and current_line is not None:
            print ("[D] " + current_line)
            all_text += current_line
            current_line=text_file.readline()

        decoded = json.decoder.JSONDecoder().decode(all_text)

        contexts=decoded["scenario"]
        print ("[D] " + str(decoded))
        
