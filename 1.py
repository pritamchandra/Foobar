def solution(s):
    dec = "" #for storing the deciphered string
    
    for i in range(len(s)):
        char = s[i]
        
        #check whether lower case by comparing ASCII values
        if "a" <= char and char <= "z":
            #replace original character with decoded character
            char = chr(219 - ord(char))
         
        dec += char #concatenate the decoded string to dec
    
    return dec
    
s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
print(solution(s))
            