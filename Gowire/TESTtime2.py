import tkinter as tk
import threading
import time

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Thread Interruption Example")
        
        self.is_running = False  # Flag to control the thread

        self.start_button = tk.Button(root, text="Start Thread", command=self.start_thread)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Thread", command=self.stop_thread)
        self.stop_button.pack(pady=10)

        self.label = tk.Label(root, text="Thread not running")
        self.label.pack(pady=10)

    def thread_function(self):
        self.is_running = True
        self.label.config(text="Thread is running")
        
        while self.is_running:
            # Simulate some work
            time.sleep(1)  # Sleep for 1 second
            print("Thread is working...")  # Replace with actual work

        self.label.config(text="Thread stopped")
        print("Thread has stopped.")

    def start_thread(self):
        if not self.is_running:  # Start the thread only if it's not already running
            self.thread = threading.Thread(target=self.thread_function)
            self.thread.start()

    def stop_thread(self):
        self.is_running = False  # Signal the thread to stop
        if hasattr(self, 'thread'):
            self.thread.join()  # Wait for the thread to finish

# Create the main application window
root = tk.Tk()
app = App(root)

# Start the Tkinter event loop
root.mainloop()
