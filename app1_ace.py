from os import write
import streamlit as st
import numpy as np
import pickle as pkle
import os.path

#Main page
def main():
    #Register pages
    pages = {
        "Home page": page_first,
        "ACE Model": page_second,
        "Self-Concept Maintenance": page_third,
        "Open Mind": page_fourth,
        "Motivation":page_fifth,
        "Reflexivity": page_sixth,
    }
    if "page" not in st.session_state:
        st.session_state.update({
            # Default page
            "page": "Home page",

            # Radio, selectbox and multiselect options
            "options": ["Hello", "Everyone", "Happy", "Streamlit-ing"],

            # Default widget values
            "text": "",
            "slider": 0,
            "checkbox": False,
            "radio": "Hello",
            "selectbox": "Hello",
            "multiselect": ["Hello", "Everyone"],
        })
    st.header('Diver-conscinousness')
    st.write('Hi there! Welcome to our diver-consciousness app!')
    user_input = st.text_input("Please tell us your name:")
    if user_input:
        st.write('Hi, ',user_input)
        st.write('This a diver-consciousness quiz with 40 questions. There is not right or wrong answer. You just need to think carefully and choose which suites you best!')
        if st.button("Click here to start"):
            with st.sidebar:
                page = st.radio("Select your page", tuple(pages.keys()))
            pages[page]()
#Home page
def page_first():
    st.write(f"""
    # Settings values
    - **Input**: {st.session_state.text}
    - **Slider**: `{st.session_state.slider}`
    - **Checkbox**: `{st.session_state.checkbox}`
    - **Radio**: {st.session_state.radio}
    - **Selectbox**: {st.session_state.selectbox}
    - **Multiselect**: {", ".join(st.session_state.multiselect)}
    """)

#Calculate score
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
#ACE Model page
def page_second():
    st.title('ACE Model')
    st.write('This is ACE part with 5 questions.')
    st.write('With each question, you have 5 choices from "totally disagree" to "totally agree"')

    #Answer list:
    choices = ['Totally Disagree','Disagree','Confused','Agree','Totally Agree']
    score_ace = 0
    score_tmp = 0
    # def calculate(score, question):
    #     score = 0
    #     if question == ('Totally Disagree'):
    #         score += 1
    #     elif question == ('Disagree'):
    #         score += 2
    #     elif question == ('Confused'):
    #         score += 3
    #     elif question == ('Agree'):
    #         score += 4
    #     else:
    #         score += 5 
    #     return score
    #Questions
    # st.write('1. Tôi biết chọn việc mà làm nên hiếm khi rơi vào trạng thái kiệt sức')
    q1 = st.radio('1. Tôi biết chọn việc mà làm nên hiếm khi rơi vào trạng thái kiệt sức', options= choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
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

    # pages = ['Page1','Page2','Page3']

# if os.path.isfile('next.p'):
#     next_clicked = pkle.load(open('next.p', 'rb'))
#     if next_clicked == len(pages):
#         next_clicked = 0 
# else:
#     next_clicked = 0 

# if next:
#     next_clicked = next_clicked+1
#     if next_clicked == len(pages):
#         next_clicked = 0 

# choice = st.sidebar.radio("Pages",('Page1','Page2', 'Page3'), index=next_clicked)
# pkle.dump(pages.index(choice), open('next.p', 'wb'))

# if choice == 'Page1':
#     st.title('Page 1')
# elif choice == 'Page2':
#     st.title('Page 2')
# elif choice == 'Page3':
#     st.title('Page 3')

# next = st.button('Go to next page')
#
def page_third():
    st.title("Self-Concept Mainteance")
    score_tmp = 0
    score_scm = 0

    choice1 = {'A':'Tôi là người trung thực trong mọi hoàn cảnh', 
    'B': 'Tôi trung thực trong hầu hết các hoàn cảnh',
    'C': 'Tôi có một danh sách việc gì phải trung thực, việc gì thì không nhất thiết',
    'D': 'Tôi không quan tâm đến tính trung thực']
    q1 = st.radio('1.Nhận định nào sau đây mô tả đúng nhất về bạn:', options= choice1.values())
    # score_tmp = calculate(score_tmp,q1)
    # score_scm += score_tmp
    if q1 == choice1.keys('1'):
        score_tmp += 4
    elif q1 == choice1.keys('2'):
        score_tmp += 3
    elif q1 == choice1.keys('3'):
        score_tmp += 2
    else:
        score_tmp += 1
    score_scm += score_tmp
    score_tmp = 0
    choice2 = ['Tôi dằn vặt trong đau khổ một thời gian dài','Tôi thấy dằn vặt nhưng nhanh chóng có lý do phù hợp cho việc đó','Tôi chấp nhận vì điều không trung thực đó trong phạm vi cho phép','Tôi không thấy có vấn đề gì']
    q2 = st.radio('2.Khi làm một điều gì đó thiếu trung thực, bạn thường:', options= choice2)
    score_tmp = calculate(score_tmp,q1)
    score_scm += score_tmp

    choice3 = ['Tôi thấy tệ về bản thân và quyết tâm không bao giờ làm lại hành vi đó nữa',
    'Tôi thấy khó chịu và tìm lý do để bào chữa',
    'Tôi xem xét lại việc thiếu trung thực và cho rằng nó là ngoại lệ có thể chấp nhận',
    'Tôi thấy không có vấn đề gì']
    q3 = st.radio('3.Bạn thường có xu hướng gì sau khi làm một hành vi thiếu trung thực:', options= choice3)
    score_tmp = calculate(score_tmp,q1)
    score_scm += score_tmp

    choice4 = ['Chắc chắn không làm dù lý do gì.'
    'Sẽ đắn đo và tìm lý do thuyết phục để làm việc đó hay không'
    'Sẽ xem lại việc này có nằm trong danh sách cho phép của tôi không',
    'Không cần phải đắn đo gì nhiều']
    q1 = st.radio('4.Đứng trước một cơ hội để thiếu trung thực (để có một lợi ích hoặc tránh một nỗi đau) nhưng không bị ai phát hiện, tôi sẽ:', options= choice4)
    score_tmp = calculate(score_tmp,q1)
    score_scm += score_tmp

def page_fourth():
    st.title("Open Mind")


def page_fifth():
    st.title("Motivation")


def page_sixth():
    st.title("Reflexivity")


if __name__ == "__main__":
    main()
    page_second()
    page_third()