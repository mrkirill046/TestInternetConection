# Imports
import tkinter
import speedtest

# Methods
def test():
    download = speedtest.Speedtest().download()
    upload = speedtest.Speedtest().upload()

    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    download_label.config(text="Download speed:\n" + str(download_speed) + " Mbit/s")
    upload_label.config(text="Upload speed:\n" + str(upload_speed) + " Mbit/s")

# Variables
root = tkinter.Tk()

# Code
root.title("Speed Internet Testing")
root.geometry("300x400")

button = tkinter.Button(root, text="Press Start", font=40, command=test)
button.pack(side=tkinter.BOTTOM, pady=40)

download_label = tkinter.Label(root, text="Download speed:\n-", font=35)
download_label.pack(pady=(50, 0))
upload_label = tkinter.Label(root, text="Upload speed:\n-", font=35)
upload_label.pack(pady=(10, 0))

root.mainloop()
