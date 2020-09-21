class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """
        Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown

        """

        #Write your code for linear interpolation here
        #print(pt1[0],pt2[0])

        x1 = pt1[0]
        x2 = pt2[0]
        I1 = pt1[2]
        I2 = pt2[2]

        if (x2 - x1) == 0:
            p1 = I1
            p2 = I2
        elif (x2 - x1) != 0:
            p1 = I1 * (x2-unknown[0])/(x2 - x1)
            p2 = I2 * (unknown[0] - x1)/(x2 - x1)
        p = p1 + p2
        return p


    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """
        Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown

        """
       # print(pt1, pt2, pt3, pt4, unknown)




        lefttwo = self.linear_interpolation(pt1, pt3, unknown)
        righttwo = self.linear_interpolation(pt2, pt4, unknown)
        if (pt2[1] - pt1[1]) == 0:
            p1 = lefttwo
            p2 = righttwo
        elif (pt2[1] - pt1[1]) != 0:
            p1 = lefttwo * (pt2[1] - unknown[1])/(pt2[1] - pt1[1])
            p2 = righttwo * (unknown[1] - pt1[1])/(pt2[1] - pt1[1])
        p = p1 + p2


        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task
        return p

