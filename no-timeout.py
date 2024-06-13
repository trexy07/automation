# clicks back to a window every x minutes 
# to stop the aplication from timing out due to inactivity
import pyautogui, time 

timeout=3 #minutes
total_time=60 # minutes

for i in range(total_time//timeout):
    start=pyautogui.position()
    pyautogui.moveTo(720, 900)  
    pyautogui.click()
    pyautogui.moveTo(800, 920)
    pyautogui.moveTo(start)
    time.sleep(60*timeout)
pyautogui.alert("done")





