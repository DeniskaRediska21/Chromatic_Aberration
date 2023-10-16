import numpy as np
from PIL import Image


def chromatic_aberation(PATH = '',offset = [[0,0,0],[0,0,0]],verbose = True,IMAGE = None):
    if IMAGE == None:
        img = np.array(Image.open(PATH))
    else:
        img = np.array(IMAGE)

    offset = np.array(offset)

    min_abs= [offset[0,np.where(np.abs(offset[0])==np.min(np.abs(offset[0])))],offset[1,np.where(np.abs(offset[1])==np.min(np.abs(offset[1])))]]

    offset[0] -= min_abs[0][0][0]
    offset[1] -= min_abs[1][0][0]

    h,l,c = img.shape
    hk = [np.max(offset[1][offset[1]>=0]),np.min(offset[1][offset[1]<=0])]
    lk = [np.max(offset[0][offset[0]>=0]),np.min(offset[0][offset[0]<=0])] 
    # Create a plaseholder with added zero-padding for offsets
    img_with_boarders = np.zeros((h+hk[0]-hk[1],l+lk[0]-lk[1],c))


    for color in range(c):
    # coordinates for both positive and negative offsets
        coords = [[offset[0,color]- np.sum(offset[0,color][offset[0,color]<0]), h] ,[offset[1,color]- np.sum(offset[1,color][offset[1,color]<0]),l]]
         
        img_with_boarders[coords[0][0]:coords[0][1]+coords[0][0],coords[1][0]:coords[1][1]+coords[1][0],color] = img[:,:,color]

    # Delete added boarders
    img_with_boarders = img_with_boarders[-hk[1]:h-hk[0],-lk[1]:l-lk[0],:]

    img_with_boarders = Image.fromarray(img_with_boarders.astype(np.uint8))
    if verbose:
        img_with_boarders.show()
    return img_with_boarders

#img = chromatic_aberation('Data/Penguins.jpg',offset = [[10,0,-10],[-10,-10,-20]],verbose = True)
#chromatic_aberation(IMAGE=img,offset = [[10,0,-10],[-10,-10,-20]],verbose = True)
#img.save('Results/chromatic_aberation.jpg')
