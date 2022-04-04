import smtplib, ssl
from json import loads
from platform import platform
import os
from colorama import *
init(autoreset=True)

smtp_server = "smtp.gmail.com"
port = 587  

italic_style = "\033[3m"
bold_style = "\033[1m"

class main:

    def fatalerror(self, text):
        print(f"{Fore.RED}{Style.BRIGHT}{bold_style}{text}{Fore.RESET}{Style.RESET_ALL}\n")

    def custominput(self, text):
        return input(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}{text}{Fore.RESET}{Style.RESET_ALL}")

    def pressentertoexit(self):
        input(f"{Fore.RED}{Style.DIM}{italic_style}press enter to exit...{Fore.RESET}{Style.RESET_ALL}\n")
        exit()

    def clearscreen(self):
        if "windows" in platform():
            os.system("cls")
        else:
            os.system("clear")
    
    def removelinefromfile(self, thefile, line_to_delete):
        with open(thefile, "r") as f:
            lines = f.readlines()
        with open(thefile, "w") as f:
            for line in lines:
                if line.strip("\n") != line_to_delete:
                    f.write(line)

    def email_login(self, email, password):
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() 
        server.starttls(context=ssl.create_default_context()) 
        server.ehlo() 
        server.login(email, password)
        return server

    
    def customprint(self, text):
        print(f"{Fore.RED}{Style.DIM}[{Style.BRIGHT}{bold_style}INFO{Style.RESET_ALL}{Style.DIM}{Fore.RED}]{Style.RESET_ALL} {Style.BRIGHT}{Fore.LIGHTRED_EX}{text}")

    def start(self):
        email_list = main.custominput("Insert email list\n-> ")
        message = main.custominput("Insert message\n-> ") 
        subject = main.custominput("Insert subject\n-> ") 
        message = 'Subject: {}\n\n{}'.format(subject, message)
        main.customprint("Starting spam...")
        creds = main.getcredentials()
        
        content = loads(creds)
        email = content['mail']
        password = content['pass']
        main.customprint(f"Logging in with {italic_style}{email}{Style.RESET_ALL}...")
        loggedin = main.email_login(email, password)
        main.customprint("Reading emails...")
        f = open(email_list)
        for line in f.readlines():
            line = line.strip()
            main.customprint(f"Sending email to '{Fore.LIGHTYELLOW_EX}{line}{Fore.RED}'")
            loggedin.sendmail(email, line, message)
            main.removelinefromfile(email_list, line)
        loggedin.quit()
        main.custominput("All done!")
        

    def printlogo(self):
        print(f"""{Fore.RED}{Style.BRIGHT}
██╗  ██╗███╗   ███╗ █████╗ ██╗██╗     ██████╗ ██████╗  █████╗ 
██║ ██╔╝████╗ ████║██╔══██╗██║██║     ██╔══██╗██╔══██╗██╔══██╗
█████╔╝ ██╔████╔██║███████║██║██║     ██║  ██║██████╔╝███████║
██╔═██╗ ██║╚██╔╝██║██╔══██║██║██║     ██║  ██║██╔══██╗██╔══██║
██║  ██╗██║ ╚═╝ ██║██║  ██║██║███████╗██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
{italic_style}[·python3 mass mailer coded by {Style.RESET_ALL}{Style.DIM}{Fore.LIGHTRED_EX}@kl3sshydra{Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}{italic_style}·]
        """)

    def getcredentials(self):
        return open("credenziali.json", "r").read()


    def kmaildra(self):
        main.clearscreen()
        main.printlogo()
        main.start()
        main.pressentertoexit()


main = main()
main.kmaildra()