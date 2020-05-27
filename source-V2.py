import configparser

from tkinter import Tk, Label, Button
import pyperclip as p
from os import path


#
# Reece W. - 5/26/2020 V2
# Updated:
# - Better Config = Less code
# - Removed useless modules
# - More Efficent
#

CONFIG_FILE = 'config.txt' 

def debugPrint(e):
    if debugging.lower() == 'true':
        print(e)

#    
# == CONFIGS ==
#
config = configparser.ConfigParser()
config['SETTINGS'] = {
    'debug': False,
    'title': 'Copy-Paster',
    'fontsize': '18',
    'fontstyle': 'Courie',
    'windowdimensions': '250x250',
}

config['BUTTONS'] = {
    'Example 1': 'You clicked button 1',
    'Example 2': 'You have clicked button 2',
}

# Write default config if not there
if not path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

config.read(CONFIG_FILE)

# Save config vaules to variables
debugging = config['SETTINGS']['debug']
Title = config['SETTINGS']['title']
fontSize = config['SETTINGS']['fontSize']
fontStyle = config['SETTINGS']['fontStyle']
windowDimensions = config['SETTINGS']['windowDimensions']

debugPrint(f"{config['SETTINGS']}")

#
# == PROGRAM ==
#


class GUI:
    def __init__(self, master):
        self.master = master
        master.title(Title)
        master.geometry(windowDimensions)
        
        for button in config['BUTTONS']:
            labelName = button
            textToCopy = config['BUTTONS'][button]
            debugPrint(f"[+] Button Created: {labelName}:\"{textToCopy}\"")

            # Makes the lable if the config file is correct
            try:
                exec(f"""self.button = Button(master,font=(\'{fontStyle}\', {fontSize}), text=\'{labelName}\', command=lambda: p.copy(\"{textToCopy}\"))""")
                exec(f"""self.button.pack()""")
            except:
                debugPrint(f"[!] Button '{labelName}' failed to pack")
                continue

        debugPrint(f"[+] Done")


if __name__ == "__main__":
    root = Tk()
    my_gui = GUI(root)
    root.mainloop()

#
# == /PROGRAM ==
#
