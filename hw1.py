''' 
@author: Nikhil Patil
@description: hw01 CSCI-462'''

def shift_cipher():
    text = "nybfxymjgjxytkynrjxnybfxymjbtwxytkynrjxnybfxymjfljtkbnxitrnybfxymjfljtkkttqnxmsjxx"
    for i in range(1,26):
        print("Shift: ", i)
        for j in range(0,len(text)):
            print(chr((ord(text[j])-97+i)%26+97), end="")
        print("\n")

def affine_cipher():
    encryptedText = "zuqtqgsytqvrsdqztwvaoyajramjazi"
    decryptedText = ""
    a = 7
    b = 22
    for i in range(0,26):
        if((7*i)%26 == 1):
            aInverse = i
    print("The inverse of a is: " + str(aInverse))
    # Decrypting Time 
    for i in range(0,len(encryptedText)):
        decryptedText += chr(((aInverse*(ord(encryptedText[i])-97-b))%26)+97)
    print(decryptedText)

def converter(value = None):
    if value is None:
        value = input("Enter a base-10 value to convert: ")
        print("Binary: " + str(bin(int(value)))[2:])
        print("Hex: " + str(hex(int(value)))[2:])
    else:
        print("Binary: " + str(bin(int(value)))[2:])
        print("Hex: " + str(hex(int(value)))[2:])


def ringCreator(arithmetic, modulus):
    modulus = int(modulus) 
    for i in range(0,modulus):
        for j in range(0,modulus):
            print(str(i) + " " + arithmetic + " " + str(j) + " = " + str(eval(str(i) + arithmetic + str(j))%modulus))
        print("\n")

def main():
    affine_cipher()
    converter(10)
    ringCreator("+", 4)
    ringCreator("*", 4)
if __name__ == "__main__":
    main()