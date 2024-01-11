def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Translate each character to Morse code
    morse_code_list = []
    for word in text.upper().split():
        for i, char in enumerate(word):
            if char.isalpha():
                morse_code_list.append(morse_code_dict[char])
                if i < len(word) - 1 and word [i +1]. isalpha():
                    morse_code_list.append(" ") 
        morse_code_list.append("/")
    
    # Join Morse codes with spaces, and words with forward slashes
    morse_translation = " ".join(morse_code_list[:-1])

    return morse_translation

# Test cases
print(morse_translator("HELLO WORLD"))
print(morse_translator("Python"))
print(morse_translator("Morse Code"))
