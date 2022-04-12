import time
from pygame import mixer


def pause_play_exit(file_name, what_are_you_doing):       # This is the function which stops and plays the audio and also save the details about what you have done.
    print("Press 'p' to pause, 'r' to Resume ")
    print("'e' to exit the program ")
    query = input()
    if query == "p":
        mixer.music.pause()
    elif query == "r":
        mixer.music.unpause()
    elif query == "e":
        water = open(file_name, "a")
        water.write(f"{time.asctime()}  this time you have {what_are_you_doing}. \n")
        mixer.music.stop()


def repeat():
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)     # This will play the audio for infinite number of times, until the user press 'e' on the keyboard to end the audio.

    while True:
        pause_play_exit("Drinking_water.txt", "Drunk water")    # This is for playing water audio, and for stopping it, and saving it in a file.
        break

    mixer.init()
    mixer.music.load("activity.mp3")

    mixer.music.set_volume(0.7)
    mixer.music.play(-1)    # This will play the audio for infinite number of times, until the user press 'e' on the keyboard to end the audio.
    while True:

        pause_play_exit("Physical_activities.txt", "done some Physical Exercise")     # This is for playing water audio, and for stopping it, and saving it in a file.
        break
    time.sleep(9)      # This sleep the program for 9 seconds we can change the sleeping time but be sure that you give the time in seconds.

    mixer.init()
    mixer.music.load("time_to_exercise.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)    # This will play the audio for infinite number of times, until the user press 'e' on the keyboard to end the audio.

    while True:
        pause_play_exit("Eye_exercise.txt", "done some Eye exercise")      # This is for playing water audio, and for stopping it, and saving it in a file.
        break
    time.sleep(10)    # This sleep the program for 9 seconds we can change the sleeping time but be sure that you give the time in seconds.


def again():       # This will create an infinite loop, which will run the program endlessly.
    repeat()
    return again()


again()
