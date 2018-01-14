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

def cardinal(a):
    try:
        output=['0'] * len(a)
        inputcardinal=a
        romans='MDCLXVI'
        numbers='-0123456789'
        purenumbers='0123456789'
        for j in range(len(a)):
            if str(inputcardinal[j])[0] in romans:
                if str(inputcardinal[j])[len(str(inputcardinal[j]))-1] in 's':
                    inputcardinal[j] = ''.join( c for c in str(inputcardinal[j]) if c in romans)
                    output[j] = str(num2words(int(roman_to_arabic(inputcardinal[j])))) + '\'s'
                elif str(inputcardinal[j])[len(str(inputcardinal[j]))-1] not in 's':
                    inputcardinal[j] = ''.join( c for c in str(inputcardinal[j]) if c in romans)
                    output[j] = str(num2words(int(roman_to_arabic(inputcardinal[j]))))
            elif str(inputcardinal[j])[0] in numbers:
                if str(inputcardinal[j])[len(inputcardinal[j])-1] not in purenumbers:
                    inputcardinal[j] = str(inputcardinal[j])[:-1]
                    inputcardinal[j] = ''.join( c for c in str(inputcardinal[j]) if c in numbers)
                    output[j] = num2words(int(str(inputcardinal[j]).replace(',','')))
            output[j] = re.sub('[-]',' ',output[j])
            output[j] = re.sub('[,/]','',output[j])
            output[j] = re.sub(' and ',' ',output[j])
        return output
    except ValueError:
        return '0'
