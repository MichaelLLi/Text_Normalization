library(tm)
library(stringr)
setwd("xxxxxxx")
data=read_csv("en_train.csv")
money=filter(data,class=="MONEY")
temp=money
temp$before=gsub("[0-9,.-]+","",temp$before)
temp$before=trimws(temp$before)
temp=temp[!duplicated(temp$before),]
temp$after=gsub(" o ","",temp$after)
text=c("eleven","twelve","thirteen","fourteen","fifteen",
       "sixteen","seventeen","eighteen","nineteen","twenty",
       "thirty","forty","fifty","sixty","seventy","eighty",
       "ninty","ninety","hundred","thousand","point","one","two","three","four","five","six","seven","eight","nine","ten","zero","minus")
for (i in 1:length(text)){
  temp$after=gsub(paste(text[i]," ",sep=""),"",temp$after)
  temp$after=gsub(paste(" ",text[i],sep=""),"",temp$after)                  
}
temp$sentence_id=NULL
temp$token_id=NULL
data_string=c("output_1.csv","output_6.csv","output_11.csv","output_16.csv","output_21.csv","output_91.csv","output_96.csv")
for (i in 1:length(data_string)) {
  data1=read_csv(data_string[i])
  filter1=filter(data1,`Semiotic Class`=="MONEY")
  colnames(filter1)<-c("class","before","after")
  filter1$before=gsub("[0-9,.-]+","",filter1$before)
  filter1$before=trimws(filter1$before)
  filter1=filter1[!duplicated(filter1$before),]
  filter1$after=gsub(" o ","",filter1$after)
  text=c("eleven","twelve","thirteen","fourteen","fifteen",
         "sixteen","seventeen","eighteen","nineteen","twenty",
         "thirty","forty","fifty","sixty","seventy","eighty",
         "ninty","ninety","hundred","thousand","point","one","two","three","four","five","six","seven","eight","nine","ten","zero","minus")
  for (i in 1:length(text)){
    filter1$after=gsub(paste(text[i]," ",sep=""),"",filter1$after)
    filter1$after=gsub(paste(" ",text[i],sep=""),"",filter1$after)                  
  }
  temp=unique(rbind(temp,filter1))
}
setwd("xxxxxx")
temp=unique(temp)
write_csv(temp,"money_trans.csv")
