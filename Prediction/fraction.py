import re
from num2words import num2words
import numpy as np

def fraction(a):
    # output= np.empty(shape=(len(a),1),dtype=object)
    output=['AAAis is wrong!'] * len(a)
    for i in range(len(a)):
        try:
            word=str(a[i])
            if "-" in word:
                output_temp="minus "
            else:
                output_temp=""
            word=word.replace("-","")
            word=word.replace("¼"," 1/4")
            word=word.replace("½"," 1/2")
            word=word.replace("¾"," 3/4")
            word=word.replace("⅞"," 7/8")
            word=word.replace("⅝"," 5/8")
            word=word.replace("⅛"," 1/8")
            word=word.replace("⅓"," 1/3")
            word=word.replace("⅔"," 2/3")
            word=word.replace(",","")
            comp=re.findall(r'[0-9]+[ ]|[0-9 ]+|[0-9/ ]+',word)
            if len(comp)>0:
                for j in range(len(comp)):
                    comp[j]=comp[j].replace(" ","")
            if len(comp)==2:
                num_temp=num2words(int(comp[0]))
                num_temp=num_temp.replace(" and "," ")
                num_temp=num_temp.replace("-"," ")
                num_temp=num_temp.replace(",","")
                output_temp += num_temp
                fraction_temp=comp[1].replace("/","")
                if int(fraction_temp) !=4 and int(fraction_temp) !=2 and int(fraction_temp) !=1:
                    frac_temp=num2words(int(fraction_temp),ordinal=True)
                    frac_temp=frac_temp.replace(" and "," ")
                    frac_temp=frac_temp.replace("-"," ")
                    frac_temp=frac_temp.replace(",","")
                    output_temp +=" "
                    output_temp +=frac_temp
                elif int(fraction_temp)==4:
                    output_temp +=" quarter"
                elif int(fraction_temp)==2 and int(comp[0])>1:
                    output_temp +=" halves"
                elif int(fraction_temp)==1:
                    output_temp +=" over one"
                else:
                    output_temp +=" half"            
                if int(comp[0])!=1 and int(fraction_temp)!=2 and int(fraction_temp) !=1:
                    output_temp +="s"
            elif len(comp)==3:
                whole_temp=num2words(int(comp[0]))
                whole_temp=whole_temp.replace(" and "," ")
                whole_temp=whole_temp.replace("-"," ")
                whole_temp=whole_temp.replace(",","")            
                output_temp +=whole_temp
                output_temp +=" and "
                comp[1]=comp[1].replace("/","")
                num_temp=num2words(int(comp[1]))
                num_temp=num_temp.replace(" and "," ")
                num_temp=num_temp.replace("-"," ")
                num_temp=num_temp.replace(",","")
                fraction_temp=comp[2].replace("/","")
                if int(comp[1])!=1:
                    output_temp += num_temp
                elif fraction_temp[0] !='8':
                    output_temp += "a"
                else:
                    output_temp += "an"               
                if int(fraction_temp) !=4 and int(fraction_temp) !=2 and int(fraction_temp) !=1:
                    frac_temp=num2words(int(fraction_temp),ordinal=True)
                    frac_temp=frac_temp.replace(" and "," ")
                    frac_temp=frac_temp.replace("-"," ")
                    frac_temp=frac_temp.replace(",","")
                    output_temp +=" "
                    output_temp +=frac_temp
                elif int(fraction_temp)==4:
                    output_temp +=" quarter"
                elif int(fraction_temp)==2 and int(comp[1])>1:
                    output_temp +=" halves"
                elif int(fraction_temp)==1:
                    output_temp +=" over one"
                else:
                    output_temp +=" half"            
                if int(comp[1])!=1 and int(fraction_temp)!=2 and int(fraction_temp) !=1:
                    output_temp +="s"            
            output[i]=output_temp
        except ValueError:
            output[i]='AAAis is wrong!'
        except TypeError:
            output[i]='AAAis is wrong!'
    return output  
