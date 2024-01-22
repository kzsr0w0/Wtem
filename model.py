##########################################################
#
#
############################################################

# モジュールのインポート
import pandas as pd
import numpy as np

# --- データの準備 -------------------------------------------------------------------------#
# 読み込み
data = pd.read_csv('C:\\folder\\make\\Python\\group\\data.csv', encoding='cp932')

# 前処理
t = data['場所']
x = data.drop('場所',axis=1)
x = x.drop('日',axis=1)


# --- モデルの作成 ---------------------------------------------------------------------------------#
# インスタンス化
from sklearn.svm import SVC
model = SVC()

# 学習
model.fit(x,t)

# 書き出し
# モデルの保存
import pickle
pickle.dump(model, open('model','wb'))