import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

### 基本表示 ###
# データフレーム #
st.write('DataFrame')
df = pd.DataFrame({
    '一列目': [1, 2, 3, 4],
    '二列目': [10, 20, 30, 40] 
})
 # 表作成方法
 # 1.write
st.write(df)
 # 2.dataframe（動的）
 # widthとheight等引数を指定できる、axis=0で列方向に最大値をハイライト、axis=1で行方向に最大値をハイライト
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
 # 3.table（静的）
st.table(df.style.highlight_max(axis=0))

# マジックコマンド
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# チャート
st.write('チャート')
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

# マップ
st.write('マップ')
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

# 画像
st.write('画像')
from PIL import Image
img = Image.open('sample.png')
st.image(img, caption='Math', use_column_width=True)


### インタラクティブなウィジェット ###
# チェックボックス
st.write('チェックボックス')
if st.checkbox('SHow Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Math', use_column_width=True)

# セレクトボックス
st.write('セレクトボックス')
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
f'あなたの好きな数字は{option}です。'

# テキスト入力
st.write('テキスト入力')
text = st.text_input('あなたの趣味を教えてください')
f'あなたの趣味：{text}'

#スライダー
st.write('スライダー')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition


### レイアウト ###
# サイドバー
st.write('サイドバー')
st.sidebar.write('サイドバー')
text = st.sidebar.text_input('あなたの趣味は？')
condition = st.sidebar.slider('あなたの調子は？', 0, 100, 50)

'あなたの趣味：', text
'コンディション：', condition

# 2カラムレイアウト
st.write('2カラムレイアウト')
left_column, right_column = st.columns(2)
button = left_column.button('右のカラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# expander
st.write('expander')
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


### プログレスバー ###
import time
st.write('プログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'


