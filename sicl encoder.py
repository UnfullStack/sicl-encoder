from PIL import Image

def encodeToByteString(path):    
    img = Image.open(path).quantize(colors=256).convert("RGB")
    w, h = img.size

    pix = img.load()
    
    colors = []
    fstr = f"{(w-1):X}"
    fstr = fstr.zfill(2)

    for y in range(h):
        for x in range(w):
            r, g, b = pix[x, y]
            if not [r,g,b] in colors:
                colors.append([r,g,b])
            a = f"{colors.index([r,g,b]):X}"
            fstr += a.zfill(2)
    
    cstr = ""
    for col in colors:
        cstr += f"{col[0]:X}".zfill(2)+f"{col[1]:X}".zfill(2)+f"{col[2]:X}".zfill(2)
    fstr = f"{(len(colors)-1):X}".zfill(2) + cstr + fstr
    
    return fstr

def decodeAndSave(bstr,output):
    ccount = int(bstr[0]+bstr[1], 16)+1
    colors = []
    cur = 0
    for x in range(ccount):
        i = 2+x*6
        colors.append((int(bstr[i]+bstr[i+1],16),int(bstr[i+2]+bstr[i+3],16),int(bstr[i+4]+bstr[i+5],16)))
        cur = i+6
    w = int(bstr[cur]+bstr[cur+1],16)+1
    cur+=2
    h = round(len(bstr[cur:])/w/2)
    
    img = Image.new("RGB", (w,h), "black")
    
    pix = img.load()
    
    for y in range(h):
        for x in range(w):
            i = x+y*w
            i*=2
            n = int(bstr[cur+i]+bstr[cur+i+1],16)
            pix[x,y] = colors[n]
    
    img.save(output)

def convertToSicl(path,output):
    open(output,"wb").write(bytes.fromhex(encodeToByteString(path)))

def convertFromSicl(path,output):
    decodeAndSave(open(path,"rb").read().hex(),output)

convertToSicl(r"C:\Users\Zach (School)\Pictures\small ansari.jpg","ansari.sicl")
convertFromSicl("ansari.sicl","ansari.png")