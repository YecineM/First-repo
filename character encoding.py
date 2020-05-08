"""
It's about :

********************************************
 *********** Character Encoding ***********
  ***********                  ***********
   ***********     encode     ***********
    ***********    input     ***********
     ***********   in any   ***********
      *********** language ***********
       **********          **********
       **********          **********
       ******************************
        
On SoloLearn:
        I don't know if there are any codes
        dealing with this on SoloLearn
        I hope I'm the first one :D
On Python:
        I'm just 'reinventing the wheel'
        because:
        •) I could simply open the file
           in "t" mode (default) and use
           the desired encoding.
        •) str objects have a method called:
           encode()
        •) str() is a built-in function
           that takes an "encoding" argument.
        •) bytes() is a built-in function
           that takes an "encoding" argument.

Little intro:

1) Fixed-width encoding
    *) ASCII (7 bits)
    *) ANSI (8 bits = 1 byte)
          Note: ANSI is often a misnomer.
          It should be "code page" or
          "extended ASCII".
          For example,
          Microsoft has manyyy versions of
          extended ASCII (code pages) that it
          calls ANSI in Notepad.
    *) UTF-32 (32 bits = 4 bytes)
    
2) Variable-width encoding
    *) UTF-8
    *) UTF-16
    
BE vs LE: Big Endianness vs Little Endianness describes byte order.
In a multi-byte number or code unit,
some CPUs read and write the high bytes first ==> big endian CPU
Others read the low bytes first ==> little endian.

BOM: byte order marker

"""

# defining functions (the hard part !!!):

b2d=lambda x:int(x,2) # binary str to decimal
                      # int.
                      # inverse of bin(x)
                      # gonna need it
                      
# getting rid of the annoying leading '0b'
import builtins
bin=lambda x:builtins.bin(x)[2:]
            
# Now the only easy encoding !!! : 
def utf32(text,be):    # BE stands for
                            # big endianness
    ls=[]
    for c in text:
        cp=ord(c)    # Python recognizes
                     # Unicode characters
                     # and gives their
                     # code points
        s=bin(cp).zfill(32)
                     # I need to convert
                     # to binary for this
                     # method.
                     # (another method
                     # is used in utf16).
                     #
                     # zfill(32):
                     # Writing the
                     # insignificant bytes
                     # prevents calling
                     # int("",2)
                     # (ValueError)
                     #
        
        if be:
            for i in range(0,25,8):
                ls.append(
                         b2d(
                            s[i:i+8]
                            )
                         )
        else:
            for i in range(0,25,8):
                ls.append(
                         b2d(
                            s[24-i:32-i]
                            )
                         )
    bom=b"\0\0\xfe\xff"[::1 if be else -1]
    return bom+bytes(ls)

# Now the harder encodings :((

# First:
# The genius utf8 that is
# backwards-compatible with ASCII :

def utf8(text):
    ls=[] # for better performance than
          # concatenation of str
    for c in text:
        cp=ord(c) # code_point
        
        # if less than 128 (ascii char) then
        # same value
        if cp<0x80:
            ls.append(cp)
        
        # else:
        else:
            s=bin(cp).zfill(21)  # binary
            
            # if cp can be written on 11 bits
            if cp<2**11:
                # first byte
                b1="110"+s[-11:-11+5]
                
                # second byte
                b2="10"+s[-11+5:]
                
                ls.extend([b2d(b1),b2d(b2)])
                
            # if cp can be written on 16 bits
            elif cp<2**16:
               # 1st byte
               b1="1110"+\
               s[-16:-16+8-4]
                
               # 2nd
               b2="10"+\
               s[-16+8-4:-16+16-4-2]
                
               # 3rd
               b3="10"+\
               s[-16+16-4-2:]
                
               ls.extend(
               [b2d(b1),b2d(b2),b2d(b3)]
               )
                
            # else we reserve 21 bits:
            # and I'm using a shorter,
            # cleaner method than
            # string concatenation :
            else:
                b1=0b11110000+\
                cp//2**18        # too long
                
                b2=0b10000000+\
                cp%2**18//2**12  # so escaped
                
                b3=0b10000000+\
                cp%2**12//2**6   # newline
                
                b4=0b10000000+cp%2**6
                
                ls.extend([b1,b2,b3,b4])         
    return bytes(ls)

# now utf-16

def utf16(text,be):
    ls=[]
    for c in text:
        cp=ord(c)
        if cp<2**16:
        #
        # Basic Multilingual Plane (BMP)
         # requires two bytes
          # (excluding the little
           # range for surrogates,
            # which is
             # 10+1 bytes wide)
             #
             ls.extend(
             [cp//2**8,cp%2**8][::1 if be \
             else -1]
             )
             
        else:        #
                     # Supplementary planes
                     # require 4 bytes
                     # (= a pair of 2-byte-
                     # surrogates.)
                     #
                     # It's so genius <3 <3
                     #
            cp2=cp-2**16
            
            # high 10 bits
            h10=cp2 // 2**10
            
            # low 10 bits
            l10=cp2 % 2**10
            
            # high surrogate
            high=h10+0xd800
            #low surrogate
            low=l10+0xdc00
            
            # split each surrogate unit
            # (split its two bytes apart)
            
            # byte 1
            b1=high//2**8
            # byte 2
            b2=high%2**8
                            
            # byte 3                
            b3=low//2**8
            
            # byte 4
            b4=low%2**8
            
            ls.extend(
            [b1,b2,b3,b4] if be else \
            [b2,b1,b4,b3]
            )
            
    bom=b"\xfe\xff"[::1 if be else -1]
    return bom+bytes(ls)

# ----------- ASCII --------------
with open(r"ascii.txt","bw") as f:
   b1=b"ASCII content : He's a 'chicken' !"
   b2=bytes(
     [ord(i) for i in \
     "ASCII content : He's a 'chicken' !"]
           )             # just to show that
                         # there are multiple
                         # ways for ASCII
   if b1==b2:
        f.write(b1)

# checking content:
# opening in mode "rt" (default):

with open(r"ascii.txt",
          encoding="ascii") as f:
    print(f.read().center(40))
    print("\n-->ASCII encoded successfully !\n".center(40))
    
# ------ Greek extended ASCII --------------
       
with open(r"greek_ext_ascii.txt","bw") as f:
    b=b"Extended (Greek) ASCII : \xd0 \xd9 \xd3 \xd6 \xd8"
    f.write(b)

# checking content:
# opening in mode "rt" (default):

with open(
         r"greek_ext_ascii.txt",
         encoding="cp1253"
         ) as f:
    print(f.read().center(40))
    print("\n-->Extended ASCII encoded successfully !\n".center(40))


# --------------- UNICODE ----------------- #

s="test string : عربي 好 𣎴"
inp="your string : "+input("\nType your desired Unicode input\n\n")

# ------------ UTF-8 -----------

with open("utf8.txt","bw") as f:
    f.write(utf8(s))
    f.write(utf8("\n"))
    f.write(utf8(inp))

# now checking in mode="rt" (default)
with open("utf8.txt",encoding="utf-8") as f:
    print(f.read())
    print("-->UTF-8 encoded successfully !\n".center(40))

# ----------- UTF-16BE ------------

with open("utf16be.txt","bw") as f:
    f.write(utf16(s,be=True))
    f.write(utf16("\n",True))
    f.write(utf16(inp,True))

# now checking in mode="rt" (default)
with open("utf16be.txt",
         encoding="utf-16") as f:
         # the absence of endianness suffix
         # in the codec name passed to
         # the open() function
         # implies that I put the BOM
         # at the start.
         # If I chose be or le , Python
         # will assume I wrote the bytes in
         # the right order in the file
         # and won't ask for the BOM.
    print(f.read())
    print("-->UTF-16BE encoded successfully !\n".center(40))
    
# ----------- UTF-16LE ------------

with open("utf16le.txt","bw") as f:
    f.write(utf16(s,be=False))
    f.write(utf16("\n",False))
    f.write(utf16(inp,False))

# now checking in mode="rt" (default)
with open("utf16le.txt",
         encoding="utf-16le") as f:
    print(f.read())
    print("-->UTF-16LE encoded successfully !\n".center(40))
    
# ----------- UTF-32BE ------------  

with open("utf32be.txt","bw") as f:
    f.write(utf32(s,be=True))
    f.write(utf32("\n",True))
    f.write(utf32(inp,True))

# now checking in mode="rt" (default)
with open("utf32be.txt",
         encoding="utf-32") as f:
         # didn't need to suffix 'be' as
         # the endianness. Python deduces
         # it from the BOM.
         # If you don't put the BOM
         # an exception is raised.
    print(f.read())
    print("-->UTF-32BE encoded successfully !\n".center(40))
    
# ----------- UTF-32LE ------------  

with open("utf32le.txt","bw") as f:
    f.write(utf32(s,be=False))
    f.write(utf32("\n",False))
    f.write(utf32(inp,False))

# now checking in mode="rt" (default)
with open("utf32le.txt",
         encoding="utf-32le") as f:
    print(f.read())
    print("-->UTF-32LE encoded successfully !\n".center(40))
