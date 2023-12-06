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




def main():
    shift_cipher()

if __name__ == "__main__":
    main()