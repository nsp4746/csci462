''' 
@author: Nikhil Patil
@description: hw02 CSCI-462
'''
import math as m


def multiplicativeInverseInRing(value, modulus):
    for i in range(0, modulus):
        if ((value*i) % modulus == 1):
            return i
    return -1


def modPower(value, power, modulus):
    return str(value) + "**"+str(power)+" mod " + str(modulus) + ": " + str((round(m.pow(value, power) % modulus)))


def main():
    print(modPower(3,2,13))

if __name__ == "__main__":
    main()