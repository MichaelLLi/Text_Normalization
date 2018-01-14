from collections import Counter
from num2words import num2words
import numpy as np
import pandas as pd
import re
letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
numbers = '0123456789'
dot = '.'
colon = ':'

def time(a):
    output=['AAAis is wrong!'] * len(a)
    inputtime=a
    for j in range(len(a)):
        try:
            # inputtime[j] = re.sub('[ ]','',inputtime[j])
            inputtime[j] = inputtime[j].lower()
            cnt = Counter(inputtime[j])
            cnt_num = sum(cnt[x] for x in numbers)
            cnt_dot = sum(cnt[x] for x in dot)
            cnt_colon = sum(cnt[x] for x in colon)
            seg = re.findall(r"[0-9]+|[a-zA-Z.]+|[0-9]+",str(inputtime[j]))
            if len(seg) == 1:
                # PM2
                output[j] = len(seg)
            elif len(seg) == 2:
                if (str(seg[0])[0] in numbers) & (str(seg[1])[0] in letters): 
                    seg[1] = re.sub('\.', '', str(seg[1]))
                    output[j] = num2words(int(str(seg[0]))) + ' ' + ' '.join(str(seg[1]))
                    output[j] = re.sub('-',' ',output[j])
                elif (str(seg[0])[0] in numbers) & (str(seg[1])[0] in numbers):
                    if str(seg[1]) == '00':
                        if ((int(str(seg[0])) >= 13) & (int(str(seg[0])) <= 24)) | (int(str(seg[0])) == 0): 
                            output[j] = num2words(int(str(seg[0]))) + ' ' + 'hundred'
                            output[j] = re.sub('-',' ',output[j])
                        else:
                            output[j] = num2words(int(str(seg[0]))) + ' ' + 'o\'clock'
                            output[j] = re.sub('-',' ',output[j])
                    elif str(seg[1])[0] == '0':
                        output[j] = num2words(int(str(seg[0]))) + ' o ' + num2words(int(str(seg[1])[-1]))
                        output[j] = re.sub('-',' ',output[j])
                    else:
                    # seg[1] = re.sub('\.qwertyuiopasdfghjklzxcvbnm', '', str(seg[1]))
                        output[j] = num2words(int(str(seg[0]))) + ' ' + num2words(int(str(seg[1])))
                        output[j] = re.sub('-',' ',output[j])
            elif len(seg) == 3:
                if (str(seg[1])[0] in numbers) & (str(seg[2])[0] in letters):
                    seg[2] = re.sub('\.', '', str(seg[2]))
                    if str(seg[1]) == '00':
                        if str(seg[2]) in ['am','pm']:
                            if(int(str(seg[0])) >=13) & (int(str(seg[0])) <=23):
                                output[j] = num2words(int(str(seg[0]))-12) + ' ' + ' '.join(str(seg[2]))
                                output[j] = re.sub('-',' ',output[j])
                            else:
                                output[j] = num2words(int(str(seg[0]))) + ' ' + ' '.join(str(seg[2]))
                                output[j] = re.sub('-',' ',output[j])
                        else:
                            if ((int(str(seg[0])) >= 13) & (int(str(seg[0])) <= 24)) & (int(str(seg[1])) == 0): 
                                output[j] = num2words(int(str(seg[0]))) + ' ' + 'hundred ' + ' '.join(str(seg[2]))
                                output[j] = re.sub('-',' ',output[j])
                            else:
                                output[j] = num2words(int(str(seg[0]))) + ' o\'clock ' + ' '.join(str(seg[2]))
                                output[j] = re.sub('-',' ',output[j])
                    elif str(seg[1])[0] == '0':
                        output[j] = num2words(int(str(seg[0]))) + ' o ' + num2words(int(str(seg[1])[-1])) + ' ' + ' '.join(str(seg[2]))
                        output[j] = re.sub('-',' ',output[j])
                    elif ((int(seg[0]) >= 13) & (int(seg[0]) <= 23)) & (str(seg[2]) in ['pm']):
                        output[j] = num2words(int(str(seg[0]))-12) + ' ' + num2words(int(str(seg[1]))) + ' ' + ' '.join(str(seg[2]))
                        output[j] = re.sub('-',' ',output[j])
                    else:
                        output[j] = num2words(int(str(seg[0]))) + ' ' + num2words(int(str(seg[1]))) + ' ' + ' '.join(str(seg[2]))
                        output[j] = re.sub('-',' ',output[j])
                elif (str(seg[1])[0] in numbers) & (str(seg[2])[0] in numbers):
                    if cnt_colon == 2:
                        if (str(seg[0]) == '1') | (str(seg[0]) == '01'):
                            if (str(seg[1]) == '1') | (str(seg[1]) == '01'):
                                if (str(seg[2]) == '1') | (str(seg[2]) == '01'):
                                    output[j] = num2words(int(str(seg[0]))) + ' hour ' + num2words(int(str(seg[1]))) + ' minute and ' + num2words(int(str(seg[2]))) + ' second'
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = num2words(int(str(seg[0]))) + ' hour ' + num2words(int(str(seg[1]))) + ' minute and ' + num2words(int(str(seg[2]))) + ' seconds'
                                    output[j] = re.sub('-',' ',output[j])
                            else:
                                if (str(seg[2]) == '1') | (str(seg[2]) == '01'):
                                    output[j] = num2words(int(str(seg[0]))) + ' hour ' + num2words(int(str(seg[1]))) + ' minutes and ' + num2words(int(str(seg[2]))) + ' second'
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = num2words(int(str(seg[0]))) + ' hour ' + num2words(int(str(seg[1]))) + ' minutes and ' + num2words(int(str(seg[2]))) + ' seconds'
                                    output[j] = re.sub('-',' ',output[j])
                        else:
                            if (str(seg[1]) == '1') | (str(seg[1]) == '01'):
                                if (str(seg[2]) == '1') | (str(seg[2]) == '01'):
                                    output[j] = num2words(int(str(seg[0]))) + ' hours ' + num2words(int(str(seg[1]))) + ' minute and ' + num2words(int(str(seg[2]))) + ' second'
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = num2words(int(str(seg[0]))) + ' hours ' + num2words(int(str(seg[1]))) + ' minute and ' + num2words(int(str(seg[2]))) + ' seconds'
                                    output[j] = re.sub('-',' ',output[j])
                            else:
                                if (str(seg[2]) == '1') | (str(seg[2]) == '01'):
                                    output[j] = num2words(int(str(seg[0]))) + ' hours ' + num2words(int(str(seg[1]))) + ' minutes and ' + num2words(int(str(seg[2]))) + ' second'
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = num2words(int(str(seg[0]))) + ' hours ' + num2words(int(str(seg[1]))) + ' minutes and ' + num2words(int(str(seg[2]))) + ' seconds'
                                    output[j] = re.sub('-',' ',output[j])
                elif str(seg[1]) == dot:
                    if str(seg[2])[0] == '0':
                        output[j] = num2words(int(str(seg[0]))) + ' o ' + num2words(int(str(seg[2])[-1]))
                        output[j] = re.sub('-',' ',output[j])
                    else:
                        output[j] = num2words(int(str(seg[0]))) + ' ' + num2words(int(str(seg[2])))
                        output[j] = re.sub('-',' ',output[j])
                elif (str(seg[1])[0] in letters) & (str(seg[2])[0] in letters): 
                    seg[1] = re.sub('\.', '', str(seg[1]))
                    seg[2] = re.sub('\.', '', str(seg[2]))
                    output[j] = num2words(int(str(seg[0]))) + ' ' + ' '.join(str(seg[1])) + ' ' + ' '.join(str(seg[2]))
                    output[j] = re.sub('-',' ',output[j])
                    
            elif len(seg) == 4:
                if (str(seg[2])[0] in letters) & (str(seg[3])[0] in letters):
                    seg[2] = re.sub('\.', '', str(seg[2]))
                    seg[3] = re.sub('\.', '', str(seg[3]))
                    if str(seg[1]) == '00':
                        if str(seg[0])[0] in numbers:
                            if ((int(str(seg[0])) >= 13) & (int(str(seg[0])) <= 23)):
                                output[j] = num2words(int(str(seg[0]))) + ' hundred ' + ' '.join(str(seg[2])) + ' ' + ' '.join(str(seg[3]))
                                output[j] = re.sub('-',' ',output[j])
                            else:
                                output[j] = num2words(int(str(seg[0]))) + ' ' + ' '.join(str(seg[2])) + ' ' + ' '.join(str(seg[3]))
                                output[j] = re.sub('-',' ',output[j])
                    elif str(seg[1])[0] == '0':
                        output[j] = num2words(int(str(seg[0]))) + ' o ' + num2words(int(str(seg[1])[-1]))+ ' '+ ' '.join(str(seg[2])) + ' ' + ' '.join(str(seg[3]))
                        output[j] = re.sub('-',' ',output[j])
                    else:
                        output[j] = num2words(int(str(seg[0]))) + ' ' + num2words(int(str(seg[1]))) + ' ' + ' '.join(str(seg[2])) + ' ' + ' '.join(str(seg[3]))
                        output[j] = re.sub('-',' ',output[j])
                elif (str(seg[2]) in dot):                
                    if (str(seg[0]) == '1') | (str(seg[0]) == '01'):
                        if (str(seg[1]) == '1') | (str(seg[1]) == '01'):
                            if (str(seg[3]) == '1') | (str(seg[3]) == '01'):
                                output[j] = num2words(int(str(seg[0]))) + ' minute ' + num2words(int(str(seg[1]))) + ' second and ' + num2words(int(str(seg[3]))) + ' millisecond'
                                output[j] = re.sub('-',' ',output[j])
                            else:
                                output[j] = num2words(int(str(seg[0]))) + ' minute ' + num2words(int(str(seg[1]))) + ' second and ' + num2words(int(str(seg[3]))) + ' milliseconds'
                                output[j] = re.sub('-',' ',output[j])
                        else:
                            if (str(seg[3]) == '1') | (str(seg[3]) == '01'):
                                output[j] = num2words(int(str(seg[0]))) + ' minute ' + num2words(int(str(seg[1]))) + ' seconds and ' + num2words(int(str(seg[3]))) + ' millisecond'
                                output[j] = re.sub('-',' ',output[j])
                            else:
                                output[j] = num2words(int(str(seg[0]))) + ' minute ' + num2words(int(str(seg[1]))) + ' seconds and ' + num2words(int(str(seg[3]))) + ' milliseconds'
                                output[j] = re.sub('-',' ',output[j])
                    else:
                        if (str(seg[1]) == '1') | (str(seg[1]) == '01'):
                            if (str(seg[3]) == '1') | (str(seg[3]) == '01'):
                                output[j] = num2words(int(str(seg[0]))) + ' minutes ' + num2words(int(str(seg[1]))) + ' second and ' + num2words(int(str(seg[3]))) + ' millisecond'
                                output[j] = re.sub('-',' ',output[j])
                            else:
                                output[j] = num2words(int(str(seg[0]))) + ' minutes ' + num2words(int(str(seg[1]))) + ' second and ' + num2words(int(str(seg[3]))) + ' milliseconds'
                                output[j] = re.sub('-',' ',output[j])
                        else:
                            if (str(seg[3]) == '1') | (str(seg[3]) == '01'):
                                output[j] = num2words(int(str(seg[0]))) + ' minutes ' + num2words(int(str(seg[1]))) + ' seconds and ' + num2words(int(str(seg[3]))) + ' millisecond'
                                output[j] = re.sub('-',' ',output[j])
                            else:
                                output[j] = num2words(int(str(seg[0]))) + ' minutes ' + num2words(int(str(seg[1]))) + ' seconds and ' + num2words(int(str(seg[3]))) + ' milliseconds'
                                output[j] = re.sub('-',' ',output[j])
                elif (str(seg[1]) in dot):
                    if str(seg[3])[0] in letters:
                        seg[3] = re.sub('\.', '', str(seg[3]))
                        if str(seg[2]) == '00':
                            output[j] = num2words(int(str(seg[0]))) + ' ' + ' '.join(str(seg[3]))
                            output[j] = re.sub('-',' ',output[j])
                        elif str(seg[2])[0] == '0':
                            output[j] = num2words(int(str(seg[0]))) + ' o ' + num2words(int(str(seg[2])[-1])) + ' ' + ' '.join(str(seg[3]))
                            output[j] = re.sub('-',' ',output[j])
                        else:
                            output[j] = num2words(int(str(seg[0]))) + ' ' + num2words(int(str(seg[2]))) + ' '+ ' '.join(str(seg[3]))
                            output[j] = re.sub('-',' ',output[j])
                elif str(seg[0])[0] in numbers:
                    if cnt_colon == 2:
                        if (str(seg[0]) == '1') | (str(seg[0]) == '01'):
                            if (str(seg[1]) == '1') | (str(seg[1]) == '01'):
                                if (str(seg[2]) == '1') | (str(seg[2]) == '01'):
                                    output[j] = num2words(int(str(seg[0]))) + ' hour ' + num2words(int(str(seg[1]))) + ' minute and ' + num2words(int(str(seg[2]))) + ' second ' + ' '.join(str(seg[3]))
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = num2words(int(str(seg[0]))) + ' hour ' + num2words(int(str(seg[1]))) + ' minute and ' + num2words(int(str(seg[2]))) + ' seconds ' + ' '.join(str(seg[3]))
                                    output[j] = re.sub('-',' ',output[j])
                            else:
                                if (str(seg[2]) == '1') | (str(seg[2]) == '01'):
                                    output[j] = num2words(int(str(seg[0]))) + ' hour ' + num2words(int(str(seg[1]))) + ' minutes and ' + num2words(int(str(seg[2]))) + ' second ' + ' '.join(str(seg[3]))
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = num2words(int(str(seg[0]))) + ' hour ' + num2words(int(str(seg[1]))) + ' minutes and ' + num2words(int(str(seg[2]))) + ' seconds ' + ' '.join(str(seg[3]))
                                    output[j] = re.sub('-',' ',output[j])
                        else:
                            if (str(seg[1]) == '1') | (str(seg[1]) == '01'):
                                if (str(seg[2]) == '1') | (str(seg[2]) == '01'):
                                    output[j] = num2words(int(str(seg[0]))) + ' hours ' + num2words(int(str(seg[1]))) + ' minute and ' + num2words(int(str(seg[2]))) + ' second ' + ' '.join(str(seg[3]))
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = num2words(int(str(seg[0]))) + ' hours ' + num2words(int(str(seg[1]))) + ' minute and ' + num2words(int(str(seg[2]))) + ' seconds ' + ' '.join(str(seg[3]))
                                    output[j] = re.sub('-',' ',output[j])
                            else:
                                if (str(seg[2]) == '1') | (str(seg[2]) == '01'):
                                    output[j] = num2words(int(str(seg[0]))) + ' hours ' + num2words(int(str(seg[1]))) + ' minutes and ' + num2words(int(str(seg[2]))) + ' second ' + ' '.join(str(seg[3]))
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = num2words(int(str(seg[0]))) + ' hours ' + num2words(int(str(seg[1]))) + ' minutes and ' + num2words(int(str(seg[2]))) + ' seconds ' + ' '.join(str(seg[3]))
                                    output[j] = re.sub('-',' ',output[j])
            elif len(seg) == 5:
                if (str(seg[1]) in dot):
                    if (str(seg[3])[0] in letters) & (str(seg[4])[0] in letters): 
                        seg[3] = re.sub('\.', '', str(seg[3]))
                        seg[4] = re.sub('\.', '', str(seg[4]))
                        if (str(seg[2])) == '00':
                            output[j] = num2words(int(str(seg[0]))) + ' ' + 'o\'clock' + ' ' + ' '.join(str(seg[3])) + ' ' + ' '.join(str(seg[4]))
                            output[j] = re.sub('-',' ',output[j])
                        elif (str(seg[2]))[0] == '0':
                            output[j] = num2words(int(str(seg[0]))) + ' o ' + num2words(int(str(seg[2]))) + ' ' + ' '.join(str(seg[3])) + ' ' + ' '.join(str(seg[4]))
                            output[j] = re.sub('-',' ',output[j])
                        else:     
                            output[j] = num2words(int(str(seg[0]))) + ' ' + num2words(int(str(seg[2]))) + ' ' + ' '.join(str(seg[3])) + ' ' + ' '.join(str(seg[4]))
                            output[j] = re.sub('-',' ',output[j])                
        except ValueError:
            output[j]='AAAis is wrong!'
        except TypeError:
            output[j]='AAAis is wrong!' 
    return output
