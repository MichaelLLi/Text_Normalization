library(tidyverse)
setwd("xxxxxxx")
data=read_csv("en_train.csv")
plain=filter(filter(data,class=="PLAIN"),before==after)
plain_short=filter(plain,nchar(before)<=5)
plain_short$sentence_id=NULL
plain_short$token_id=NULL
data=plain_short

data_string=c("output_1.csv","output_6.csv","output_11.csv","output_16.csv","output_21.csv","output_91.csv","output_96.csv")
for (i in 1:length(data_string)) {
  data1=read_csv(data_string[i])
  filter1=filter(data1,`Output Token`=="<self>")
  filter1=filter(filter1,`Semiotic Class`=="PLAIN")
  filter1=filter(filter1,nchar(`Input Token`)<=5)
  filter1=unique(filter1)
  colnames(filter1)<-c("class","before","after")
  data=unique(rbind(data,filter1))
}
write_csv(data,"letter_capture.csv")
