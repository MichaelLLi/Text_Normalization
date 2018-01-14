# Text Normalization Challenge

This project was created to tackle Google's challenge of Text normalization on Kaggle, namely:
https://www.kaggle.com/c/text-normalization-challenge-english-language

# Introduction and Methodology

To tackle this task, we looked at the translations of each category (such as PLAIN, DATE, etc) defined by Google, and discovered that each category had **clear patterns** of how they should be translated - though there were of course special cases.

To exploit these patterns, we decided on a two step process to predict the speech form of the word: 

1. We classify the word into a certain category.
2. We change the word according to some predefined rules.

This became the "Classification" and "Prediction" part of our algorithm. The classification part of our algorithm was carried out using a mixed set of manually generated and computer-discovered features along with Gradient Boosted Trees, while we mainly used regex, high-frequency word databases, and pattern recognition for our prediction models.

For more information, please visit the respective folders.

# Results

Our final accuracy of translation is 99.31%, which put us at #40 (Top 15%) of the test, leading to a Silver Medal from Kaggle.
