import tkinter as tk

def send_info():
    # retrieve text from entry widget
    info = entry.get()
    # do something with info
    print(f"Info sent: {info}")
    # clear entry widget
    entry.delete(0, tk.END)

# create window
window = tk.Tk()
window.title("Send Info")

# create label
label = tk.Label(window, text="Enter info:")
label.pack()

# create entry widget
entry = tk.Entry(window)
entry.pack()

# create button
button = tk.Button(window, text="Send", command=send_info)
button.pack()

# start event loop
window.mainloop()
