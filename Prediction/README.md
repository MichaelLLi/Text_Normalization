# Prediction

As detailed on the front page, we divided the task up to two stages - first classify each text to some category of words, and then predict. This part is the prediction part - input are words and categories, and output are the prediction of the spoken form of the given words.

## Introduction

We made 15 functions (one function for each classification, we did not need to change the 'PUNCT' classification) to make prediction for words given their classification results.
All of these functions run on 64-bit python.

## Submission

Based on the results we got from the model in gbm_magic.py in the "Classification" folder, we divided the results into 16 pieces corresponding to classification and then we individually ran through all 15 prediction functions to obtain our final prediction for submission. 
