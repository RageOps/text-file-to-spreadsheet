from pynput.keyboard import Key, Controller
import json, time

# Initialize our keyboard controller
keyboard = Controller()

# Define our functions
def DoTab():
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

def DoEnter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

# Open the file with our json data and parse it to a python dict
t = open(r"") # Put your text path here, don't delete the r
file = json.loads(t.read())

# Sleep a certain amount of time before doing our actions
wait = 3
for x in range(wait): # 3 seconds
    time.sleep(1)
    print(wait-x)

# Using keyboard input, output all of your data into a spreadsheet file of your choosing
for key in file:
    for value in key:
        for data in value:
            keyboard.type(str(value[data]))
            DoTab()
            time.sleep(0.075) # Good idea to sleep the program so that things don't break
            continue
        DoEnter()
        continue
    DoEnter()
    keyboard.type('Next Section:') # To divide up our data in case of multiple subsections
    DoEnter()