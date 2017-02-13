#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:22:23 2017

@author: janusboandersen
"""

#Examples with complex numbers

#Complex math module
import cmath
import math

#define four complex numbers in each of the four quadrants
# 2 | 1
#---|---
# 3 | 4

z1 = 1 + 1j
z2 = -1 + 1j
z3 = -1 - 1j
z4 = 1 - 1j

z = [z1,z2,z3,z4]

#get the argument, preferred polar form
#theta2 = math.atan2(z.imag, z.real)

#manual calculation - shows the problem: z1 and z3 yield same argument angle, as well does z2 and z4
theta_man_1 = [math.atan(z1.imag/z1.real), math.atan(z2.imag/z2.real), math.atan(z3.imag/z3.real), math.atan(z4.imag/z4.real)]

#correcting the calcs by adding/subtracting pi to point angle into right quadrants
theta_man_2 = [math.atan(z1.imag/z1.real), math.atan(z2.imag/z2.real) + math.pi, math.atan(z3.imag/z3.real) - math.pi, math.atan(z4.imag/z4.real)]

#using the cmath functions
theta_rad = [cmath.phase(c) for c in z] #in radians
theta_pi = [t / math.pi for t in theta_rad]  #in terms of fractions of pi
theta_deg = [t * 180.0/math.pi for t in theta_rad]  #in degrees
