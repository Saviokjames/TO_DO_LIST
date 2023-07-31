import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("To-Do List Maker")

# Create a listbox to store the tasks
listbox = tk.Listbox(window)
listbox.pack()

def add_task():# Create a function to add a task to the listbox
  task = input("Enter a task: ")
  listbox.insert(tk.END, task)

# Create a button to add a task
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()




# Run the main loop
window.mainloop()
