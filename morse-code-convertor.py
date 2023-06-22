"""
Author: Sergio Alejandro Villegas Ferruzca
Code: morse-code.py
Function: Given a string translate it into morse code using the International Morse Code convertion
Source: https://morsecode.world/international/morse2.html
"""

class Morse:
    # We define the translations as a dictionary
    convertion = {
        "a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".",
        "f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---",
        "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.", "o" : "---",
        "p" : ".--.", "q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-",
        "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--",
        "z" : "--..", "0" : "-----", "1" : ".----", "2" : "..---", "3" : "...--",
        "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..",
        "9" : "----.", "," : "--..--", "." : ".-.-.-", " " : " "
    }

    def convert(self, phrase):
        print("String: " + phrase)
        phrase_translated = ""
        for letter in phrase:
            morse = self.convertion.get(letter.lower())
            phrase_translated = phrase_translated + morse + " "
        return print("Morse: " + phrase_translated)

phrase = str(input("Enter a phrase to be translated into Morse code: "))

morse = Morse()
morse.convert(phrase)
