from math import pi


def calc_cricle_area(r):
    if type(r) not in [int, float] :
        raise TypeError("the radius must be non negative ral number")
    if r < 0:
        raise ValueError("the radius can not be negative")
    return pi * (r**2)
        

# print(calc_cricle_area("3"))