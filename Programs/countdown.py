import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Time remaining: {timeformat}", end='\r')
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

# Input the countdown duration in seconds
seconds = int(input("Enter the countdown duration (in seconds): "))

# Start the countdown timer
countdown_timer(seconds)