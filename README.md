# Digital Image Processing 
Assignment #1

Due: Thu 02/06/20 11:59 PM

1. Resampling:

Do not use any in-built functions from opencv and numpy. In general, you can use function from math library. 
Functions allowed for this part are: np.array(), np.matrix(), np.zeros(), np.ones(), cv2.imread(), cv2.namedWindow(), cv2.waitKey().

(8 pts.) Write code for zooming and shrinking an image using the nearest neighbor and bilinear interpolation. The input to your program is: (i) image, (ii) transformation parameters, and (iii) interpolation method.
 
  - Starter code available in directory resize/      
  - resize/resample.py: One is required to edit the functions "nearest_neighbor" and "bilinear", you are welcome to add more       function. Do not edit the function "resize"
  - resize/interpolation.py: Write code for linear and bilinear interpolation in there respective function definitions, you are welcome to write new functions and call them from these functions
  - This part of the assignment can be run using dip_hw1_resize.py (there is no need to edit this file)
  - Usage: ./dip_hw1_resize.py -i image-name -fx scalex -fy scaley -m method                   
       - image-name: name of the image
       - scalex, scaley: scale to resize the image (eg. fx 0.5, fy 0.5 to make it half the original size)
       - method: "nearest_neightbor" or "bilinear" 
  - Please make sure your code runs when you run the above command from prompt/Terminal
  - Any output images or files must be saved to "output/" folde
----------------------
Two images are provided for testing: cells.png and cell2.jpg
  
Notes: 

1. Files not to be changed: requirements.txt and .circleci directory 

2. the code has to run using one of the following commands

 - Usage: ./dip_hw1_resize.py -i image-name -fx scalex -fy scaley -m method
 
   Example: ./dip_hw1_resize.py -i cells.png -fx 0.5 -fy 0.75 -m nearest_neightbor

 - Usage: python dip_hw1_resize.py -i image-name -fx scalex -fy scaley -m method
 
   Example: python dip_hw1_resize.py -i cells.png -fx 0.5 -fy 0.75 -m nearest_neightbor
  
3. Any output file or image should be written to output/ folder

4. The code has to run on CircleCI

5. The TA will not be able to grade if the code does not pass the CircleCI test

Resampling      - 8 Pts

----------------------
