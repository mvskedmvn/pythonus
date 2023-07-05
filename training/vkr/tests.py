import tkinter
 
foregroundColor = "#eee"
backgroundColor = "#555"
 
root = tkinter.Tk()
root.configure(background= backgroundColor)
root.title("Launcher")
root.geometry("600x400")
 
version = tkinter.Label(text = "Engine 5.1 - Launcher (0.01)", fg = foregroundColor, bg = backgroundColor)
version.place(relx = .2, rely = .1, relwidth = 0.6, relheight = 0.1)
 
root.mainloop()