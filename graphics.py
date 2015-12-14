from tkinter import *
import sys
import time
from ping import Ping

enable=False

def callback():
    global enable
    print(enable)
    if(enable):
        for x in range(0,4):
            distance=sensors[x].distance()
            setLines(x,distance)
            w.itemconfigure("s%d"%(x+1),text="%-8d cm" % round(distance))
    Gui.after(500,callback)
    """d1=round(sensor1.distance())
    setLines(0,d1)
    w.itemconfigure("s1",text="%-8d cm" % round(d1))
    print("S1 called the callback!")
    w.itemconfigure("s2",text="%-8d cm" % round(sensor2.distance()))
    print("S2 called the callback!")
    w.itemconfigure("s3",text="%-8d cm" % round(sensor3.distance()))
    print("S3 called the callback!")
    w.itemconfigure("s4",text="%-8d cm" % round(sensor4.distance()))
    print("S4 called the callback!")"""
def stop():
    global enable
    enable=False
    print("Stop"+str(enable))
    for x in range(0,4):
        setLines(x,0)
def start():
    global enable
    enable=True
    print("Start"+str(enable))
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
def setLines(sensor,distance):
    #tk.NORMAL
    #w.item.configure("",state=tk.HIDDEN)    
    if distance <= 50:
        line=0
    elif(distance>50 and distance<=100):
        line=1    
    elif(distance>100 and distance<=150):
        line=2
    elif(distance>150 and distance<=200):
        line=3
    elif(distance>200 and distance<=250):
        line=4
    elif(distance>250 and distance<=300):
        line=5
    elif(distance>300 and distance<=350):
        line=6
    elif(distance>350):
        line=7
    for x in range(0,8,1):
        if(x<=line):
            w.itemconfigure("line%d%d"%(sensor,x),state=NORMAL)
        else:
            w.itemconfigure("line%d%d"%(sensor,x),state=HIDDEN)
    
 
def drawSensorLine():
    colors=["RED","YELLOW","BLUE","BLUE","BLUE","GREEN","GREEN","GREEN"]
    x = 200
    y1 = 110
    y2 = 130
    distances = [200,300,400,500,600,700,800,900]
    for sensor in range(0,4,1):
        for line in range(0,8,1):
            w.create_line(distances[line],y1-10*line,distances[line],y2+10*line,fill=colors[line],width=3,tags="line%d%d"%(sensor,line))
        y1+=150
        y2+=150
    
#create the main gui window
Gui = Tk()
Gui.geometry('1000x800')
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
S = Button(Gui, text="Start", justify=CENTER, command=start)
S.config(height=2, width=10)
S.pack()
S = Button(Gui, text="Stop", justify=CENTER, command=stop)
S.config(height=2, width=10)
S.pack()
#create the canvas to draw on
w = Canvas(Gui, width=1000, height=700)
w.pack()

#Sensor 1 labels
w.create_text(35,50,text="Sensor 1: ")
w.pack()

w.create_text(120,50,text="testing",tag="s1")
w.pack()

w.create_line(70,90,70,150)
w.create_line(40,120,100,120)

#Sensor 2 labels
w.create_text(35,200,text="Sensor 2: ")
w.pack()

w.create_text(120,200,text="testing",tag="s2")
w.pack()

w.create_line(70,240,70,300)
w.create_line(40,270,100,270)
#Sensor 3 labels
w.create_text(35,350,text="Sensor 3: ")
w.pack()

w.create_text(120,350,text="testing",tag="s3")
w.pack()

w.create_line(70,390,70,450)
w.create_line(40,420,100,420)

#Sensor 4 labels
w.create_text(35,500,text="Sensor 4: ")
w.pack()

w.create_text(120,500,text="testing",tag="s4")
w.pack()

w.create_line(70,540,70,600)
w.create_line(40,570,100,570)

"""
sensor1 = Ping(17, 21)
sensor2 = Ping(18, 22)
sensor3 = Ping(19, 23)
sensor4 = Ping(20, 24)"""
sensors = [Ping(17, 21),Ping(18, 22),Ping(19, 23),Ping(20, 24)]

colors=["RED","YELLOW","BLUE","BLUE","BLUE","GREEN","GREEN","GREEN"]
x = 200
y1 = 110
y2 = 130
distances = [200,300,400,500,600,700,800,900]#range(200,900,100)
"""for x in range(200,900,100):
#    w.create_line(x, y1, x, y2,fill=colors[3])
#    y1-=10
#    y2+=10
distance1=sensor1.distance()
print(distance1)
print(distances)

distance1=sensor1.distance()

if distance1 <= 50:
        w.create_line(distances[0],y1,distances[0],y2,fill=colors[0])
elif(distance1>50 and distance1<=100):
        y1-=10
        y2+=10
        w.create_line(distances[1],y1,distances[1],y2,fill=colors[1])
elif(distance1>100 and distance1<=150):
        w.create_line(distances[1],y1,distances[1],y2,fill=colors[2])
        y1-=10
        y2+=10
        w.create_line(distances[2],y1,distances[2],y2,fill=colors[2])
elif(distance1>150 and distance1<=200):
        w.create_line(distances[1],y1,distances[1],y2,fill=colors[3])
        y1-=10
        y2+=10
        w.create_line(distances[2],y1,distances[2],y2,fill=colors[3])
        y1-=10
        y2+=10
        w.create_line(distances[3],y1,distances[3],y2,fill=colors[3])
elif(distance1>200 and distance1<=250):
        w.create_line(distances[4],y1,distances[4],y2,fill=colors[4])
        y1-=10
        y2+=10
elif(distance1>250 and distance1<=300):
        w.create_line(distances[5],y1,distances[5],y2,fill=colors[5])
        y1-=10
        y2+=10
elif(distance1>300 and distance1<=350):
        w.create_line(distances[6],y1,distances[6],y2,fill=colors[6])
        y1-=10
        y2+=10
elif(distance1>350):
        print("7")
        w.create_line(distances[7],y1,distances[7],y2,fill=colors[7])
        y1-=10
        y2+=10
"""
    
#draw arc
#w.create_arc(start = 362.5, extent = 15, style = ARC, )
drawSensorLine()
#Gui.after(1,callback)
callback()
Gui.mainloop()

