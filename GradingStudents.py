#!/bin/python3

import math
import os
import random
import re
import sys



def gradingStudents(n,grades):
    rounded_grades: list = []
    if (1 <= n <= 60):
         for i in grades:
            if i < 38:
                rounded_grades.append(i)
            else:
                if ((i + (5 - i) % 5)-i) < 3:
                    rounded_grades.append(((i + (5 - i) % 5)))
                elif ((i + (5 - i) % 5)-i) >= 3:
                    rounded_grades.append(i)
    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades_count, grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
