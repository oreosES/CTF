import cv2
import numpy as np

code_dict =  {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
     '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
     '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
     '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
     '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
     '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
     '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
     '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
     '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
     '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
     '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'
     }

def decodeMorse(morseCode):
    for item in morseCode.split(' '):
        return code_dict.get(item)

cap = cv2.VideoCapture('secadmin.mov')
state = False
count = 0
area = 2500000
dot = 8
blank = 20
morseword = []
while cap.isOpened():
    ret,image = cap.read()
    B,G,R = cv2.split(image)
    _, Bthresh = cv2.threshold(B,0,5,cv2.THRESH_BINARY)
    _, Gthresh = cv2.threshold(G,245,255,cv2.THRESH_BINARY)
    _, Rthresh = cv2.threshold(R,0,5,cv2.THRESH_BINARY)
    bwise = cv2.bitwise_or(Bthresh,Gthresh)
    bwise = cv2.bitwise_or(Rthresh,bwise)
    eroded = cv2.erode(bwise, None, iterations=2)
    dilated = cv2.dilate(eroded, None, iterations=8)
    pixels = [item for sublist in dilated for item in sublist]
    vis = np.concatenate((G,dilated), axis=1)
    cv2.imshow('image',vis)
    sumarea = sum(pixels)
    if state == (sumarea > area):
        count = count+1
    else:
        if state == True:
            if count < dot:
                morseword.append("-")
                print("-"),
            else:
                morseword.append(".")
                print("."),
        else:
            if count > blank:
                print(decodeMorse(''.join(morseword)))
                morseword = []
                print(" ")
        state = sumarea > area
        count = 0
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
