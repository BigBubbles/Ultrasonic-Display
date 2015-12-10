from Tkinter import *
import sys
from ping import Ping

def callback():
    print("called the callback!")

#define function for 1 sensor set up
def Sensor1():
    #delete print in final code
    print("1 sensor")

#define function for 2 sensor set up
def Sensor2():
    #delete print in final code
    print("2 sensors")

#define function for 3 sensor set up
def Sensor3():
    #delete print in final code
    print("3 sensors")

#define function for 4 sensor set up
def Sensor4():
    #delete print in final code
    print("4 sensors")
    #draw the circle that indicates the sensor
    #w.create_
    #call gridlayout
    GridLayout()
    

#define the dislog box for exit confirmation
def Exit():
    result = messagebox.askyesno("Warning", "Do you wish to exit the system?")
    if result == True:
        exit()

#define function to draw grid
def GridLayout():
    x = 10
    for i in range(60, 10):
        w.create_line(0,x, 600,x)
        x +=10

#create the main gui window
Gui = Tk()
Gui.geometry('1000x500')
Gui.title("Ultrasonic Sensor Ping Representation")


# create a menu for main window
menu = Menu(Gui)
Gui.config(menu=menu)
#file menu
FileM = Menu(menu)
menu.add_cascade(label="File", menu=FileM)
FileM.add_command(label="Exit", command=Exit)
#sensor menu
SensorM = Menu(menu)
menu.add_cascade(label="Sensors", menu=SensorM)
SensorM.add_command(label="One Sensor", command=Sensor1)
SensorM.add_command(label="Two Sensors", command=Sensor2)
SensorM.add_command(label="Three Sensors", command=Sensor3)
SensorM.add_command(label="Four Sensors", command=Sensor4)
#help menu
HelpM = Menu(menu)
menu.add_cascade(label="Help", menu=HelpM)
HelpM.add_command(label = "Help", command = callback)
HelpM.add_command(label="About", command=callback)

#create start button
S = Button(Gui, text="Start", justify=CENTER, command=callback)
S.config(height=2, width=10)
S.pack()

#create the canvas to draw on
w = Canvas(Gui, width=600, height=400)
w.pack()

#draw arc
#w.create_arc(start = 362.5, extent = 15, style = ARC, )

#draw line
x = 10
w.create_line(0,20, 600,20)
w.pack

mainloop()
