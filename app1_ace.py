from os import write
import streamlit as st
import numpy as np

st.title('ACE Model')
st.write('This is ACE part with 5 questions.')
st.write('With each question, you have 5 choices from "totally disagree" to "totally agree"')

#Answer list:
choices = ['Totally Disagree','Disagree','Confused','Agree','Totally Agree']
score_ace = 0

#Questions
st.write('1. Tôi biết chọn việc mà làm nên hiếm khi rơi vào trạng thái kiệt sức')
q1 = st.radio('1. Tôi biết chọn việc mà làm nên hiếm khi rơi vào trạng thái kiệt sức', options= choices)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
if q1 == ('Totally Disagree'):
   score_ace += 1
elif q1 == ('Disagree'):
    score_ace += 2
elif q1 == ('Confused'):
    score_ace += 3
elif q1 == ('Agree'):
    score_ace += 4
else:
    score_ace += 5 
st.write('Score: ',score_ace)