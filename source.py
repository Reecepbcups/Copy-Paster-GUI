#
# Reecepbcups#3370 - 7/1/2019 8:56 PM 
#

import time
import os.path
import random
import string
import pyperclip as p
from tkinter import Tk, Label, Button

debugging = False 

def removeText(string):
    '''
    Select the info after the "=" sign
    Replace all un-needed text char's
    '''
    try:
        return string.split('=')[1].replace("\"", "").replace('\n', '')
    except IndexError:
        debugPrint(f"\n[!] The button {string} is not correctly defined in Buttons.txt\n")

def debugPrint(error):
    if debugging == True:
        print(error)
#    
# == Window CONFIG ==
#

if os.path.exists("Config.txt") == False:
    with open("Config.txt", 'w') as f:
        f.write("""title=Copy-Paster\n""")
        f.write("""fontsize=18\n""")
        f.write("""fontstyle=Courier\n""")
        f.write("""windowdimensions=250x250""")
    f.close()
    config = open("Config.txt", 'r').readlines()
    debugPrint("[+] Config.txt file has been created & saved to RAM")
else:        
    config = open("Config.txt", 'r').readlines()
    debugPrint("[+] Config.txt has been loaded to RAM")


# Set Variables from Config
for option in config:
    if option.lower().startswith("debug"):
        debugging = True
        debugPrint(f"- Debugging: {debugging}")
    if option.lower().startswith("title"):
        Title = removeText(option)
        debugPrint(f"- Title: {Title}")
    if option.lower().startswith("fontsize"):
        fontSize = removeText(option)
        debugPrint(f"- Font Size: {fontSize}")
    if option.lower().startswith("fontstyle"):
        fontStyle = removeText(option)
        debugPrint(f"- Font Style: {fontStyle}")
    if option.lower().startswith("windowdimensions"):
        windowDimensions = removeText(option)
        debugPrint(f"- Dimensions: {windowDimensions}\n")
        
#        
# == /Window CONFIG == 
#

#
# == Button Config ==
#
if os.path.exists("Buttons.txt") == False:
    with open("Buttons.txt", 'w') as f:
        f.write("""Example 1=You clicked button 1\n""")
        f.write("""Example 2=You have clicked button 2\n""")
    f.close()
    buttons = open("Buttons.txt", 'r').readlines()
    debugPrint("[+] Buttons.txt has been created and saved to RAM")
else:        
    buttons = open("Buttons.txt", 'r').readlines()
    debugPrint("[+] Buttons.txt has loaded to RAM")

#
# == /Button Config ==
#

#
# == PROGRAM ==
#

class GUI:
    def __init__(self, master):
        self.master = master
        master.title(Title)
        master.geometry(windowDimensions)
        
        for text in buttons: 
            if text.startswith("newline"):
                # Creats a line break
                self.label = Label(master, text="\n")
                self.label.pack()
                debugPrint("[+] GUI line break inserted")
            
            else:
                # Gets Name before the = sign
                labelName = text.split('=')[0].replace('\n','')
                # Gets whats after the = sign
                textToCopy = removeText(text)
                debugPrint(f"[+] Button Created: {labelName}:\"{textToCopy}\"")

                try:
                    exec(f"""self.button = Button(master,font=(\'{fontStyle}\', {fontSize}), text=\'{labelName}\', command=lambda: p.copy(\"{textToCopy}\"))""")
                    exec(f"""self.button.pack()""")
                except:
                    debugPrint(f"[!] Button '{labelName}' failed to pack")
                    continue
        debugPrint(f"[+] Done")

root = Tk()
my_gui = GUI(root)
root.mainloop()

#
# == /PROGRAM ==
#
