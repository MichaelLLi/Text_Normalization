library(tidyverse)
library(wordnet)
inWordnet <- function(w, pos =  c("ADJECTIVE", "ADVERB", "NOUN", "VERB")) {
  for (x in pos) {
    filter <- getTermFilter("ExactMatchFilter", w, TRUE)
    terms <- getIndexTerms(x, 5, filter)
    if (!is.null(terms)) return(TRUE)
  }
  return(FALSE)
}
vInWordnet <- Vectorize(inWordnet, vectorize.args = c("w", "pos"))
vInWordnet(c("of"))


data=read_csv("en_train.csv")
letters=filter(data,class=="LETTERS")
letters$sentence_id=NULL
letters$token_id=NULL
output=unique(letters)


write_csv(output,"letter_reverse.csv")
