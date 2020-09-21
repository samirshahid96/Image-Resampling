import numpy as np
import math
##########################################################
from resize import interpolation
interpolation_obj = interpolation.interpolation()
##########################################################
class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """
        calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method

        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """
        resizes an image using nearest neighbor approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method

        """
        R, C = image.shape
        r = round(fx * R)
        c = round(fy * C)
        new_image = np.zeros((r, c), dtype = np.uint8)
        print(R,C)
        print(r,c)
        ##########################################################
        if R > r:
            Sr = R / r
        elif R < r:
            Sr = (R - 1) / r
        if C > c:
            Sc = C / c
        elif C < c:
            Sc = (C - 1) / c
        ##########################################################
        for jr in range(r):
            for jc in range(c):
                Ir = round(jr/fx)
                Ic = round(jc/fy)
                new_image[jr, jc] = image[Ir, Ic]
        ##########################################################
        image = new_image
        return image

    def bilinear_interpolation(self, image, fx, fy):
        """
        resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        
        Note: Do not write the code to perfrom interpolation between points in this file. 
        There is a file named interpolation.py, and two function definitions are provided
        linear_interpolation: Write your code to perform linear interpolation between two in this function
        bilinear_interpolation: Write your code to perfrom bilinear interpolation using four points in this functions. 
        As bilinear interpolation essentially does linear interpolation three times, you coould simply call the
        linear_interpolation function three times, with the correct parameters.

        """

        # Write your code for bilinear interpolation here
        R, C = image.shape
        r = round(fx * R)
        c = round(fy * C)
        new_image = np.zeros((r, c), dtype=np.uint8)
        ##########################################################
        ##########################################################
        for jr in range(r):
            for jc in range(c):
                ##########################################################
                ptr1 = []
                ptr2 = []
                ptr3 = []
                ptr4 = []
                ptr5 = []
                ##########################################################
                ptr5.append(jr,jc,jr/(r/R))
                ptr1.append(min(math.floor(jr / (r/R)), R-1))
                ptr1.append(min(math.floor(jc / (c/C)), C-1))
                ptr1.append(image[min(math.floor(jr / (r/R)), R - 1), min(math.floor(jc / (c/C)), C - 1)])
                ##########################################################
                ptr2.append(min(math.floor(jr / (r/R)), R - 1))
                ptr2.append(min(math.floor(jc / (c/C)) + 1, C - 1))
                ptr2.append(image[min(math.floor(jr / (r/R)), R - 1), min(math.floor(jc / (c/C)) + 1, C - 1)])
                ##########################################################
                ptr3.append(min(math.floor(jr / (r/R)) + 1, R - 1))
                ptr3.append(min(math.floor(jc / (c/C)), C - 1))
                ptr3.append(image[min(math.floor(jr / (r/R)) + 1, R - 1), min(math.floor(jc / (c/C)), C - 1)])
                ##########################################################
                ptr4.append(min(math.floor(jr / (r/R)) + 1, R - 1))
                ptr4.append(min(math.floor(jc / (c/C)) + 1, C - 1))
                ptr4.append(image[min(math.floor(jr / (r/R)) + 1, R - 1), min(math.floor(jc / (c/C)) + 1, C - 1)])
                ##########################################################
                new_image[jr, jc] = interpolation_obj.bilinear_interpolation(ptr1, ptr2, ptr3, ptr4, ((jr/(r/R)), (jc/(c/C))))
        ##########################################################
        image = new_image

        return image
