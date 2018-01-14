import pandas as pd
import re
from collections import Counter

def electronic(a):
    output=[None] * len(a)
    inputelectronic=a
    slash = '/'
    for j in range(len(inputelectronic)):
        try:
            cnt = Counter(str(inputelectronic[j]))
            cnt_slash = sum(cnt[x] for x in slash)
            if str(inputelectronic[j]) == '::':
                output[j] = '::'
            elif str(inputelectronic[j])[0] == '#':
                output[j] = ''.join(inputelectronic[j])
                output[j] = output[j].lower()
                output[j] = re.sub('#', 'hash tag ', output[j])
                output[j] = re.sub('\.',' dot',output[j])
                output[j] = re.sub('-',' dash',output[j])
                output[j] = re.sub('/',' slash',output[j])
                output[j] = re.sub(':',' colon',output[j])
                output[j] = re.sub(',',' comma',output[j])
                output[j] = re.sub('0',' o',output[j])
                output[j] = re.sub('1',' one',output[j])
                output[j] = re.sub('2',' two',output[j])
                output[j] = re.sub('3',' three',output[j])
                output[j] = re.sub('4',' four',output[j])
                output[j] = re.sub('5',' five',output[j])
                output[j] = re.sub('6',' six',output[j])
                output[j] = re.sub('7',' seven',output[j])
                output[j] = re.sub('8',' eight',output[j])
                output[j] = re.sub('9',' nine',output[j])
            elif str(inputelectronic[j])[:4] == 'http':
                ab = list(str(inputelectronic[j]))
                output[j] = ' '.join(ab)
                output[j] = output[j].lower()
                output[j] = re.sub('. c o m','. com',output[j])
                output[j] = re.sub('\.','dot',output[j])
                output[j] = re.sub('-','dash',output[j])
                output[j] = re.sub('/','slash',output[j])
                output[j] = re.sub(':','colon',output[j])
                output[j] = re.sub(';','s e m i colon',output[j])
                output[j] = re.sub(',','c o m m a',output[j])
                output[j] = re.sub('_','u n d e r s c o r e',output[j])
                output[j] = re.sub('#','h a s h',output[j])
                output[j] = re.sub('!','e x c l a m a t i o n m a r k',output[j])
                output[j] = re.sub('\)','c l o s i n g p a r e n t h e s i s',output[j])
                output[j] = re.sub('\(','o p e n i n g p a r e n t h e s i s',output[j])
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
            else: 
                ab = list(str(inputelectronic[j]))
                output[j] = ' '.join(ab)
                output[j] = output[j].lower()
                output[j] = re.sub('\.','dot',output[j])
                output[j] = re.sub('-','d a s h',output[j])
                output[j] = re.sub('/','s l a s h',output[j])
                output[j] = re.sub(':','c o l o n',output[j])
                output[j] = re.sub(',','c o m m a',output[j])
                output[j] = re.sub('_','u n d e r s c o r e',output[j])
                output[j] = re.sub('\(','o p e n i n g p a r e n t h e s i s',output[j])
                output[j] = re.sub('\)','c l o s i n g p a r e n t h e s i s',output[j])
                output[j] = re.sub('#','h a s h',output[j])
                output[j] = re.sub('!','e x c l a m a t i o n m a r k',output[j])      
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
        except ValueError:
            output[j]='AAAis is wrong!'
        except TypeError:
            output[j]='AAAis is wrong!'
    return output
