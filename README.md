# Chromatic Aberration

Python implementation of Chromatic Aberration photo effect

## Inputs
+ PATH - path to original image
+ offset - offset in form of [[Rx,Gx,Bx],[Ry,Gy,By]], where COLORaxis is offset of the color(R,G or B) on respected axis (x or y)
+ verbose - if True show image on screen
+ IMAGE - input image in form of PIL image or np.array

## Outputs
+ PIL image

## Gallery
```
img = chromatic_aberation('Data/Penguins.jpg',offset = [[10,0,-10],[-10,-10,-20]],verbose = True)
```

| Original Image                       | Chromatic Aberration                                     |
|--------------------------------------|----------------------------------------------------------|
| ![Original Image](Data/Penguins.jpg) | ![Chromatic Aberration](Results/chromatic_aberation.jpg) |
