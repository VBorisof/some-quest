from option import Option

class Context:
    id = 0
    text = ""
    options = []

    def __init__(self, id, text, options):
        self.id = id
        self.text = text
        self.options = options

    @classmethod
    def from_json(cls, json_data):
    	print ("[Context] Got some data : " + str(json_data) + "\n")
    	result = cls(**json_data)
    	result.options = list(map(Option.from_json, json_data["options"]))
    	print ("[Context] Returning " + str(result) + "\n")
    	return result