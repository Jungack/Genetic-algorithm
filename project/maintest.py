# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:19:35 2021

@author: Florian




"""

import numpy as np
l = [0, 1, 2, 3]
l += np.ones(len(l))/100000
print(l)
weights = [100/(l[i]*sum(1/l)) for i in range (len(l))]
print(weights)
