import streamlit as st
from PIL import Image
import datetime
import pyperclip
from calc import YushoSentence

if 'calc_btn' not in st.session_state: 
	st.session_state.calc_btn = False

st.title("ぬまぶ優勝条件計算アプリ")
st.caption("最終戦での優勝条件を計算してくれるアプリだよ")
st.caption("1位+200pt, 2位+120pt, 3位+40pt, 4位-40pt, 5位-120pt, 6位-200pt　レア役ボーナスは考慮しないよ")

cols = list(st.columns(3))
names = [ "" for i in range(6)]
y_sentence = [ "" for i in range(6)]
stacks = [ 0 for i in range(6) ]
copy_btns = [ False for i in range(6)]

#フォームの形成
with st.container():
	for i in range(3):
		with cols[i]:
			#名前
			names[i] = st.text_input('名前'+str(i+1), placeholder = '名前'+str(i+1))
			#ポイント
			stacks[i] = st.number_input('ポイント'+str(i+1), step = 10)
			#名前
			names[i+3] = st.text_input('名前'+str(i+4), placeholder = '名前'+str(i+4))
			#ポイント
			stacks[i+3] = st.number_input('ポイント'+str(i+4), step = 10)
			st.caption("----------------")
submit_btn = st.button("計算")

with st.container():
	if submit_btn or st.session_state.calc_btn:
		st.session_state.calc_btn = True
		for i in range(6):
			if names[i] == '':
				names[i] = "Player{}".format(i + 1)
		for i in range(6):
			y_sentence[i] = YushoSentence(stacks, i + 1, names)
		for i in range(3):
			with cols[i]:
				st.text_area(names[i]+'の優勝条件', y_sentence[i])
				copy_btns[i] = st.button("↑コピー", key = i)
				if copy_btns[i]:
					pyperclip.copy(y_sentence[i])
				st.text_area(names[i+3]+'の優勝条件', y_sentence[i+3])
				copy_btns[i+3] = st.button("↑コピー", key = i+3)
				if copy_btns[i+3]:
					pyperclip.copy(y_sentence[i+3])	
				st.caption("----------------")