# encoding="utf-8"
from gtts import gTTS
import os
import turtle
import speech_recognition as sr
from tkinter import *

root = Tk()
direction1 = Label(root, text = "Paste text in any language:")
direction1.grid(row = 0)
#direction1.grid(row = 0, column = 0)
entry = Entry(root, width = 70)
entry.grid(row = 0, column = 1)
entry.focus_set()
text = "El Cruz Azul Fútbol Club" #Default text
langFrequencyDiff = []
def callback():
    text = entry.get()
    if not text:
        print("Please type in some text!")
    else:
        file = open('Text.txt', 'w', encoding="utf-8")
        file.write(text)
def run():
    # Create array of frequencies of letters for each language
    frequency = "Letter Frequencies.csv"
    letters = []
    for line in open(frequency, encoding="utf-8"):
        tokens = line.split(" ")
        letters.append(tokens)
    # Create an array of frequencies of each letter for a text
    with open("Text.txt", "r", encoding="utf-8") as file:
        text = file.read().replace('\n', '')
    if not text:
        print("Please type some text first!")
    else:
        cnt = 0
        letterLoop = 0
        textFrequencies = []
        words = text.split(" ")
        letterCount = 0
        for i in words:
            for j in i:
                letterCount += 1
        tempLetters = letters[0][0].split(",")
        del tempLetters[0]
        for i in range(0, len(tempLetters)):
            for j in text:
                if j == tempLetters[i]:
                    cnt += 1
            textFrequencies.append((cnt / letterCount) * 100)
            letterLoop += 1
            cnt = 0
        # Text frequencies is correct (tested)
        # Create an array that stores the difference of frequencies of each letter between the text and wiki values
        langFrequencyDiff = []  # Frequency difference of all letters for each language
        frequencyDiff = 0.0
        for x in range(1, 16):
            for i in range(0, 84):  # loops through columns of data values on wiki
                # temp = letters[i][0].split(",") # Temporary array of frequencies of certain letter for each language
                tempFrequencies = letters[x][0].split(",")
                del tempFrequencies[0]
                frequencyDiff += abs(float(textFrequencies[i]) - float(tempFrequencies[i]) * 100)
            langFrequencyDiff.append(frequencyDiff)
            frequencyDiff = 0
        test = letters[1][0].split(",")
        del test[0]
        num = 0.0
        for i in range(0, len(test)):
            if i <= 25:
                num += abs(0.03846 - float(test[i]))
            else:
                num += 0
        # Get the index that stores the smallest frequency difference -> get language
        index = 0
        for i in range(0, len(langFrequencyDiff)):
            if langFrequencyDiff[i] < langFrequencyDiff[index]:
                index = i
        lang = letters[index + 1][0].split(",")[0]
        tot = 0
        for diff in langFrequencyDiff:
            tot += diff
        if tot == 0:
            lang = "Chinese"
        print("The text is written in " + lang)
        lang = "The text is written in " + lang
        output = gTTS(text=lang, lang='en', slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")
        root.destroy()
        david = turtle.Turtle()
        david.hideturtle()
        david.penup()
        david.setx(-400)
        david.sety(0)
        david.pendown()
        david.speed(10)
        for i in range(0, len(langFrequencyDiff)):
            if index == i:
                david.fillcolor("Blue")
                david.begin_fill()
            david.forward(55)
            david.left(90)
            david.forward(langFrequencyDiff[i] * 3)
            david.left(90)
            david.forward(55)
            david.left(90)
            david.forward(langFrequencyDiff[i] * 3)
            david.left(90)
            david.forward(55)
            david.end_fill()
        david.penup()
        for y in range(0, 101, 10):
            david.setx(-410)
            david.sety(0 + y * 2.8)
            david.write(str(y) + " ", True, align="center", font=("Arial", 10, "normal"))
        david.setx(-480)
        david.sety(50)
        david.write("Frequency Diff", True, align="center", font=("Arial", 12, "normal"))
        david.penup()
        i = 0
        for x in range(-370,455,55):
            david.setx(x)
            david.sety(-15)
            temp = letters[i + 1][0].split(",")[0]
            david.write(temp, True, align="center", font=("Arial", 8, "normal"))
            i += 1
        david.sety(-45)
        david.setx(42.5)
        david.write("Languages", True, align="center", font=("Arial", 12, "normal"))
        turtle.done()
def talk():
    if speak["text"] == "Text to Speech":
        speak["text"] = "Pause"
    elif speak["text"] == "Pause":
        speak["text"] = "Text to Speech"
    file = open('Text.txt', 'r', encoding="utf-8")
    sentence = file.read()
    output = gTTS(text=sentence, lang='en', slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")
def end():
    root.destroy()
enter = Button(root, text = "OK", width = 12, command = callback)
enter.grid(row = 1)
detect = Button(root, text = "Detect Language", width = 12, command = run)
detect.grid(row = 2)
speak = Button(root, text = "Text to Speech", width = 12, command = talk)
speak.grid(row = 3)
exit = Button(root, text = "Quit", width = 12, command = end)
exit.grid(row = 4)
root.mainloop()