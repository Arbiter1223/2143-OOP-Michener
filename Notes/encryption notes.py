# ***Notes from class***
# CAT

# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

# Shift = 3
# C = F
# A = D
# T = W

# set a message
# get a message
# set shift
# encrypt message
# decrypt message!
# print message - getter

# Obfuscation - hiding it in plain sight; only one step to do conversion.
class shiftCipher(object):
    def __init__(self):
        self.plainText = 'None'
        self.cipherText = 'None'
        self.cleanText = 'None'
        self.shift = 3

#****************************************************************************************
# Name: getUserMessage
# Description: Prompts the user for message from standard in
# Parameters: None
#****************************************************************************************

    def getUserMessage(self):
        temp = input("Message: ")
        self.setMessage(temp)

#****************************************************************************************
# Name: setMessage
# Description: Sets plainText and then cleans and calls encrypt
# Parameters:
#   message (string): String message
#   encrypted (bool): False = plainText
#****************************************************************************************

    def setMessage(self, message, encrypted = False):
        if (not encrypted):
            self.plainText = message
            self.cleanData()
            self.__encrypt()
        else:
            self.chipherText = message
            self.__decrypt()

    def getPlainText(self):
        return self.plainText
    
    def getCipherText(self):
        return self.cipherText

    def setShift(self, shift):
        self.shift = shift

    def getShift(self):
        return self.shift

    def cleanData(self):
        self.cleanText = ''
        for letter in self.plainText:
            if (not((ord(letter) > 47 and ord(letter) < 58) or (ord(letter) > 64 and ord(letter) < 91) or (ord(letter) > 96 and ord(letter) < 123))):
                continue
            if ord(letter) > 96:
                self.cleanText += chr(ord(letter) - 32)
            else:
                self.cleanText += letter


    def __encrypt(self):
        self.cipherText = ''
        if (not self.plainText):
            return
        # For each character to be cleaned...
        for letter in self.cleanText:
            # ...if it is a letter (a - z, or A - Z), then encrypt
            if ((ord(letter) > 64 and ord(letter) < 91) or (ord(letter) > 96 and ord(letter) < 123)):
                self.cipherText += chr((((ord(letter) + self.shift) - 65) % 26) + 65)
            # ...if it is a number (0 - 9), then encrypt
            elif (ord(letter) > 47 and ord(letter) < 58):
                self.cipherText += chr((((ord(letter) + self.shift) - 48) % 10) + 48)

    def __decrypt(self):
        self.cleanText = ''
        # For each character to be cleaned...
        for letter in self.cipherText:
            # ...if it is a letter (a - z, or A - Z), then decrypt
            if ((ord(letter) > 64 and ord(letter) < 91) or (ord(letter) > 96 and ord(letter) < 123)):
                self.cleanText += chr((((ord(letter) - self.shift) - 65) % 26) + 65)
            # ...if it is a number (0 - 9), then decrypt
            elif (ord(letter) > 47 and ord(letter) < 58):
                self.cleanText += chr((((ord(letter) - self.shift) - 48) % 10) + 48)


alice = shiftCipher()
alice.getUserMessage()

# DEBUGGING
# print ("\n***Showing values for Alice***")
# print ("Plain Text: " + alice.plainText)
# print ("Clean Text: " + alice.cleanText)
# print ("Cipher Text: " + alice.cipherText)
# rint ("Shift: %d" % (alice.shift))

bob = shiftCipher()
bob.cipherText = alice.getCipherText()

# DEBUGGING
# print ("\n***Showing values for Bob BEFORE setting message***")
# print ("Plain Text: " + bob.plainText)
# print ("Clean Text: " + bob.cleanText)
# print ("Cipher Text: " + bob.cipherText)
# print ("Shift: %d" % (bob.shift))

bob.setMessage(bob.cipherText, True)

# DEBUGGING
# print ("\n***Showing values for Bob AFTER setting message***")
# print ("Plain Text: " + bob.plainText)
# print ("Clean Text: " + bob.cleanText)
# print ("Cipher Text: " + bob.cipherText)
# print ("Shift: %d" % (bob.shift))