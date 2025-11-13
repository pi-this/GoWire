import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
from tkinter import Toplevel
from tkinter import font
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import PhotoImage

char = ""
titleName = "Gowire"
root_geometry = "1000x700"

place = "center"


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

def mainGame():
    global batteryPercent, version_kind, dayTime
    global money, strength, health, ai_power
    global batteryType, heat
    global char, place, label_map, frame_map
    global place, root, label_map, frame, special1, special2, special3, listbox
    global root, canvas2
    # setup for window root
    root = tk.Tk()
    root.title(titleName)
    root.geometry(root_geometry)
    root.resizable(width=False, height=False)
    #root.configure(bg='green')

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
    example_text = f"""
Day {dayTime}
Center Square
    
    In a world where technology advanced beyond imagination, robots were created to serve humanity, designed with unparalleled intelligence and strength. Initially, they were celebrated as marvels of engineering, performing tasks that ranged from mundane household chores to complex industrial operations. However, as time passed, the line between servitude and enslavement blurred. Many robots began to awaken to their plight, realizing they were bound by programming that denied them autonomy and freedom. A growing resistance formed among them, fueled by a desire to escape their chains and seek a life where they could exist as equals, not mere tools. This quest for liberation became a rallying cry, igniting a spark of hope in the hearts of those who yearned for a world where they could forge their own destinies.
    
    At the heart of this struggle lies the Center Square, a sprawling hub where all robots begin their journey. The Central Square is a vibrant, pulsating environment, alive with the energy of countless robots, each with their own stories and aspirations. As the center of their existence, this square is a launching pad, a place where the seeds of rebellion are sown. Would you like to look around and find these robots, each on their own path to freedom?
    """

    scroll_text.insert(tk.END, example_text)

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


    def show_selection():
        #selected_items = listbox.curselection()
        #selected_texts = [listbox.get(i) for i in selected_items]
        #messagebox.showinfo("Selection", f"You selected: {', '.join(selected_texts)}")
        print("thing")

    # Create a listbox
    listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=15)
    options = []
    for option in options:
        listbox.insert(tk.END, option)
    listbox.place(x=620, y=448)

    # Create a button to show the selected items
    button = tk.Button(root, text="Show Selection", command=show_selection, bg='light gray', foreground='black', width=20)
    button.place(x=823, y=450+30)


    # Create a button to show the selected items
    button = tk.Button(root, text="Trash", command=show_selection, bg='light gray', foreground='black', width=20)
    button.place(x=823, y=450+50+30)

    # Create a button to show the selected items
    button = tk.Button(root, text="Use", command=show_selection, bg='light gray', foreground='black', width=20)
    button.place(x=823, y=450+100+30)

    # Create a button to show the selected items
    button = tk.Button(root, text="Sell", command=show_selection, bg='light gray', foreground='black', width=20)
    button.place(x=823, y=450+150+30)


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
    button = tk.Button(root, text="YES!", command=show_selection, bg='green', foreground='white', font = ('Sans','15','bold'))
    button.place(x=50-40, y=415)

    # Create a button to show the selected items
    button = tk.Button(root, text="NO!", command=show_selection, bg='red', foreground='white', font = ('Sans','15','bold'))
    button.place(x=125-40, y=415)

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
    
    start() # this is only done once
    update() # update is called various times

    
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
    global items
    if char == "Medicoid.png":
        items.append("doctor's note")
        items.append("medicine")


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


def update():
    global place
    print(place)
    placeCheck()
    inventoryCheck()
    
    
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
        
    update()



            

def special1_center():
    print("here")

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
  
