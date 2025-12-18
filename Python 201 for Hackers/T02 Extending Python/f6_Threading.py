import threading
import time
from datetime import datetime

# --- 1. THE TARGET FUNCTION ---


def sleeper(i):
    """A simple task that simulates work using time.sleep()"""
    print(f"  [Task {i}] Started at {datetime.now().strftime('%H:%M:%S')}")
    time.sleep(i)
    print(f"  [Task {i}] Finished after {i}s delay")

# =================================================================
# CONCEPT 1: SEQUENTIAL EXECUTION (The "Normal" Way)
# =================================================================
# Without threads, the program waits for one function to finish
# completely before starting the next. Total time: 0+1+2+3 = 6 seconds.


def run_sequentially():
    print("\n--- Starting Sequential Run ---")
    start_time = time.time()
    for i in range(4):
        sleeper(i)
    print(f"Total Sequential Time: {time.time() - start_time:.2f} seconds")

# =================================================================
# CONCEPT 2: MULTI-THREADING (Parallelism-ish)
# =================================================================
# Threads allow tasks to run at the same time. The main program
# doesn't wait for them to finish unless we use .join().
# Total time: ~3 seconds (the duration of the longest task).


def run_threaded():
    print("\n--- Starting Threaded Run ---")
    start_time = time.time()
    threads = []

    for i in range(4):
        # Create a thread object pointing to the function and passing args
        t = threading.Thread(target=sleeper, args=(i,))
        threads.append(t)
        t.start()  # This kicks off the thread immediately

    # .join() tells the main program: "Wait here until this thread is done"
    for t in threads:
        t.join()

    print(f"Total Threaded Time: {time.time() - start_time:.2f} seconds")

# =================================================================
# CONCEPT 3: TIMERS (Scheduled Execution)
# =================================================================
# A Timer is a thread that waits for a specific interval before acting.


def run_timers():
    print("\n--- Starting Timers (Non-blocking) ---")
    # This schedules the function but continues executing the code below immediately
    threading.Timer(2, sleeper, [2]).start()
    print("Timer for 2s scheduled! Moving on...")


# =================================================================
# CONCEPT 4: INTER-THREAD COMMUNICATION (The Stop Flag)
# =================================================================
# Using a shared variable to let one thread control another.
stop_signal = False


def input_worker():
    """Thread that listens for user input (a blocking operation)"""
    global stop_signal
    while not stop_signal:
        cmd = input("Type 'stop' to end the counter: \n")
        if cmd.lower() == "stop":
            stop_signal = True
            print("Stop signal sent...")
            break


def counter_worker():
    """Thread that performs a background task until signaled to stop"""
    count = 0
    while not stop_signal:
        print(f"Counter: {count}")
        count += 1
        time.sleep(1)
    print("Counter thread safely exited.")


# --- EXECUTION ---
if __name__ == "__main__":
    # Uncomment these to see the difference in timing:
    # run_sequentially()
    # run_threaded()
    # run_timers()

    print("\n--- Starting Communication Demo ---")
    # We define the threads
    t1 = threading.Thread(target=input_worker)
    t2 = threading.Thread(target=counter_worker)

    # We start them
    t1.start()
    t2.start()

    # Wait for both to finish before closing the main program
    t1.join()
    t2.join()
    print("Main program exited.")
