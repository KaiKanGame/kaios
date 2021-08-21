from assets import sysAssets

def encryptDecrypt(inpString):
    xorKey = 'J'
    length = len(inpString)
    for i in range(length):
     
        inpString = (inpString[:i] +
             chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:])
        print(inpString[i], end = "")
    return inpString
    
if __name__ == '__main__':
    sampleString = sysAssets().crip
    # Encrypt the string
    print(end = "")
    encrypted = end = ""
    sampleString = encryptDecrypt(sampleString)

 
   