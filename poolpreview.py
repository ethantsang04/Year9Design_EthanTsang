from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup

lst = []
assists = []
goals = []
points = []
lstprint = ""
totalpts = 0
players = []
print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')

root = Tk()
root.geometry("800x600+0+900")
root.configure(background="light cyan")
root.title("Pool Preview")

if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
else:
    content = -99

def addPlayerToList(evt):
    global players
    name = variable.get()
    if players.count(name) > 0:
        return
    listbox.insert(END, name)
    for i in range(listbox.size()):
        players.append(listbox.get(i))

def createlistbox(value):
    var=listbox.get(ANCHOR)
    if var!=NONE:
        dTag=content.find(attrs={"csk":var})
        parent=dTag.findParent("tr")
        #player=str(parent.contents[1].text)
        team=str(parent.contents[3].text)
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
        points=int(parent.contents[8].text) 
        gamesplayed=int(parent.contents[5].text)
    listbox2 = Listbox(root, height=9)
    listbox2.place(x=200, y=405)
    listbox2.insert(END, 'Players Stats: ')
    listbox2.insert(END, 'Points: ' + str(points))
    listbox2.insert(END, 'Team: ' + team)
    listbox2.insert(END, 'Goals: ' + str(goals))
    listbox2.insert(END, 'Assists: ' + str(assists))
    listbox2.insert(END, 'Games Played: ' + str(gamesplayed))
    
def saveList():
    myfile = open("myplayers.txt", "w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayer.txt", "Players saved to disk")
  
def selected(evt):
    global player
    playerLabel.place(x=200, y=405)
    teamLabel.place(x=200, y=430)
    pointsLabel.place(x=200, y=455)
    goalsLabel.place(x=200, y=480)
    assistsLabel.place(x=200, y=505)
    
#draw canvas
can = Canvas(root, width=780, height=370)
can.grid(row=0, column=0,padx=10,pady=10)
image1= Image.open("Hockey.jpg")
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)

image1= Image.open("Hockey.jpg")
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)

can.create_oval(325, 25, 375, 75, fill="black", outline="#DDD", width=4)
can.create_line(250, 50, 320, 50, fill="#DDD", width=4)
can.create_line(275, 40, 320, 40, fill="#DDD", width=4)
can.create_line(275, 60, 320, 60, fill="#DDD", width=4)
can.create_text(350, 50, text="pool", fill="white")
can.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

instlab = Label(root,text="Add players:")
instlab.grid(row=1, column=0, sticky=NE, padx=10, pady=10)
instlab.configure(background="light cyan")

def switchPhoto(value):
    fullname = listbox.get(ACTIVE)
    full_list = fullname.split(",")
    first = full_list[1]
    last = full_list[0]
    filename = "headshots/" + last[0:5] + first[0:2] + "01.jpg"
    global photo2
    my_image = Image.open(filename.lower())
    photo2 = ImageTk.PhotoImage(my_image)
    can2.itemconfig(myimg2, image=photo2)

#listbox
listbox = Listbox(root,height=10)
listbox.grid(row=1,column =0, sticky=NW, padx=10, pady=10)
#listbox.bind('<<ListboxSelect>>', switchPhoto)
listbox.bind('<<ListboxSelect>>', createlistbox)

listbox = Listbox(root, width=23, height=20)
listbox.grid(row=1, column=0, sticky=NW, padx=10)
listbox.bind('<<ListboxSelect>>', switchPhoto)

def makeOptions():
    if content != -99:
        names = content.findAll(attrs={"data-stat" : "player"})
        playerlist = []
        for player in names:
            if(player != "None"):
                playerlist.append(player.get('csk'))
        return playerlist

#pulldown
OPTIONS = makeOptions()
variable = StringVar(root)
variable.set(OPTIONS[0])
w = OptionMenu(root, variable, *OPTIONS, command=addPlayerToList)
w.grid(row=1, column=0, sticky=NE, padx=10, pady=40)

def remplayers(value):
    var=listbox.get(ACTIVE)
    listbox.delete(listbox.index(ACTIVE))
    lst.remove(var)

listbox.bind('<Double-Button-1>',remplayers)

#button
savebutton = Button(root,text="Save", command=saveList)
savebutton.place(x=760, y=577)

can2 = Canvas(root, width=115, height=175)
image2 = Image.open("headshots/mcdavco01.jpg")
photo2 = ImageTk.PhotoImage(image2)
myimg2 = can2.create_image(0, 0, anchor=NW, image=photo2)
can2.configure(background="light cyan")
can2.place(x=500, y=400)

"""
def switchPhoto():
    global photo
    my_image = Image.open("headshots/crosbi01.jpg")
    photo = ImageTk.PhotoImage(my_image)
    can.itemconfig(myimg,image=photo)

#GUI
root=Tk()
root.geometry()
root.title("hockey pool")

can = Canvas(root, width=125, height=180)
image1 = Image.open("headshots/marnemi01.jpg")
photo = ImageTk.PhotoImage(image1)
myimg = can.create_image(0, 0, anchor=NW, image=photo)
can.pack()

button = Button(root, text="change photo", command=switchPhoto)
button.pack
"""

mainloop()
