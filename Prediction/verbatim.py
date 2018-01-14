from num2words import num2words
import numpy as np
import pandas as pd
import re

def verbatim(a):
    output=[None] * len(a)
    inputverbatim=a
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    capitals = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    greek = {'ς':'sigma','Α':'alpha','Β':'beta','Γ':'gamma','Δ':'delta','Ε':'epsilon','Ζ':'zeta','Η':'eta','Θ':'theta','Ι':'iota','Κ':'kappa','Λ':'lambda','Μ':'mu','Ν':'nu','Ξ':'xi','Ο':'omicron','Π':'pi','Ρ':'rho','Σ':'sigma','Τ':'tau','Υ':'upsilon','Φ':'phi','Χ':'chi','Ψ':'psi','Ω':'omega','α':'alpha','β':'beta','γ':'gamma','δ':'delta','ε':'epsilon','ζ':'zeta','η':'eta','θ':'theta','ι':'iota','κ':'kappa','λ':'lambda','μ':'mu','ν':'nu','ξ':'xi','ο':'omicron','π':'pi','ρ':'rho','σ':'sigma','τ':'tau','υ':'upsilon','φ':'phi','χ':'chi','ψ':'psi','ω':'omega'}
    special = {'#':'number','&':'and','$':'dollar','€':'euro','_':'underscore','%':'percent','~':'tilde','²':'squared', '³':'cubed', '>':'greater than', '<': 'less than', '=':'equals', '*':'asterisk','florida': 'florida'}
    for j in range(len(a)):
        try:
            output[j] = inputverbatim[j]
            if (str(output[j])[0] == '.'):
                output[j] = ' '.join(output[j]) 
                output[j] = re.sub('\.','dot',output[j])
                output[j] = re.sub('-','d a s h',output[j])
                output[j] = re.sub('0','o',output[j])
                output[j] = re.sub('1','o n e',output[j])
                output[j] = re.sub('2','t w o',output[j])
                output[j] = re.sub('3','t h r e e',output[j])
                output[j] = re.sub('4','f o u r',output[j])
                output[j] = re.sub('5','f i v e',output[j])
                output[j] = re.sub('6','s i x',output[j])
                output[j] = re.sub('7','s e v e n',output[j])
                output[j] = re.sub('8','e i g h t',output[j])
                output[j] = re.sub('9','n i n e',output[j])
                output[j] = output[j].lower()
            elif str(output[j]) in special:
                output[j] = special[str(output[j])]
            elif str(output[j]) in greek:
                output[j] = greek[str(output[j])]  
            elif (len(str(output[j])) > 1):
                output[j] = ' '.join(output[j]) 
                output[j] = re.sub('0','o',output[j])
                output[j] = re.sub('1','one',output[j])
                output[j] = re.sub('2','two',output[j])
                output[j] = re.sub('3','three',output[j])
                output[j] = re.sub('4','four',output[j])
                output[j] = re.sub('5','five',output[j])
                output[j] = re.sub('6','six',output[j])
                output[j] = re.sub('7','seven',output[j])
                output[j] = re.sub('8','eight',output[j])
                output[j] = re.sub('9','nine',output[j])
                output[j] = output[j].lower()
            output[j] = re.sub('#', 'hash', output[j])
        except ValueError:
            output[j]='AAAis is wrong!'
        except TypeError:
            output[j]='AAAis is wrong!'
    return output
