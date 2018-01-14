library(tm)
library(stringr)
library(tidyverse)
data=read_csv("en_train.csv")
measure=filter(filter(data,class=="MEASURE"),before!=after)
temp=measure
index=str_locate(temp$before,"[/]?+[A-Za-z%'\"\u0374-\u03FF]")[,1]
temp$before=substring(temp$before,index)
temp=temp[!duplicated(temp$before),]
temp$after=gsub(" o ","",temp$after)
text=c("eleven","twelve","thirteen","fourteen","fifteen",
       "sixteen","seventeen","eighteen","nineteen","twenty",
       "thirty","forty","fifty","sixty","seventy","eighty",
       "ninty","ninety","hundred","thousand","million","point","billion","one","two","three","four","five","six","seven","eight","nine","ten","zero","minus")
for (i in 1:length(text)){
  temp$after=gsub(paste(text[i]," ",sep="")," ",temp$after)
  temp$after=gsub(paste(" ",text[i],sep="")," ",temp$after)                  
}
temp$after=trimws(temp$after)
temp$sentence_id=NULL
temp$token_id=NULL
data_string=c("output_1.csv","output_6.csv","output_11.csv","output_16.csv","output_21.csv","output_91.csv","output_96.csv")
for (i in 1:length(data_string)) {
  data1=read_csv(data_string[i])
  filter1=filter(data1,`Semiotic Class`=="MEASURE")
  colnames(filter1)<-c("class","before","after")
  index=str_locate(filter1$before,"[/]?+[A-Za-z%'\"\u0374-\u03FF]")[,1]
  filter1$before=substring(filter1$before,index)
  filter1=filter1[!duplicated(filter1$before),]
  filter1$after=gsub(" o ","",filter1$after)
  text=c("eleven","twelve","thirteen","fourteen","fifteen",
         "sixteen","seventeen","eighteen","nineteen","twenty",
         "thirty","forty","fifty","sixty","seventy","eighty",
         "ninty","ninety","hundred","thousand","million","point","billion","one","two","three","four","five","six","seven","eight","nine","ten","zero","minus")
  for (i in 1:length(text)){
    filter1$after=gsub(paste(text[i]," ",sep="")," ",filter1$after)
    filter1$after=gsub(paste(" ",text[i],sep="")," ",filter1$after)                  
  }
  filter1$after=trimws(filter1$after)
  temp=unique(rbind(temp,filter1))
}

write_csv(temp,"measure_trans.csv")
