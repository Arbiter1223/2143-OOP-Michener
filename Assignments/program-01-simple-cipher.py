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

#****************************************************************************************
# Name: getPlainText
# Description: Simply returns plainText
#****************************************************************************************

    def getPlainText(self):
        return self.plainText

#****************************************************************************************
# Name: getCipherText
# Description: Simply returns cipherText
#****************************************************************************************
    
    def getCipherText(self):
        return self.cipherText

#****************************************************************************************
# Name: setShift
# Description: Sets the shift for encryption
# Parameters:
#    shift (int): Amount to shift by
#****************************************************************************************

    def setShift(self, shift):
        self.shift = shift

#****************************************************************************************
# Name: getShift
# Description: Simply returns the shift number
#****************************************************************************************

    def getShift(self):
        return self.shift

#****************************************************************************************
# Name: cleanData
# Description: Cleans the message entered by the user and prepares it for encryption
#****************************************************************************************

    def cleanData(self):
        self.cleanText = ''
        for letter in self.plainText:
            if (not((ord(letter) > 47 and ord(letter) < 58) or (ord(letter) > 64 and ord(letter) < 91) or (ord(letter) > 96 and ord(letter) < 123))):
                continue
            if ord(letter) > 96:
                self.cleanText += chr(ord(letter) - 32)
            else:
                self.cleanText += letter

#****************************************************************************************
# Name: __encrypt
# Description: Takes cleanText and offsets it by specified shift to create cipherText
#****************************************************************************************

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

#****************************************************************************************
# Name: __decrypt
# Description: Takes cipherText and offsets it (in other direction) by specified shift
#    to recreate cleanText
#****************************************************************************************

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

print ("Input: " + alice.plainText)
print ("Output: " + bob.cleanText)