import webbrowser
import time

total_breaks = 3
break_count = 0
print("This program started om " +time.ctime())
while (break_count < total_breaks ):
    time.sleep(5) #delay 5 second
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=OG2eGVt6v2o")
    break_count = break_count + 1
