import random

import pyfiglet
from colorama import Fore

def GetuserAgent():
    """This Function return a random user agent """
    User = [
        "Mozilla/5.0 (Linux; Android 7.1.0; A30 Build/MNB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.4; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Mozilla/5.0 (X11; Linux i686; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Mozilla/5.0 (Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Mozilla/5.0 (Linux; Android 5.1.0; A6 Build/MNB19M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4464.104 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"]


    return {"user-agent":random.choice(User)}



   

class StartSimpleCLI:
    """
    Provide a Simple and minimal CLI to interact with program
    """
    
    VALID_COMMANDS = {
        "1": "DOS attack",
        "2":"contributors list",
        "3":"github repo",
        "?": "help"
    }



    def __init__(self):
        pass


    def GetSite(self):
        site = input("correct format: https://www.example.com\nsite: ")        
        if "https://" in site :
            pass
        elif not "https://" in site :
            site = f"https://{site}"
        elif "http://" in site :
            site = site.replace("http://","https://")
        return site
    
    def ShowLogo(self):
        """This Method Show Starter Logo in cli"""
        
        fig = pyfiglet.Figlet()
        SuggestedFont = ["ripper!_", "fbr_stri", "ugalympi", "stencil1", "nancyj-fancy", "nancyj-fancy", "alligator2", "speed", "ucf_fan_"]
    
        Message = "DOS ATTACKER"
        font = random.choice(SuggestedFont)
        pyfiglet.print_figlet(text=Message, font="speed", colors="GREEN")
        print(f"\n{Fore.RED}Repo: https://github.com/amirhosseindehghan1/Dos-attack{Fore.WHITE}\n")

    def Start(self):
        self.ShowLogo()
        self.Show_Help()
        site = self.GetInputAndCountibue()
        return site

    def GetInputAndCountibue(self):
        while 1:
            x = input(": ")
            if x not in self.VALID_COMMANDS:
                self.Invalid_Command()
                self.Show_Help()
                continue
            else:
                match x:
                    case "1":
                        site = self.GetSite()
                        return site
                    case "2":
                        self.Show_Contributors_List()
                        continue
                    case "3":
                        self.Show_Github_Repo()
                        continue
                    case "?":
                        self.Show_Help()
                        continue
                    case _:
                        self.Invalid_Command()
                        self.Show_Help()
                        continue



    def Show_Github_Repo(self):
        print(f"\n{Fore.RED}Repo: https://github.com/amirhosseindehghan1/Dos-attack{Fore.WHITE}\n")


    def Invalid_Command(self):
        print(f"{Fore.RED}Invalid Command!{Fore.WHITE}")


    def Show_Help(self):
        commands = (
        f"""{Fore.BLUE}commands{Fore.WHITE}:
        1. DOS Attack
        2. contributors List
        3. Github Repo
        ?. Help
        """)
        print(commands)
    

    def Show_Contributors_List(self):
        # don't forget to add your info to contributors_info
        contributors_info = [
            {
                "name": "Ali Sharirfy",
                "github": "https://github.com/alisharify7"
            },
        ]
        print("DOS ATTACKER contributors list")
        for index,value in enumerate(contributors_info):
            print(f"""  {index+1}:{value["name"]}\n\t-{value["github"]}""")

  