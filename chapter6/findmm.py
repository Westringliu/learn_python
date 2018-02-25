#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if(L):
        max=L[0]
        min=L[0]
        for value in L:
            if value>=max:
                max=value
            if value<=min:
                min=value
        return(min,max)
    else:
        return(None,None)
