#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def quadratic(a, b, c):
    nx=-b+math.sqrt(b*b-a*c*4)
    ny=-b-math.sqrt(b*b-a*c*4)
    return nx,ny

