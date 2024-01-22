##################################################################
#
#   天候から地域推測アプリ
#   202401018 ~ 0122
#
##################################################################

# --- モジュールのインポート ------------------------------------- #
import streamlit as st
import pandas as pd
import pickle

# pickleファイルをロードするための関数を定義
@st.cache
def load_model():
    with open('model', 'rb') as file:
        model = pickle.load(file)
    return model

# この関数は、指定された都市と月に基づいて時系列データの予測を行います。
def predict_time_series(city, month):
    # 実際の時系列モデル（例えばARIMA）をここに実装します。
    # 以下は仮の戻り値としての例です。
    return pd.Series([20, 21, 22], index=pd.date_range('2024-01-01', periods=3, freq='M'))

# モデルをロード
model = load_model()

# --- streamlitのUI------------------------------------------------- #
# タイトル
st.title('気象条件に基づく都市検索と時系列分析')

# ユーザー入力
temperature = st.slider('気温を選択', min_value=-50, max_value=50, value=20)
month = st.selectbox('月を選択', list(range(1, 13)), index=4)
kousuiryou = st.slider('降水量を選択', min_value=0, max_value=50, value=5)
nissyou = st.slider('日照時間を選択', min_value=0, max_value=50, value=5)

# 検索ボタン
if st.button('都市を検索'):
    # 条件に合う都市を検索
    fit_data = [month, temperature,kousuiryou, nissyou]
    prediction = model.predict([fit_data])
    city = prediction
    
    if city:  # cityが空でない場合
        st.write(f'条件に一致する都市: {city}')
        
        # 時系列データの予測
        ts_prediction = predict_time_series(city, month)
        st.line_chart(ts_prediction)
    else:
        st.write('条件に一致する都市は見つかりませんでした。')
