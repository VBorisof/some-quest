import context
import choice

class World:
    context_stack=[]
    contexts=[]
    
    def __init__(self):
        
        context_1=context.Context(
            "Context 1"
        )
        choice_1_1=choice.Choice("Option 1.")
        choice_1_2=choice.Choice("Option 2.")

        context_1.choices = [
            choice_1_1,
            choice_1_2
        ]
        
        self.contexts=[
            context_1
        ]

    def run(self):
        current_context=self.contexts[0]
        user_input=""
        while user_input!="quit":
            print(current_context.text)
            for i in range(0, len(current_context.choices)):
                print("  " + str(i+1) + ". " +
                      current_context.choices[i].text)
            user_input=input("> ")

            try:
                option_index=int(user_input)-1
                if (option_index<0
                    or option_index>len(current_context.choices) - 1):
                   raise ValueError()
                
            except ValueError:
                print("[!] Please enter a valid option.")
                continue

            current_context=current_context.choices[option_index].next_context
            if current_context is None:
                print("[+] Game over.")
                break
