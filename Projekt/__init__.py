#zapninani programu
def start():
    once = True
    morse()

def morse():
    #inicializace pouze jednou na zacatku
    if (once):
        morseCode = { 'A':'.-', 'B':'-...',
                            'C':'-.-.', 'D':'-..', 'E':'.',
                            'F':'..-.', 'G':'--.', 'H':'....',
                            'I':'..', 'J':'.---', 'K':'-.-',
                            'L':'.-..', 'M':'--', 'N':'-.',
                            'O':'---', 'P':'.--.', 'Q':'--.-',
                            'R':'.-.', 'S':'...', 'T':'-',
                            'U':'..-', 'V':'...-', 'W':'.--',
                            'X':'-..-', 'Y':'-.--', 'Z':'--..',
                            '1':'.----', '2':'..---', '3':'...--',
                            '4':'....-', '5':'.....', '6':'-....',
                            '7':'--...', '8':'---..', '9':'----.',
                            '0':'-----', ', ':'--..--', '.':'.-.-.-',
                            '?':'..--..', '/':'-..-.', '-':'-....-',
                            '(':'-.--.', ')':'-.--.-'}
        yep = input("If you want to see a summary of all available characters, press Y and Enter:")
        yep = yep.upper
        once = False
        if (yep == "Y"):#pokud y, vypise mozne znaky
            print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ( )")
            input("Press Enter to continue..")

    decision = input("For encoding morse press 1, For decoding morse press 2, for exit press 3:") #co chces delat / dekodovat / zakodovat
    if (decision == "3"):
        print("Goodbye")
    else:
        if (decision == "1"): #dekodovani
            text = input("Enter text to encode:")
            encode(text)
            input("Press Enter to continue")
            morse()
        elif (decision == "2"): #rozkodovani
            text = input("Enter morse code to decode, write / after every letter, write // after every word:")
            decode(text)
            input("Press Enter to continue")
            morse()
        else: #spatnej input
            print("Your input isn't 1 or 2")
            input("Press Enter to continue")
            morse()

# Funkce zakoduje do morseovky
def encode(message):
    try:
        message = message.upper()
        counter = 1
        code = ''
        for letter in message:
            if letter != ' ':
                if counter < len(message):
                    # Najde ve slovniku odpovidajici kod pro jednotlive znaky
                    code = code + morseCode[letter] + '/'
                else:
                    code = code + morseCode[letter]
            else:
                # 1 / jsou ruzne znaky, 2 / ruzna slova
                code += '/'
            counter = counter + 1
 
        return print(code)
    # P�i nedefinovan�m vstupu se vyp�e chybov� hl�ka
    except KeyError: 
        print("Character", letter, "is note defined in morse code")
        print("These characters are defined: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ( )")
       

# Funkce dek�duje do morseovky
def decode(inputMessage):
    try:
        decodedMessage = ''
        message = inputMessage.split('//') # Do message se ulo�� v�echny slova
        counter = 1
   
        for word in message:
            letters = word.split('/') # Do letters se ulo�� v�echny p�smena
            for letter in letters:
                if (letter != ''): # Pro ka�d� p�smeno se najde odpov�daj�c� kl�� v dictionary morseCode
                    decodedMessage = decodedMessage + list(morseCode.keys())[list(morseCode.values()).index(letter)]
            if (counter < len(message)): # Krom posledn�ho slova, se za ka�d�m slovem p�ip�e mezera
                decodedMessage = decodedMessage + ' '
            counter = counter + 1
        return   print(decodedMessage)
    except Exception: # P�i nenalezen� hodnoty v dictionary se vyp�e chybov� hl�ka
        print("Character", letter, "is note defined in morse code")