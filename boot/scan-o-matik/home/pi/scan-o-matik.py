import tkinter
import socket
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title("Scan-O-Matik")

scan = tkinter.StringVar()
hostname = socket.gethostname()

scanboxLabel = tkinter.Label(root, text = "Scan")
scanboxLabel.pack(side = "top")

scanboxEntry = tkinter.Entry(root, textvariable = scan)
scanboxEntry.pack(side = "top")

img = None

panel = tkinter.Label(root, image = img)
root.background_image = panel
#root.background.pack(fill = "both", expand = "yes")
panel.pack(side = "bottom", fill = "both", expand = "yes")

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

def imageload(event):
    global img
    #edit the line below to reflect the folder containing the folder named after the hostname you set
    path = "/mnt/share/mount/path/to/folder/%s/%s.PNG"%(hostname,scan.get())
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image = img)
    panel.image = img
    print(path) #print out the path for diagnostics

	
scanboxEntry.focus()
scanboxEntry.bind("<Tab>", imageload)

app=FullScreenApp(root)


root.mainloop()
