# Prediction

As detailed on the front page, we divided the task up to two stages - first classify each text to some category of words, and then predict. This part is the prediction part - input are words and categories, and output are the prediction of the spoken form of the given words.

## Introduction

We made 15 function (one function for each classification) to make prediction for words given their classification results.
All of these functions run on 64-bit python.

## Submission

Based on the results we obtained from the model in gbm_magic.py in the "Classification" folder, we divided the results according to classification and then we individually ran through all 15 prediction functions to get our final prediction for submission. 
