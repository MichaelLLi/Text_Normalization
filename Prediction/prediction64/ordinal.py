from num2words import num2words
import numpy as np
import pandas as pd
import re

numerals = [
        {'letter': 'M', 'value': 1000},
        {'letter': 'D', 'value': 500},
        {'letter': 'C', 'value': 100},
        {'letter': 'L', 'value': 50},
        {'letter': 'X', 'value': 10},
        {'letter': 'V', 'value': 5},
        {'letter': 'I', 'value': 1},
    ]

def roman_to_arabic(number):
    index_by_letter = {}
    for index in (range(len(numerals))):
        index_by_letter[numerals[index]['letter']] = index

    result = 0
    previous_value = None
    for letter in reversed(number):
        index = index_by_letter[letter]
        value = numerals[index]['value']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value
    return result

def ordinal(a):
    output=[None] * len(a)
    inputordinal=a
    romans='MDCLXVI'
    numbers='-0123456789'
    for j in range(len(a)):
        try:
            if str(inputordinal[j])[0] in romans:
                if str(inputordinal[j])[len(str(inputordinal[j]))-1] in 's':
                    inputordinal[j] = ''.join( c for c in str(inputordinal[j]) if c in romans)
                    output[j] = 'the' + ' ' + str(num2words(int(roman_to_arabic(inputordinal[j])),ordinal = True)) + '\'s'
                else:
                    inputordinal[j] = ''.join( c for c in str(inputordinal[j]) if c in romans)
                    output[j] = 'the' + ' ' + str(num2words(int(roman_to_arabic(inputordinal[j])),ordinal = True))
            else:
                inputordinal[j] = ''.join( c for c in str(inputordinal[j]) if c in numbers)
                output[j] = num2words(int(str(inputordinal[j]).replace(',','')), ordinal = True)
            output[j] = re.sub('[-]',' ',output[j])
            output[j] = re.sub('[,/]','',output[j])
            output[j] = re.sub(' and ',' ',output[j])
        except ValueError:
            output[j]='AAAis is wrong!'
        except TypeError:
            output[j]='AAAis is wrong!'
    return output
