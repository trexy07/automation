import pyautogui, random, requests, time 
screenWidth, screenHeight = pyautogui.size()
print(screenWidth,screenHeight)
# pyautogui.moveTo(200, 1750)
# pyautogui.click()  

# pyautogui.click('search') # wnats image file




response = requests.get(
    'https://www.mit.edu/~ecprice/wordlist.10000',
    timeout=10)

# Here we are decoding the response and storing it in a variable for further use 
randomWords = response.content.decode('utf-8')
# Getting a list of all the words without spaces basically 
words = randomWords.splitlines()
# Choosing a random word from the list every time
# random_word = random.choice(words)

# open edge
pyautogui.click(200, 1750)  
pyautogui.write('firefox\n', interval=.25)
time.sleep(1)

# start e's
pyautogui.hotkey('ctrl', 'shift', 'm')
time.sleep(1)
pyautogui.write('bing.com\n', interval=0.25)


pyautogui.click(1440, 400)



# more ees
for i in range(10//5):
    word=random.choice(words)
    pyautogui.write(f'{word}\n', interval=0.25)

    print(i,word)

    pyautogui.moveTo(1440+random.randrange(-100,40), 300+random.randrange(-10,11))  
    pyautogui.doubleClick() 
    # double click is wrong
    time.sleep(random.randrange(15,20)+random.randrange(100)/100)
pyautogui.alert('done!')








