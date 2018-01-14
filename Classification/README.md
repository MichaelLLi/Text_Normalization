# Classification

As detailed on the front page, we divided the task up to two stages - first classify each text to some category of words, and then predict. This part is the classification part - input are words and output are categories, corresponding to those on the kaggle competition.

## Introduction

All of our manually generated features are contained in two modules: features64 and features32. Features32 *only* runs on 32-bit python, due to the enchant library.


## Methodology

The main model used was Gradient Boosted Trees. We used ASCII sequence encoding to let GBM discover its own features, but also assisted it by adding our features through features64 and features32. 

The final model parameters used are detailed in the python file as modelV3 and modelV2.


