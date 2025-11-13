import threading
import time

# Initialize the variable
counter = 0

# Define the function to increment the counter every minute
def increment_counter():
    global counter
    while True:
        time.sleep(2)  # Wait for 60 seconds
        counter += 1
        print(f"Counter incremented to: {counter}")

# Start the background thread
thread = threading.Thread(target=increment_counter)
thread.daemon = True  # This ensures the thread will exit when the main program exits
thread.start()

# Your main code continues here
for i in range(10):
    print(f"Main code running: {i}")
    time.sleep(1)  # Simulate some work in the main code

print("Main code finished.")
