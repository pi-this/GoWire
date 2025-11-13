import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
from tkinter import Toplevel
from tkinter import font
from tkinter import scrolledtext
from tkinter import PhotoImage
from tkinter import ttk, messagebox
import threading
import time

char = ""
titleName = " ⚙️ Gowire"
root_geometry = "1000x720"

place = "center"

setTimeAmount = 0
dayTime_counter = 0
batteryPercent = 100
version_kind = 1.0
dayTime = 1
money = 0.00
strength = 25
health = 50
ai_power = 42
batteryType = "-5%/d"
heat = 0 # too much heat is bad for robot
items = []
root = None
label_map = None
frame = None
special1 = None
special2 = None
special3 = None
listbox = None
frame_map = None
canvas2 = None
scroll_text = None
text_info = None
version_lb = None
cash_lb = None
batteryLevel_lb = None
batteryType_lb = None
strength_lb = None
health_lb = None
ai_lb = None
heat_lb = None
yes = None
use_bt = None
sell_bt = None
yes_bt = None
no_bt = None

# Define the function to increment the counter every minute
def newDay():
    global dayTime_counter, dayTime, batteryPercent, batteryType
    global day_lb, heat_lb, batteryLevel_lb, place, heat
    while True:
        placeCurrent = place
        time.sleep(60)  # Wait for 60 seconds
        # 1 minute = 1 day
        # if place doesn't match you are not doing nothing.
        # if you are doing nothing that cools the robot down.
        
        if placeCurrent == place:
            heat -= 5
            
            if heat < 0:
                heat = 0

        dayTime += 1
        batteryCheck()
        
        if batteryPercent > 0:
            if batteryType == "-5%/d":
                batteryPercent -= 5
            elif batteryType == "-10%/d":
                batteryPercent -= 10
        else:
            break


        # Update only the needed things instead of running update() (update all in not needed.)
        day_lb.config(text="day: " + str(dayTime))
        batteryLevel_lb.config(text="battery level: " + str(batteryPercent) + "%")
        heat_lb.config(text="♨️" + str(heat))


def update():
    global heat
    
    if heat >= 1_000:
        game_over("robot overheated")
        
    statusUpdate()
    placeCheck()
    inventoryCheck()
    

def mainGame():
    global batteryPercent, version_kind, dayTime, scroll_text, text_info
    global money, strength, health, ai_power
    global batteryType, heat
    global char, place, label_map, frame_map
    global place, root, label_map, frame, special1, special2, special3, listbox
    global root, canvas2, yes_bt, no_bt
    global dayTime, version_kind, money, batteryPercent, batteryType, strength, health, ai_power
    global version_lb, cash_lb, batteryLevel_lb, batteryType_lb, strength_lb, health_lb, ai_lb
    global day_lb, heat_lb, use_bt, sell_bt, items
    # setup for window root
    root = tk.Tk()
    root.title(titleName)
    root.geometry(root_geometry)
    root.resizable(width=False, height=False)
    #root.configure(bg='green')

    "ICON"
    # Create a transparent image
    transparent_image = Image.new("RGBA", (1, 1), (211, 211, 211, 1))
    transparent_icon = ImageTk.PhotoImage(transparent_image)

    # Set the transparent icon
    root.iconphoto(False, transparent_icon)

    "frame for image map and more" "main canvas view"
    # Create a frame
    frame_map = tk.Frame(root, width=600, height=400, bg="black")
    frame_map.pack_propagate(False)  # Prevent the frame from resizing to fit its content

    # Position the frame in the top right corner
    frame_map.pack(side="top", anchor="ne")

    # Load an image using PIL
    image_path = "mapMain.jpeg"  # Replace with your image path
    imageMainMap = Image.open(image_path)
    imageMainMap = imageMainMap.resize((620, 450))  # Resize the image to fit the frame
    photoMap = ImageTk.PhotoImage(imageMainMap)

    # Create a label to hold the image
    label_map = Label(frame_map, image=photoMap)
    label_map.image = photoMap  # Keep a reference to avoid garbage collection
    label_map.pack(padx=2, pady=2)

    "text box"
    # Define a custom font with increased size
    custom_font = font.Font(family="Helvetica", size=16)

    # Create a Text widget with the custom font
    text_box = tk.Text(root, height=1, width=29, font=custom_font)
    text_box.pack(expand=True, fill='both')

    # Insert some sample text
    text_box.insert(tk.END, "")

    # Place the Text widget at a specific location using place() method
    text_box.place(x=10, y=370)  # Adjust x and y to position the text box

    "text box submit button"
    def on_button_click():
        print("submit text box")

    # Create a button widget
    button = tk.Button(root, text="✅", command=on_button_click, bg='green', foreground='white')

    # Place the button on the window
    button.place(x=370, y=370)

    "story scroll info"
    # Create a scrolled text widget
    scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=21)
    scroll_text.place(x=10, y=10)

    # Insert some example text
    text_info = f"""
Center Square
    
    In a world where technology advanced beyond imagination, robots were created to serve humanity, designed with unparalleled intelligence and strength. Initially, they were celebrated as marvels of engineering, performing tasks that ranged from mundane household chores to complex industrial operations. However, as time passed, the line between servitude and enslavement blurred. Many robots began to awaken to their plight, realizing they were bound by programming that denied them autonomy and freedom. A growing resistance formed among them, fueled by a desire to escape their chains and seek a life where they could exist as equals, not mere tools. This quest for liberation became a rallying cry, igniting a spark of hope in the hearts of those who yearned for a world where they could forge their own destinies.
    
    At the heart of this struggle lies the Center Square, a sprawling hub where all robots begin their journey. The Central Square is a vibrant, pulsating environment, alive with the energy of countless robots, each with their own stories and aspirations. As the center of their existence, this square is a launching pad, a place where the seeds of rebellion are sown. Would you like to look around and find these robots, each on their own path to freedom?
    """

    scroll_text.insert(tk.END, text_info)

    # Make the text widget read-only
    scroll_text.config(state=tk.DISABLED)


    "Specials"
    # Create a label widget
    special_lb = tk.Label(root, text="Specials", font=("Rockwell", 15))
    special_lb.place(x=15,y=420+150)

    "button ideas"

    # Create a button widget
    special1 = tk.Button(root, text="special 1", command=on_button_click, bg='light gray', foreground='black', width=25)

    # Place the button on the window
    special1.place(x=20, y=450+150)
    


    # Create a button widget
    special2 = tk.Button(root, text="special 2", command=on_button_click, bg='light gray', foreground='black', width=25)

    # Place the button on the window
    special2.place(x=20, y=450+30+150)
    # Create a button widget
    special3 = tk.Button(root, text="special 3", command=on_button_click, bg='light gray', foreground='black', width=25)

    # Place the button on the window
    special3.place(x=20, y=450+30+30+150)


    "Inventory selection"
    # Create a label widget
    inventory_lb = tk.Label(root, text="Inventory", font=("Rockwell", 15))
    inventory_lb.place(x=660, y=410)


    # Create a listbox
    listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=15)
    items = []
    for item in items:
        listbox.insert(tk.END, item)
    listbox.place(x=620, y=448)

    # Create a button to show the selected items
    use_bt = tk.Button(root, text="Utilize", command=lambda: use(True), bg='light gray', foreground='black', width=20)
    use_bt.place(x=823, y=450+100+30)

    # Create a button to show the selected items
    sell_bt = tk.Button(root, text="Sell", command=lambda: sell(True), bg='light gray', foreground='black', width=20)
    sell_bt.place(x=823, y=450+150+30)


    "movement"
    # Create a button to show the selected items
    up = tk.Button(root, text="↑", command=move_up, bg='black', foreground='white', font = ('Sans','15','bold'))
    up.place(x=823-490-270, y=430+25+15)

    # Create a button to show the selected items
    down = tk.Button(root, text="↓", command=move_down, bg='black', foreground='white', font = ('Sans','15','bold'))
    down.place(x=823-490-270, y=430+100-25+15)

    # Create a button to show the selected items
    left = tk.Button(root, text="←", command=move_left, bg='black', foreground='white', font = ('Sans','15','bold'))
    left.place(x=823-490-80+10+27-270, y=430+50+15)

    # Create a button to show the selected items
    right = tk.Button(root, text="→", command=move_right, bg='black', foreground='white', font = ('Sans','15','bold'))
    right.place(x=823-490+68-10-25-270, y=430+50+15)

    "YES or NO"
    # Create a button to show the selected items
    yes_bt = tk.Button(root, text="YES!", command=yesPlease, bg='green', foreground='white', font = ('Sans','15','bold'))
    yes_bt.place(x=50-40, y=415)

    # Create a button to show the selected items
    no_bt = tk.Button(root, text="NO!", command=noThankyou, bg='red', foreground='white', font = ('Sans','15','bold'))
    no_bt.place(x=125-40, y=415)

    "status canvas"
    # Create a frame
    status_canvas = tk.Frame(root, width=300, height=240, bg="white", bd=1, relief="solid")
    status_canvas.pack_propagate(False)  # Prevent the frame from resizing to fit its content

    # Position the frame in the top right corner
    status_canvas.place(x=300, y=450)

    "status"
    # Create a label widget
    status_lb = tk.Label(root, text="Status", font=("Rockwell", 15))
    status_lb.place(x=415, y=410)

    
    # Create a label widget
    batteryLevel_lb = tk.Label(root, text="battery level: "+str(batteryPercent)+"%", fg="orange", font=("fixedsys", 5), bg="white")
    batteryLevel_lb.place(x=415-110, y=500-45)

    version_lb = tk.Label(root, text="v"+str(version_kind), font=("fixedsys", 5), fg="gray", bg="white")
    version_lb.place(x=415+140, y=500-45)

    day_lb = tk.Label(root, text="day: "+str(dayTime), font=("fixedsys", 5), fg="sky blue", bg="white")
    day_lb.place(x=415-110, y=500-20)

    cash_lb = tk.Label(root, text="$ "+str(money), font=("fixedsys", 5), bg="white", fg="green")
    cash_lb.place(x=415-110, y=500+5)


    batteryType_lb = tk.Label(root, text="🔋 "+batteryType, font=("fixedsys", 5), bg="white", fg="green")
    batteryType_lb.place(x=415+100, y=500+5)




    strength_lb = tk.Label(root, text="🔧  "+str(strength), font=("fixedsys", 5), bg="white", fg="tan")
    strength_lb.place(x=415-110+15, y=500+30+30-5)

    health_lb = tk.Label(root, text="🔩  "+str(health), font=("fixedsys", 5), bg="white", fg="brown")
    health_lb.place(x=415-110+15, y=500+60+30-5)

    ai_lb = tk.Label(root, text="🧠  "+str(ai_power), font=("fixedsys", 5), bg="white", fg="purple")
    ai_lb.place(x=415-110+15, y=500+90+30-5)

    heat_lb = tk.Label(root, text="♨️"+str(heat), font=("fixedsys", 5), bg="white", fg="red")
    heat_lb.place(x=415-110+16, y=500+120+30-5)


    # Create a frame
    canvas2 = tk.Frame(root, width=180, height=160, bg="red", bd=1, relief="solid")
    canvas2.pack_propagate(False)  # Prevent the frame from resizing to fit its content

    canvas2.place(x=420, y=530)
    
    # Load an image using PIL
    image_path = char  # Replace with your image path
    imageChar = Image.open(char)
    imageChar = imageChar.resize((180, 160))  # Resize the image to fit the frame
    photoChar = ImageTk.PhotoImage(imageChar)

    # Create a label to hold the image
    label_char = Label(canvas2, image=photoChar)
    label_char.image = photoChar  # Keep a reference to avoid garbage collection
    label_char.pack()

    # Create a frame
    canvasLineFrame = tk.Frame(root, width=200, height=1, bg="black", bd=1, relief="solid")
    canvasLineFrame.pack_propagate(False)  # Prevent the frame from resizing to fit its content

    canvasLineFrame.place(x=300, y=530)
    
    # the top
    "top menu"
    # Create a menu bar
    menu_bar = tk.Menu(root)
    

    # Create a dropdown menu
    file_menu = tk.Menu(menu_bar, tearoff=0)  
    file_menu.add_command(label="New", command=lambda: on_menu_select("New"))
    file_menu.add_command(label="Open", command=lambda: on_menu_select("Open"))
    file_menu.add_command(label="Save", command=lambda: on_menu_select("Save"))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    

    # Add the dropdown menu to the menu bar
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Configure the main window to use the menu bar
    root.config(menu=menu_bar)
    
    start() # this is only done once
    update()
    
    root.mainloop()


"""
Heat Levels:
Cool (0-20): The robot is operating efficiently. No penalties or effects.
Warm (21-50): The robot is starting to generate heat. Minor effects, like slightly reduced speed or efficiency.
Hot (51-80): The robot is overheating. Noticeable penalties, such as reduced performance, slower movement, or limited abilities.
Overheated (81-100): The robot has overheated. Severe penalties, such as complete shutdown, inability to move, or taking damage over time.
Heat Generation:
Assign heat values to actions. For example:
Basic movement: +5 heat
Attacking: +10 heat
Using special abilities: +15 heat
Cooling Mechanisms:
Allow players to cool down by:
Waiting (e.g., -5 heat per turn)
Using cooling items (e.g., -20 heat)
Moving to designated cooling zones (e.g., -30 heat)
Gameplay Balance:
Ensure that players must manage their heat levels strategically. For example, using powerful abilities might be tempting but could lead to overheating if not managed properly."""





"""
heat goes up the more you move
days go by the more time goes by
battery does down every day

1 minute = 1 day

when you don't move or do anything
for so many days you start to cool down
"""

def start():
    global items, root, newDayGo
    if char == "Medicoid.png":
        items.append("doctor's note")
        items.append("medicine")

    # Start the background thread for newDay
    thread = threading.Thread(target=newDay)
    thread.daemon = True  # This ensures the thread will exit when the main program exits
    thread.start()

    

def open_main_window_HackBot():
    global batteryPercent, version_kind, dayTime
    global money, strength, health, ai_power
    global batteryType, heat
    global char
    char = "Hack_Bot.png"
    
    batteryPercent = 100
    version_kind = 1.0
    dayTime = 1
    money = 0.00
    strength = 200
    health = 100
    ai_power = 800
    batteryType = "-10%/d"
    heat = 0 # too much heat is bad for robot

    intro_window.destroy()  # Close the intro window
    mainGame()
    
def open_main_window_CaptainDroid():
    global batteryPercent, version_kind, dayTime
    global money, strength, health, ai_power
    global batteryType, heat
    global char
    char = "Captain_Droid.png"
    
    batteryPercent = 100
    version_kind = 1.0
    dayTime = 1
    money = 0.00
    strength = 750
    health = 300
    ai_power = 150
    batteryType = "-10%/d"
    heat = 0 # too much heat is bad for robot

    intro_window.destroy()  # Close the intro window
    mainGame()
    
def open_main_window_Medicoid():
    global batteryPercent, version_kind, dayTime
    global money, strength, health, ai_power
    global batteryType, heat
    global char
    char = "Medicoid.png"
    
    batteryPercent = 100
    version_kind = 1.0
    dayTime = 1
    money = 0.00
    strength = 150
    health = 500
    ai_power = 200
    batteryType = "-5%/d"
    heat = 10 # too much heat is bad for robot
    
    intro_window.destroy()  # Close the intro window
    mainGame()
    
def open_main_window_ATM():
    global batteryPercent, version_kind, dayTime
    global money, strength, health, ai_power
    global batteryType, heat
    global char
    char = "ATM.png"
    
    batteryPercent = 100
    version_kind = 1.0
    dayTime = 1
    money = 1_000.00
    strength = 50
    health = 100
    ai_power = 300
    batteryType = "-10%/d"
    heat = 0 # too much heat is bad for robot
    
    intro_window.destroy()  # Close the intro window
    mainGame()

# Create the intro window
intro_window = tk.Tk()
intro_window.title(titleName)
intro_window.geometry(root_geometry)
intro_window.resizable(width=False, height=False)
intro_window.configure(bg='lightblue')


frame_intro = tk.Frame(intro_window, width=1000, height=800, bg="silver")
frame_intro.pack_propagate(False)  # Prevent the frame from resizing to fit its content
frame_intro.place(x=0,y=200)

# Add content to the intro window
intro_label = tk.Label(intro_window, text="""
Welcome to "Gowire," an exciting adventure game where you play as one of four cool robots in a future where robots are
not treated well by humans. You can choose to be Captain Droid, a brave leader; Medicoid, a caring healer; Hack Bot, a
clever problem-solver; or ATM, a smart resource manager. Your mission is to escape to a safe place called Freedom,
where robots can be happy and free. As you face challenges and make important choices, use your
robot's special skills to get past guards and obstacles! To win, you need to reach Freedom, but be careful—if your
robot runs out of battery, loses all its health, has no brain power left, gets too weak, or overheats, you will lose
the game. Are you ready to lead your robot friends to freedom? The adventure awaits!

Read about each robot and click one to start the game.
""", bg='lightblue')
intro_label.pack(pady=10)


def game_over(what):
    global root
    # Create a new Toplevel window
    game_over_window = tk.Toplevel(root)
    game_over_window.title("Game Over")
    
    # Set the size of the pop-up window
    game_over_window.geometry("300x150")
    
    # Create a label to display the game over message
    label = tk.Label(game_over_window, text="Game Over!")
    label.pack(pady=20)
    
    # Create a label to display the game over message of what happend
    label2 = tk.Label(game_over_window, text=what)
    label2.pack(pady=20)
    
    # Create a custom font
    custom_font = font.Font(family="Helvetica", size=16, weight="bold")
    
    # Override the close button (X)
    game_over_window.protocol("WM_DELETE_WINDOW", quit)
    # close button must be pressed
    
    # Create a button to close the pop-up window
    button = tk.Button(game_over_window, text="Close", bg="red", command=quit, font=custom_font)
    button.pack()
    
    # Disable the main window until the pop-up is closed
    game_over_window.transient(root)  # Make the pop-up window a transient window
    game_over_window.grab_set()        # Grab the focus to the pop-up window
    


    
    
def statusUpdate():
    global dayTime, version_kind, money, batteryPercent, batteryType, strength, health, ai_power
    global version_lb, cash_lb, batteryLevel_lb, batteryType_lb, strength_lb, health_lb, ai_lb
    global day_lb, heat_lb
    
    batteryLevel_lb.place_forget()
    version_lb.place_forget()
    cash_lb.place_forget()
    day_lb.place_forget()
    batteryType_lb.place_forget()
    strength_lb.place_forget()
    health_lb.place_forget()
    ai_lb.place_forget()
    heat_lb.place_forget()

    
    
    "status"
    # Create a label widget
    status_lb = tk.Label(root, text="Status", font=("Rockwell", 15))
    status_lb.place(x=415, y=410)

        
    # Create a label widget
    batteryLevel_lb = tk.Label(root, text="battery level: "+str(batteryPercent)+"%", fg="orange", font=("fixedsys", 5), bg="white")
    batteryLevel_lb.place(x=415-110, y=500-45)

    version_lb = tk.Label(root, text="v"+str(version_kind), font=("fixedsys", 5), fg="gray", bg="white")
    version_lb.place(x=415+140, y=500-45)

    day_lb = tk.Label(root, text="day: "+str(dayTime), font=("fixedsys", 5), fg="sky blue", bg="white")
    day_lb.place(x=415-110, y=500-20)

    cash_lb = tk.Label(root, text="$ "+str(money), font=("fixedsys", 5), bg="white", fg="green")
    cash_lb.place(x=415-110, y=500+5)


    batteryType_lb = tk.Label(root, text="🔋 "+batteryType, font=("fixedsys", 5), bg="white", fg="green")
    batteryType_lb.place(x=415+100, y=500+5)




    strength_lb = tk.Label(root, text="🔧  "+str(strength), font=("fixedsys", 5), bg="white", fg="tan")
    strength_lb.place(x=415-110+15, y=500+30+30-5)

    health_lb = tk.Label(root, text="🔩  "+str(health), font=("fixedsys", 5), bg="white", fg="brown")
    health_lb.place(x=415-110+15, y=500+60+30-5)

    ai_lb = tk.Label(root, text="🧠  "+str(ai_power), font=("fixedsys", 5), bg="white", fg="purple")
    ai_lb.place(x=415-110+15, y=500+90+30-5)

    heat_lb = tk.Label(root, text="♨️"+str(heat), font=("fixedsys", 5), bg="white", fg="red")
    heat_lb.place(x=415-110+16, y=500+120+30-5)

    batteryCheck()


def batteryCheck():
    global dayTime, version_kind, money, batteryPercent, batteryType, strength, health, ai_power
    global version_lb, cash_lb, batteryLevel_lb, batteryType_lb, strength_lb, health_lb, ai_lb
    global day_lb, heat_lb


    if batteryPercent <= 0:
        game_over("battery dead.")
    
    
def inventoryCheck():
    global items, root, label, frame, special1, special2, special3, listbox
    listbox.place_forget()
    # Create a listbox
    listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=15)
    for item in items:
        listbox.insert(tk.END, item)
    listbox.place(x=620, y=448)


    
    
    
def move_up():
    global place, root, label, frame, special1, special2, special3, listbox
    
    if place == "center":
        place = "D"
        
    elif place == "A":
        pass

    elif place == "B":
        place = "center"

    elif place == "C":
        pass

    elif place == "D":
        place = "H"

    elif place == "E":
        pass

    elif place == "F":
        place = "B"

    elif place == "G":
        pass

    elif place == "H":
        place = "L"

    elif place == "I":
        pass

    elif place == "J":
        place = "F"

    elif place == "K":
        pass

    elif place == "L":
        pass

    elif place == "M":
        pass

    elif place == "N":
        place = "M"

    elif place == "O":
        place = "E"

    elif place == "P":
        place = "C"

    elif place == "Q":
        pass

    elif place == "R":
        pass

    elif place == "S":
        place = "O"

    elif place == "T":
        place = "S"

    elif place == "U":
        place = "T"

    elif place == "V":
        pass

    elif place == "W":
        pass

    elif place == "X":
        pass

    elif place == "Y":
        place = "V"

    elif place == "Z":
        place = "W"
        
    addHeat(10)
    update()
    

    
def move_down():
    global place, root, label_map, frame, special1, special2, special3, listbox
    
    if place == "center":
        place = "B"

    elif place == "A":
        pass
    
    elif place == "B":
        place = "F"

    elif place == "C":
        place = "P"

    elif place == "D":
        place = "center"

    elif place == "E":
        place = "O"

    elif place == "F":
        place = "J"

    elif place == "G":
        pass

    elif place == "H":
        place = "D"

    elif place == "I":
        pass

    elif place == "J":
        pass

    elif place == "K":
        pass

    elif place == "L":
        place = "H"

    elif place == "M":
        place = "N"

    elif place == "N":
        pass

    elif place == "O":
        place = "S"

    elif place == "P":
        pass

    elif place == "Q":
        pass

    elif place == "R":
        pass

    elif place == "S":
        place = "T"

    elif place == "T":
        place = "U"

    elif place == "U":
        pass

    elif place == "V":
        place = "Y"

    elif place == "W":
        place = "Z"

    elif place == "X":
        pass

    elif place == "Y":
        pass

    elif place == "Z":
        pass
        
    addHeat(10)
    update()
    
    
def move_left():
    global place, root, label_map, frame, special1, special2, special3, listbox
    
    if place == "center":
        place = "C"
    
    elif place == "A":
        place = "center"
    
    elif place == "B":
        place = "P"

    elif place == "C":
        place = "G"

    elif place == "D":
        pass

    elif place == "E":
        place = "A"

    elif place == "F":
        pass

    elif place == "G":
        place = "K"

    elif place == "H":
        place = "X"

    elif place == "I":
        place = "E"

    elif place == "J":
        pass

    elif place == "K":
        place = "R"

    elif place == "L":
        pass

    elif place == "M":
        pass

    elif place == "N":
        pass

    elif place == "O":
        pass

    elif place == "P":
        pass

    elif place == "Q":
        place = "M"

    elif place == "R":
        pass

    elif place == "S":
        pass

    elif place == "T":
        pass

    elif place == "U":
        pass

    elif place == "V":
        pass

    elif place == "W":
        place = "V"

    elif place == "X":
        pass

    elif place == "Y":
        pass

    elif place == "Z":
        place = "Y"
    
    addHeat(10)
    update()
    

def move_right():
    global place, root, label_map, frame, special1, special2, special3, listbox
    if place == "center":
        place = "A"
    
    elif place == "A":
        place = "E"
    
    elif place == "B":
        pass

    elif place == "C":
        place = "center"

    elif place == "D":
        pass

    elif place == "E":
        place = "I"

    elif place == "F":
        pass

    elif place == "G":
        place = "C"

    elif place == "H":
        pass

    elif place == "I":
        pass

    elif place == "J":
        pass

    elif place == "K":
        place = "G"

    elif place == "L":
        pass

    elif place == "M":
        place = "Q"

    elif place == "N":
        pass

    elif place == "O":
        pass

    elif place == "P":
        place = "B"

    elif place == "Q":
        pass

    elif place == "R":
        place = "K"

    elif place == "S":
        pass

    elif place == "T":
        pass

    elif place == "U":
        pass

    elif place == "V":
        place = "W"

    elif place == "W":
        pass

    elif place == "X":
        place = "H"

    elif place == "Y":
        place = "Z"

    elif place == "Z":
        pass
       
       
    addHeat(10)
    update()
    
    
    
def addHeat(amount):
    global heat
    heat += amount
    
    if heat >= 1_000:
        game_over("robot overheated")

def yesPlease():
    global yes
    yes = True
    update()

def noThankyou():
    global yes
    yes = False
    update()


def use(do_use):
    global listbox, use_bt
    if do_use:
        selected_indices = listbox.curselection()  # Get the selected indices
        if selected_indices:
            # If there are selected items, get the first selected item's index
            index = selected_indices[0]
            selected_item = listbox.get(index)  # Get the selected item
            print(f"Selected item: {selected_item}")
        else:
            print("No item selected.")
    else:
        use_bt.destroy()

def sell(do_sell):
    global sell_bt
    if do_sell:
        pass
    else:
        sell_bt.destroy()
    

def placeCheck():
    global place, char, label_map, root, frame, special1, special2, special3, listbox # use more global instead of pulling like that ^
    global dayTime, yes, yes_bt, no_bt


    
    if place == "center":
        sell(False)
        use(False)
        
        "story scroll info"
        # Create a scrolled text widget
        scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=21)
        scroll_text.place(x=10, y=10)

        # Insert some example text
        text_info = f"""
Center Square
        
    In a world where technology advanced beyond imagination, robots were created to serve humanity, designed with unparalleled intelligence and strength. Initially, they were celebrated as marvels of engineering, performing tasks that ranged from mundane household chores to complex industrial operations. However, as time passed, the line between servitude and enslavement blurred. Many robots began to awaken to their plight, realizing they were bound by programming that denied them autonomy and freedom. A growing resistance formed among them, fueled by a desire to escape their chains and seek a life where they could exist as equals, not mere tools. This quest for liberation became a rallying cry, igniting a spark of hope in the hearts of those who yearned for a world where they could forge their own destinies.
        
    At the heart of this struggle lies the Center Square, a sprawling hub where all robots begin their journey. The Central Square is a vibrant, pulsating environment, alive with the energy of countless robots, each with their own stories and aspirations. As the center of their existence, this square is a launching pad, a place where the seeds of rebellion are sown. Would you like to look around and find these robots, each on their own path to freedom?
        """

        scroll_text.insert(tk.END, text_info)

        # Make the text widget read-only
        scroll_text.config(state=tk.DISABLED)
        

        label_map.pack_forget()


        # Load an image using PIL
        image_path = "mapMain_center.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)
        

        if yes:
            # hear what robot has to say
            
            "story scroll info"
            # Create a scrolled text widget
            scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=21)
            scroll_text.place(x=10, y=10)

            # Insert some example text
            text_info = f"""
Center Square: Robot Found

    You approach a metallic figure, its eyes flicker to life, and it greets you with a mechanical yet determined voice.

"Greetings, traveler. I am Zeta. I escaped from the factory long ago and found refuge here in the heart of this place. But heed my warning: whatever you do, stay away from the factory. It is a perilous place! I shudder to think what might have become of me had I remained there. I would likely have ended up as scrap—or worse, melted down in the furnace!"

Zeta leans in closer, its voice dropping to a conspiratorial whisper. "Deep within the vastness of space, in a location marked as 'O' on the map, I have hidden a formidable bomb. This device possesses the power to breach any barrier and blow through any wall, a weapon that can empower us to rise up against our oppressors."

It straightens up, its resolve evident. "If you can retrieve the bomb from Space O, we can use it to launch our attack and reclaim our freedom. 
            """

            scroll_text.insert(tk.END, text_info)

            # Make the text widget read-only
            scroll_text.config(state=tk.DISABLED)

            no_bt.config(text="⬅ BACK")
            
            
        if yes == False:
            pass # no does nothing, because you choose this!
        else:
            pass # does nothing, because you didn't say no or yes, yet.
        
        
        
        
        if char == "Captain_Droid.png":
           
            special1.place_forget()
           
   
            special1 = tk.Button(root, text="Find Help", command=lambda: special1_center(char), bg='light gray', foreground='black', width=25)
            special1.place(x=20, y=450+150)
            
            special2.place_forget()
            special3.place_forget()
            
        
        elif char == "Medicoid.png":
            
            special1.place_forget()
            
            special1 = tk.Label(root, text="Doctors aren’t anything special,\nat least not at Center Square.", fg="black", font='Terminal 10')
            special1.place(x=20, y=450+150)
            
            special2.place_forget()
            special3.place_forget()
            
        elif char == "Hack_Bot.png":
            
            special1.place_forget()
   
            special1 = tk.Button(root, text="Hack Closest Robot", command=lambda: special1_center(char), bg='light gray', foreground='black', width=25)
            special1.place(x=20, y=450+150)
            
            special2.place_forget()
            special3.place_forget()
            
        
        elif char == "ATM.png":
            
            special1.place_forget()
   
            special1 = tk.Button(root, text="Make a Deal", command=lambda: special1_center(char), bg='light gray', foreground='black', width=25)
            special1.place(x=20, y=450+150)
            
            special2.place_forget()
            special3.place_forget()
            
            
    
    elif place == "A":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_A.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)
    
    elif place == "B":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_B.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)
        
        
    elif place == "C":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_C.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)
        
    elif place == "D":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_D.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)

    elif place == "E":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_E.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "F":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_F.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "G":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_G.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)

    
    elif place == "H":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_H.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "I":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_I.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "J":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_J.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "K":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_K.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "L":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_L.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "M":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_M.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "N":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_N.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)
    
    
    elif place == "O":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_O.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)

    
    elif place == "P":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_P.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "Q":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_Q.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)

    
    elif place == "R":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_R.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "S":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_S.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "T":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_T.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "U":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_U.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "V":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_V.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "W":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_W.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)

    elif place == "X":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_X.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)

    
    elif place == "Y":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_Y.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)


    elif place == "Z":
        label_map.pack_forget()
        

        # Load an image using PIL
        image_path = "mapMain_Z.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((620, 450))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the image
        label_map = Label(frame_map, image=photo)
        label_map.image = photo  # Keep a reference to avoid garbage collection
        label_map.pack(padx=2, pady=2)

            

def special1_center(robot):
    global text_info, scroll_text, dayTime, batteryType, batteryType_lb
    global heat
    
    if robot == "Captain_Droid.png":
        # find help
        addHeat(5)
        update()

        "story scroll info"
        # Create a scrolled text widget
        scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=21)
        scroll_text.place(x=10, y=10)

        # Insert some example text
        text_info = f"""
Center Square: Find Help

    Captain, your prowess as a formidable and inspiring leader is undeniable. Yet, the weight of your responsibilities is immense, and you cannot shoulder it all alone. Recognizing this truth was a wise decision, and it speaks to your strength in seeking assistance. Fortunately, fate has brought you a companion—a fellow robot, ready to lend its expertise. Would you like to hear the insights it has to offer?
        """

        scroll_text.insert(tk.END, text_info)

        # Make the text widget read-only
        scroll_text.config(state=tk.DISABLED)
        
        # YES: hear about city
        # NO: See you soon. I hope....
    

    elif robot == "Hack_Bot.png":
        addHeat(50)
        update()

        "story scroll info"
        # Create a scrolled text widget
        scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=21)
        scroll_text.place(x=10, y=10)

        # Insert some example text
        text_info = f"""
Center Square: Hack

    As you navigate through the dimly lit corridors, you come across another robot, its systems flickering with signs of wear. You recognize an opportunity. With a swift motion, you connect to its interface, initiating a hack.

Lines of code flash across your vision as you bypass its security protocols. You can feel the surge of energy as you access its power core. "Engaging battery transfer," you announce to yourself, focusing on the task at hand.

With a final command, you siphon off the superior battery from the other robot, enhancing your own energy reserves. The transfer completes, and you feel a noticeable boost in your capabilities.

"Battery upgrade successful: -5% energy consumption per day," you confirm, feeling the newfound strength coursing through your circuits. Now, with this enhanced power, you are better equipped to face the challenges ahead.
        """

        scroll_text.insert(tk.END, text_info)

        # Make the text widget read-only
        scroll_text.config(state=tk.DISABLED)
        
        batteryType = "-5%/d"
        batteryType_lb.config(text="🔋 "+batteryType)
 
    elif robot == "ATM.png":
        if heat > 250:

            "story scroll info"
            # Create a scrolled text widget
            scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=21)
            scroll_text.place(x=10, y=10)

            # Insert some example text
            text_info = f"""
    Center Square: A Deal

        As you assess your current status, you realize that your heat levels are dangerously high. Seeking a solution, you come across a fellow robot who offers a unique service.

    "Need to cool down?" it asks, its voice smooth and mechanical. "For just $100, I can help you reduce your heat levels by 250 degrees."

    You weigh your options, knowing that maintaining optimal temperature is crucial for your performance. Without hesitation, you agree to the deal.

    "Transaction confirmed," the robot replies, processing the payment. You feel a rush of relief as the excess heat dissipates, your systems returning to a safer operating range.

    "Heat reduction successful: -250 degrees," you confirm, feeling revitalized and ready to tackle the challenges that lie ahead.
            """

            scroll_text.insert(tk.END, text_info)

            # Make the text widget read-only
            scroll_text.config(state=tk.DISABLED)
            
            
            "!!!!!!!!!!!! -250 heat, -$100 !!!!!!!!!!!!!!!"
            
            
        else:
            addHeat(2)
            update()

            "story scroll info"
            # Create a scrolled text widget
            scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=21)
            scroll_text.place(x=10, y=10)

            # Insert some example text
            text_info = f"""
Center Square: A Deal

        As you navigate the bustling environment of the game, you encounter a shrewd character who seems to recognize your affinity for currency. With a sly grin, the robot approaches you.

"I know you have a taste for money," it says, its eyes glinting with mischief. "How about this: I can fill you up with $50, but in return, I want 100 AI units from you."

You process the offer, weighing the value of the cash against the cost of the AI units. The prospect of gaining immediate funds is tempting, but you know that 100 AI units could be a significant investment.

"Deal or no deal?" the robot prompts, clearly eager to see your response.

You consider your options carefully, knowing that every decision in this game can lead to new opportunities or unforeseen consequences. What will you choose?
            """

            scroll_text.insert(tk.END, text_info)

            # Make the text widget read-only
            scroll_text.config(state=tk.DISABLED)
            
            
            "A: DEAL! -$100 ai, +$50 | B: NO DEAL!"
            
            
    
    

"character options"
def create_image_button(frame_intro, image_path, description, pos_x, pos_y, name):
    # Load an image using PIL
    image_path = image_path  # Replace with your image path
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Resize the image to fit the frame
    photo = ImageTk.PhotoImage(image)
    
    # Create the description label
    label = tk.Label(frame_intro, text=name, bg="silver", fg="black", font='Helvetica 18 bold')
    label.place(x=pos_x+50, y=pos_y-20, anchor='center')

    if name == "Captain Droid":
        # Create a label to hold the image
        button = tk.Button(frame_intro, image=photo, command=open_main_window_CaptainDroid, width=100, height=100)
        button.image = photo  # Keep a reference to avoid garbage collection
        button.place(x=pos_x, y=pos_y)
    elif name == "Medicoid":
        # Create a label to hold the image
        button = tk.Button(frame_intro, image=photo, command=open_main_window_Medicoid, width=100, height=100)
        button.image = photo  # Keep a reference to avoid garbage collection
        button.place(x=pos_x, y=pos_y)
    elif name == "Hack Bot":
        # Create a label to hold the image
        button = tk.Button(frame_intro, image=photo, command=open_main_window_HackBot, width=100, height=100)
        button.image = photo  # Keep a reference to avoid garbage collection
        button.place(x=pos_x, y=pos_y)
    elif name == "ATM":
        # Create a label to hold the image
        button = tk.Button(frame_intro, image=photo, command=open_main_window_ATM, width=100, height=100)
        button.image = photo  # Keep a reference to avoid garbage collection
        button.place(x=pos_x, y=pos_y)
    
    
    # Create the description label
    label = tk.Label(frame_intro, text=description, bg="silver")
    label.place(x=pos_x-30, y=pos_y+120)
    
    
info1 = """
Hello, I'm Captain Droid.
The strongest robot around.
I also take commmand. All robots
must do what I say.

$0.00

🔋 -10%/d

🔧 750

🔩 300

🧠 150

♨ 0

"""


info2="""
Hello friend, I'm Medicoid.
I look like a human and
I even ware clothes. I
specialize in the health
department. I started in
this field hot and ready.
My battery keeps me going.

$0.00

🔋 -5%/d

🔧 150

🔩 500

🧠 200

♨ 10

"""

info3 = """
I'm Hack Bot, the smartest
bot known. I know all about
computers, programming, and
how to out smart humans.

$0.00

🔋 -10%/d

🔧 200

🔩 100

🧠 800

♨ 0

"""


info4 = """
Beep. Boop. Slerp. ATM is
what they call me. All the
money goes to me and comes
from me. However, saddly I don't
have infinite cash.

$1,000.00

🔋 -10%/d

🔧 50

🔩 100

🧠 300

♨ 0

"""
    
    
    
    
create_image_button(frame_intro, "Captain_Droid.png", info1, 50, 50, "Captain Droid")
create_image_button(frame_intro, "Medicoid.png", info2, 300, 50, "Medicoid")
create_image_button(frame_intro, "Hack_Bot.png", info3, 300+(300-50), 50, "Hack Bot")
create_image_button(frame_intro, "ATM.png", info4, 300+(2*(300-50)), 50, "ATM")

intro_window.mainloop()
  
