from pyfiglet import Figlet
import colorama

colorama.init()

def print_color_text(text, color):
    print(color + text +colorama.Style.RESET_ALL)

def get_colored_text(text, color):
    return color + text + colorama.Style.RESET_ALL
def main():
    name = input("What is your name: ")
    age = input("How old are you?: ")
    address = input("Where is your home address?: ")

    font = Figlet(font='small')

    name_enhance = font.renderText(name)
    age_enhance = font.renderText(age)
    address_enhance = font.renderText(address)

    print_color_text("Hello! ", colorama.Fore.BLUE)
    print_color_text(name_enhance, colorama.Fore.BLUE)
    print_color_text("Your age is ", colorama.Fore.RED)
    print_color_text(age_enhance, colorama.Fore.RED)
    print_color_text("And you currently living in ", colorama.Fore.YELLOW)
    print_color_text(address_enhance, colorama.Fore.YELLOW)
    print_color_text("Nice to meet you, " + name, colorama.Fore.BLUE)

if __name__ == "__main__":
    main()    
