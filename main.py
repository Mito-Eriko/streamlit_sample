import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)  #プログレスバー　0 <= value <= 100 for int　    0.0 <= value <= 1.0 for float


for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expandar1 = st.expander('問い合わせ1')
expandar1.write('問い合わせ1の回答')
expandar2 = st.expander('問い合わせ2')
expandar2.write('問い合わせ2の回答')
expandar3 = st.expander('問い合わせ3')
expandar3.write('問い合わせ3の回答')





