#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:07:06 2017

@author: janusboandersen
"""

from sympy import (symbols, diff, integrate, Rational, lambdify, solve, exp)


t = symbols('t')
y = exp(10*t)

q = 8*(diff(y,t,t))+8*(diff(y,t))+6*y
