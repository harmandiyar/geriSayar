import time

def countdown(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1

    print("Countdown finished!")

if __name__ == "__main__":
    try:
        duration = int(input("Enter countdown duration in seconsds: "))
        countdown(duration)
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")