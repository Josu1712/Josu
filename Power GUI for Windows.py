import tkinter,os,time
root = tkinter.Tk()
label = tkinter.Label(root, text="Power")
label.pack()
def shutdown():
    os.system("shutdown /s /t 5")
def restart():
    os.system("shutdown /r /t 5")
def close():
    exit()
button = tkinter.Button(root, text="Shutdown", command=shutdown)
button.pack()
button2 = tkinter.Button(root, text="Restart", command=restart)
button2.pack()
button3 = tkinter.Button(root, text="Exit",command=close)
button3.pack()
root.mainloop()