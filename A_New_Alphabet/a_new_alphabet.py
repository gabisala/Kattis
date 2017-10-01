
import sys

# Read data
text = sys.stdin.readline().lower()

# Translation dictionary letters: new alphabet
translation = {
    "a": "@", "b": "8", "c": "(", "d": "|)", "e": "3", "f": "#", "g": "6", "h": "[-]", "i": "|", "j": "_|",
    "k": "|<", "l": "1", "m": "[]\/[]", "n": "[]\[]", "o": "0", "p": "|D", "q": "(,)", "r": "|Z", "s": "$",
    "t": "']['", "u": "|_|", "v": "\/", "w": "\/\/", "x": "}{", "y": "`/", "z": "2"
}

# # Output the input text with each letter (lowercase and uppercase) translated into its New Alphabet counterpart
translated = [translation[c] if 97 <= ord(c) <= 122 else c for c in text]
print ''.join(translated)
