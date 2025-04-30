import os # import the os library for os.system() method
import time # import the time library for time.sleep() method
from datetime import datetime 
"""importing the datetime module from datetime class, 
imported this way instead of just import datetime allows you to skip the prefix datetime.method() 
if you only did import datetime then you would have to do datetime.date.today() instead of date.today()"""

def set_background(image_path): # user defines a function set_background() with image_source parameter/arguments, the value passed to the function is replaced with whatever parameter when calling method
    try:
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}") # gsettings commands for bash
        os.system(f"gsettings set org.gnome.desktop.background picture-options 'stretched'") # gsettings commands for bash
        print(f"Background set to: {image_path}")
    except Exception as e:
        print(f"Error setting background: {e}")

if __name__ == "__main__":
    nighttime_image = "/home/ubuntu/Downloads/nighttimebackground.jpg"
    daytime_image = "/home/ubuntu/Downloads/daytimebackground.jpg"
    image_cycle = [daytime_image, nighttime_image]
    image_index = 0

    while True:
        now = datetime.now()
        current_minute = now.minute

        current_image_path = image_cycle[image_index % 2]
        set_background(current_image_path)
        image_index = (image_index + 1) % 2

        time.sleep(60) # tells the program to sleep for 60 seconds
