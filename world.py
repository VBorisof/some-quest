import context
import option

class World:
    scenario = None
    is_running = True

    def __init__(self, scenario):
        self.scenario = scenario

    def run(self):
        current_context=self.scenario.contexts[0]
        user_input=""
        while self.is_running:
            print("\n")
            print(" .--------------------------------------------------------------------------.")
            print("------------------------------------------------------------------------------")
            print(current_context.text)
            print("\\______________________________________________________________________________")
            print("| ")
            for i in range(0, len(current_context.options)):
                print("| " + str(i+1) + ". " +
                      current_context.options[i].text)
            print("\\______________________________________________________________________________")
            user_input=input("> ")

            try:
                if user_input == "q" : 
                    is_running = False
                    continue

                option_index=int(user_input)-1
                if (option_index<0
                    or option_index>len(current_context.options) - 1):
                   raise ValueError()
                
            except ValueError:
                print("[!] Please enter a valid option.")
                continue

            next_context_id = current_context.options[option_index].next
            current_context = next(filter(lambda c : c.id == next_context_id, self.scenario.contexts), None)


            if current_context is None:
                print("[+] Game over. Try again? (Y/n)")
                user_input=input("> ")

                if (user_input == "n" or user_input == "N"):
                    self.is_running = False

                break
