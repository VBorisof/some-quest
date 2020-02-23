class Option:
    text = ""
    next = 0
    
    def __init__(self, text, next):
        self.text = text
        self.next = next

    @classmethod
    def from_json(cls, json_data):
    	print("[Option] Got some data : " + str(json_data) + "\n")
    	result = cls(**json_data)
    	print ("[Option] Returning " + str(result) + "\n")
    	return result
