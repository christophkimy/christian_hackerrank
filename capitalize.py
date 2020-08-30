# https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    a = []
    for i in s.split(' '):
        a.append(i.capitalize())
    return " ".join(a)
