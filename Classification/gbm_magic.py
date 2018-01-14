# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 04:26:16 2017

@author: Michael
"""

import pandas as pd
import numpy as np
import os
import pickle
import gc
import xgboost as xgb
import re
from sklearn.cross_validation import train_test_split

max_num_features = 25
pad_size = 1
boundary_letter = -1
space_letter = 0
max_data_size = 3000000

out_path = r'.'
df = pd.read_csv('en_train.csv')
dataX=pd.read_csv("true_train_x_full.csv",encoding="latin-1")
dataX=dataX.values
dataX=dataX[:,4:]
x_data = []
y_data =  pd.factorize(df['class'])
labels = y_data[1]
y_data = y_data[0]
gc.collect()
for x in df['before'].values:
    x_row = np.ones(max_num_features, dtype=int) * space_letter
    for xi, i in zip(list(str(x)), np.arange(max_num_features)):
        x_row[i] = ord(xi)
    x_data.append(x_row)

def context_window_transform(data, pad_size):
    pre = np.zeros(max_num_features)
    pre = [pre for x in np.arange(pad_size)]
    data = pre + data + pre
    neo_data = []
    for i in np.arange(len(data) - pad_size * 2):
        row = []
        for x in data[i : i + pad_size * 2 + 1]:
            row.append([boundary_letter])
            row.append(x)
        row.append([boundary_letter])
        neo_data.append([int(x) for y in row for x in y])
    return neo_data

x_data = x_data[2+4000000:max_data_size+4000000]
y_data = y_data[2+4000000:max_data_size+4000000]
x_data = np.array(context_window_transform(x_data, pad_size))
gc.collect()
x_data = np.array(x_data)
y_data = np.array(y_data)

print('Total number of samples:', len(x_data))
print('Use: ', max_data_size)
#x_data = np.array(x_data)
#y_data = np.array(y_data)

print('x_data sample:')
print(x_data[0])
print('y_data sample:')
print(y_data[0])
print('labels:')
print(labels)

x_train=x_data
y_train=y_data

gc.collect()
x_train, x_valid, y_train, y_valid= train_test_split(x_train, y_train,
                                                      test_size=0.1, random_state=2017)


gc.collect()
num_class = len(labels)
dtrain = xgb.DMatrix(x_train, label=y_train)
dvalid = xgb.DMatrix(x_valid, label=y_valid)

df = pd.read_csv('en_test.csv')
x_data = []
for x in df['before'].values:
    x_row = np.ones(max_num_features, dtype=int) * space_letter
    for xi, i in zip(list(str(x)), np.arange(max_num_features)):
        x_row[i] = ord(xi)
    x_data.append(x_row)
x_data = np.array(context_window_transform(x_data, pad_size))
gc.collect()
x_data = np.array(x_data)
dtest=xgb.DMatrix(x_data)





watchlist = [ (dtrain, 'train'), (dvalid, 'valid')]

param = {'objective':'multi:softmax',
         'eta':'0.2', 'max_depth':12,
         'silent':1, 'nthread':-1,
         'num_class':num_class,
         'eval_metric':'merror'}
modelV3 = xgb.train(param, dtrain, 50, watchlist, early_stopping_rounds=20,
                  verbose_eval=10,xgb_model=model)


param = {'objective':'multi:softmax',
         'eta':'0.1', 'max_depth':15,
         'silent':1, 'nthread':-1,
         'num_class':16,
         'eval_metric':'merror','min_child_weight':5}
modelV2 = xgb.train(param, dtrain, 50, watchlist, early_stopping_rounds=10,
                  verbose_eval=10,xgb_model=model)
gc.collect()

pred = model.predict(dtest)
pred = [labels[int(x)] for x in pred]
y_valid = [labels[x] for x in y_valid]
x_valid = [ [ chr(x) for x in y[2 + max_num_features: 2 + max_num_features * 2]] for y in x_valid]
x_valid = [''.join(x) for x in x_valid]
x_valid = [re.sub('a+$', '', x) for x in x_valid]

gc.collect()

df_pred = pd.DataFrame(columns=['data', 'predict', 'target'])
df_pred['data'] = x_valid
df_pred['predict'] = pred
df_pred['target'] = y_valid
df_pred.to_csv(os.path.join(out_path, 'pred_V5.csv'))

df_erros = df_pred.loc[df_pred['predict'] != df_pred['target']]
df_erros.to_csv(os.path.join(out_path, 'errors_V5.csv'), index=False)

model.save_model(os.path.join(out_path, 'xgb_model'))



