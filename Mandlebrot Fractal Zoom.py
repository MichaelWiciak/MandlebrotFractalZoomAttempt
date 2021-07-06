from PIL import Image
import math
import cmath

class ZoomCreator(object):
    
    def __init__(self, coords, magnification):
        self._coords = coords
        self._size = magnification
        self.__drawImage()
        
    def __drawImage(self):
        img = Image.new('RGB',(500,500),'black')
        bm = img.load()
        
        for x in range(500*500):
            realPart = (x%500-250)/(self._size*100) + self._coords[0]
            imaginaryPart = (x//500 - 250)/(self._size*100) + self._coords[1]
            colour = self.__interperetCoordAsColour((realPart, imaginaryPart))
            bm[x%500,x//500] = (colour>>16, (colour>>8)%(2**8), colour%(2**8))
            
        self._image = img
        
    def saveImage(self, location = 'm'):
        self._image.show()
        self._image.save(location+'.bmp')
        
    def returnImage(self):
        return self._image
                
    def __interperetCoordAsColour(self, coords):
        iterationsToDestabilise = 0
        numberToAdd = complex(coords[0], coords[1])
        x = complex(0,0)
        while iterationsToDestabilise < 200 and abs(x)<30:
            x=x**2 + numberToAdd
            iterationsToDestabilise+=1
            
        colourNumber = int((iterationsToDestabilise/200 * (2**24-1))//1)
        return colourNumber


zoomCoords = []
zoomCoords.append((-1.99999999913827011875827476290869498831680913663682095950680227271547027727918984035447670553861909622481524128059475119256402014495673143316612650410291078,1.31489544350763757513624756680650500215170052091209570952944934353054899402752459447109588643199807746570323310307848990793091163454288839050259823313135764*10**-14))
zoomCoords.append((0.25-2**(-10000),0))


images = []
for i in range(1,100):
    print(i)
    a = ZoomCreator(zoomCoords[0], 2**i/2)
    images.append(a.returnImage())
images[0].save('zoom.gif', format='GIF', append_images=images[1:], save_all=True, duration = 10, loop = 0)
 



