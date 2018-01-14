library(readr)
library(tidyverse)
library(stringr)
Sys.setlocale("LC_ALL", 'en_US.UTF-8')
setwd("xxxxxxx")
classification <- read_csv("gbm_pred_true_test_magic3.csv")
en_test_2 <- read_csv("en_test_2.csv")
magic <- cbind(en_test_2, classification)
magic <- magic[,-4]
colnames(magic)[4] <- 'pred'

############## Predict address ##########################
address <- magic %>% 
  filter(pred == 'ADDRESS')
write.csv(address, 'address_V4.csv', row.names = F)

############## Predict cardinal ##########################
cardinal <- magic %>% 
  filter(pred == 'CARDINAL')
write.csv(cardinal, 'cardinal_V4.csv', row.names = F)

############## Predict date ##########################
date <- magic %>% 
  filter(pred == 'DATE')
write.csv(date, 'date_V4.csv', row.names = F)

############## Predict decimal ##########################
decimal <- magic %>% 
  filter(pred == 'DECIMAL')
write.csv(decimal, 'decimal_V4.csv', row.names = F)

############## Predict digit ##########################
digit <- magic %>% 
  filter(pred == 'DIGIT')
write.csv(digit, 'digit_V4.csv', row.names = F)

############## Predict electronic ##########################
electronic <- magic %>% 
  filter(pred == 'ELECTRONIC')
write.csv(electronic, 'electronic_V4.csv', row.names = F)

############## Predict fraction ##########################
fraction <- magic %>% 
  filter(pred == 'FRACTION')
write.csv(fraction, 'fraction_V4.csv', row.names = F)

############## Predict letters ##########################
letters <- magic %>% 
  filter(pred == 'LETTERS')
write.csv(letters, 'letters_V4.csv', row.names = F)

############## Predict measure ##########################
measure <- magic %>% 
  filter(pred == 'MEASURE')
write.csv(measure, 'measure_V4.csv', row.names = F)

############## Predict money ##########################
money <- magic %>% 
  filter(pred == 'MONEY')
write.csv(money, 'money_V4.csv', row.names = F)

############## Predict ordinal ##########################
ordinal <- magic %>% 
  filter(pred == 'ORDINAL')
write.csv(ordinal, 'ordinal_V4.csv', row.names = F)

############## Predict plain ##########################
plain <- magic %>% 
  filter(pred == 'PLAIN')
write.csv(plain, 'plain_V4.csv', row.names = F)

############## Predict telephone ##########################
telephone <- magic %>% 
  filter(pred == 'TELEPHONE')
write.csv(telephone, 'telephone_V4.csv', row.names = F)

############## Predict time ##########################
time <- magic %>% 
  filter(pred == 'TIME')
write.csv(time, 'time_V4.csv', row.names = F)

############## Predict verbatim ##########################
verbatim <- magic %>% 
  filter(pred == 'VERBATIM')
write.csv(verbatim, 'verbatim_V4.csv', row.names = F)

############## Predict punctuation ##########################
punctuation <- magic %>% 
  filter(pred == 'PUNCT')
punctuation$`0` <- punctuation$before


############## Loading the results from running prediction functions  ##################################
address6 <- read_csv("address6.csv")
cardinal6 <- read_csv("cardinal6.csv")
date6 <- read_csv("date6.csv")
decimal6 <- read_csv("decimal6.csv")
digit6 <- read_csv("digit6.csv")
electronic6 <- read_csv("electronic6.csv")
fraction6 <- read_csv("fraction6.csv")
letters6 <- read_csv("letters6.csv")
measure6 <- read_csv("measure6.csv")
money6 <- read_csv("money6.csv")
ordinal6 <- read_csv("ordinal6.csv")
plain6 <- read_csv("plain6.csv")
telephone6 <- read_csv("telephone6.csv")
time6 <- read_csv("time6.csv")
verbatim6 <- read_csv("verbatim6.csv")

model_V4 <- rbind(address6,cardinal6, date6, decimal6, digit6, electronic6, fraction6, letters6, measure6, money6, ordinal6,plain6,telephone6,time6,verbatim6)
model_V4 <- model_V4[,-1]
model_V4 <- rbind(model_V4, punctuation)

model_V4 <- model_V4 %>% 
  arrange(sentence_id, token_id)

model_V4$id <- paste(model_V4$sentence_id,model_V4$token_id,sep='_')
colnames(model_V4)[5] <- 'after'
submission_V4 <- model_V4[,c(6,5)]

write.csv(model_V4, 'model_V4.csv',col.names = F)

## Write the submission file ##
write.csv(submission_V4, 'submission_V4.csv',row.names = F)
