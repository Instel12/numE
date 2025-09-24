dictionary = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",

    "0","1","2","3","4","5","6","7","8","9",

    "!","@","#","$","%","^","&","*","(",")",
    "-","_","=","+","[","]","{","}","|","\\",
    ":",";","'","\"",",",".","/","?","<",">",
    "~","`"," ",
    
    "§","±","µ","¢","£","¥","€","°","©","®",
    "™","¿","¡","•","…","‹","›","¶","ß","þ",
    "ð","ø","å","æ","œ","ƒ","∂","∆","∞","√",
    "≈","≠","≤","≥","÷","×","¤"
]

current = ""

def zerostuff(n):
    s = str(n)
    if len(s) > 1:
        return s
    else:
        return f"0{s}"

def encode(str):
    current = ""  
    for char in str:
        current = f"{current}{zerostuff(dictionary.index(char))}"
    return(current)

def decode(str):
    chunks = [str[i:i+2] for i in range(0, len(str), 2)]
    
    decoded = "".join(dictionary[int(c)] for c in chunks)
    return decoded