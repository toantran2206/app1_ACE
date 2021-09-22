from os import write
import streamlit as st
import numpy as np

st.title('ACE Model')
st.write('This is ACE part with 5 questions.')
st.write('With each question, you have 5 choices from "totally disagree" to "totally agree"')

#Answer list:
choices = ['Totally Disagree','Disagree','Confused','Agree','Totally Agree']
score_ace = 0
score_tmp = 0
def calculate(score, question):
    score = 0
    if question == ('Totally Disagree'):
        score += 1
    elif question == ('Disagree'):
        score += 2
    elif question == ('Confused'):
        score += 3
    elif question == ('Agree'):
        score += 4
    else:
        score += 5 
    return score
#Questions
# st.write('1. Tôi biết chọn việc mà làm nên hiếm khi rơi vào trạng thái kiệt sức')
q1 = st.radio('1. Tôi biết chọn việc mà làm nên hiếm khi rơi vào trạng thái kiệt sức', options= choices)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
# if q1 == ('Totally Disagree'):
#    score_ace += 1
# elif q1 == ('Disagree'):
#     score_ace += 2
# elif q1 == ('Confused'):
#     score_ace += 3
# elif q1 == ('Agree'):
#     score_ace += 4
# else:
#     score_ace += 5 
score_tmp = calculate(score_tmp,q1)
score_ace += score_tmp
q2 = st.radio('2. Khi tôi biết mục tiêu của mình là gì và cần làm gì để đạt được mục tiêu đó thì tôi thường cố gắng làm đến nơi đến chốn:',options=choices)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
score_tmp = calculate(score_tmp,q2)
score_ace += score_tmp

q3 = st.radio('3. Khi bắt đầu một việc gì, tôi luôn đặt ra tiêu chuẩn rõ ràng về kết quả đạt được và có kế hoạch hành động cụ thể:',options=choices)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
score_tmp = calculate(score_tmp,q3)
score_ace += score_tmp


q4 = st.radio('4. Trong mọi dự án, tôi luôn giữ được nhiệt huyết và luôn hoàn thành đúng hạn với tiêu chuẩn cao nhất có thể.',options=choices)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
score_tmp = calculate(score_tmp,q4)
score_ace += score_tmp

q5 = st.radio('5. Tôi thường đạt được mục tiêu đã đặt ra',options=choices)
score_tmp = calculate(score_tmp,q5)
score_ace += score_tmp
st.write('Score: ',score_ace)