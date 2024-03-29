import argparse
from PIL import Image

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = "@%#*+=-:. "        


def newImg(gscale_img,file_name,gscale,outfile):
    
    global gscale1
    global gscale2
    img_width, img_height = gscale_img.size
    


    if (gscale == 1):
        map_len = round(255/ len(gscale1))
    else:
        map_len = 255 // len(gscale2) 
  
    pix = gscale_img.load()

    with open("{}".format(outfile), 'w') as ascii_img:
        for y in range(img_height):
            for x in range(img_width):
                #print("{} {} {}".format(y,x,pix[y,x]))
                char = pix[x,y]//map_len
                if (gscale == 2):
                    if (char == 10):
                        char = 9
                    ascii_img.write(gscale2[char])
                    if (x == img_width -1):
                        ascii_img.write("\n")
                
                else:
                    #print(len(gscale1))
                    ascii_img.write(gscale1[char])
                    if (x == img_width -1):
                        ascii_img.write("\n")
                    


def scaleImg(img,scale_factor):
    #new_rows, new_cols = (img.size[0])//scale_factor, img.size[1]//scale_factor
    new_rows, new_cols = img.size
    new_cols = new_cols//scale_factor
    new_rows = new_rows//scale_factor
    img = img.resize((new_rows,new_cols),Image.ANTIALIAS)
    
    img = img.convert("RGBA")

    pixdata = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
           # print(pixdata[x,y])
            if pixdata[x, y] == (0, 0, 0, 0):
                pixdata[x, y] = (255, 255, 255, 255)
    

    
    
    
    print(img.size )
    return img
    

def openIMG(img_name,scale_factor,gscale,outfile):

    
    img = Image.open(img_name)

   # print("{},{}".format(img_width,img_height))
    #img = img.convert("LA")

    img = scaleImg(img,scale_factor)
    img = img.convert("L")
    newImg(img,img_name,gscale,outfile)
    #img.show()
    

    
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Img to Ascii")
    
    parser.add_argument('--file', dest='imgFile', required=True) 
    parser.add_argument('--out', dest='outFile', required=False) 
    parser.add_argument('--scale', dest='scale', required=False) 
    parser.add_argument('--grayscale', dest='gscale', required=False)
    
    args = parser.parse_args() 
    
    img_name = None
    if args.imgFile:
        img_name = args.imgFile
    
    outfile = "AsciiImage.txt"
    if args.outFile:
        outfile = args.outFile
    
    scale_factor = 2
    if args.scale:
        scale_factor = int(args.scale)
    
    gscale = 2
    if args.gscale:
        gscale = int(args.gscale)
    
    openIMG(img_name,scale_factor,gscale,outfile)