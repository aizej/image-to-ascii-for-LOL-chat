from os import listdir
from PIL import Image
from cv2 import imread
from numpy import array
from PIL import Image, ImageOps 
from time import sleep
from pyautogui import typewrite
from keyboard import press_and_release



League_of_legends_ingame_chat = True    #set True if you want to type in lol chat or False if not
ALL_chat = True   #set to false for TEAM chat
reverse_colors = False
time_between_letters = 0.01   #in seconds
maximal_characters_per_line = 50   #for lol chat 
how_wide = 4    #4 is good 
time_till_start = 5 #in seconds           change tis to higher number if your loding time is higher




pics = listdir("pics")
max_lenght = maximal_characters_per_line
dir_to_pics = [f"pics/{i}"  for i in pics]
hhhh = ["l","."]
if reverse_colors:
    hhhh.reverse()
wide = how_wide


lenght = len(hhhh)
multi_int_to_char = 256/lenght

cv2_im = imread(dir_to_pics[0])
im = Image.open(dir_to_pics[0])


y,x,z = cv2_im.shape
multiplier = x/max_lenght
x = int(x/multiplier)
y = int((y/multiplier)/wide)

im = im.resize((x,y))
im = ImageOps.grayscale(im) 
img_as_numpy_array = array(im)


chat_mes_line_per_line = []
for line in img_as_numpy_array:
    chat_line = ""
    for i in line:
        chat_line +=  hhhh[int(i/multi_int_to_char)]
    chat_mes_line_per_line.append(chat_line)




sleep(time_till_start)


for chat_line in chat_mes_line_per_line:

    if League_of_legends_ingame_chat:
        if ALL_chat:
            press_and_release('shift+enter')   #pro LOL
        else:
            press_and_release('enter')

    typewrite(chat_line,interval=time_between_letters)
    typewrite("\n")


