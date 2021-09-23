from os import write
import streamlit as st
import numpy as np
import pickle as pkle
import os.path

#Answer list:
choices = ['Totally Disagree','Disagree','Confused','Agree','Totally Agree']
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
    score_scm = 0

    choice1 = {'A':'Tôi là người trung thực trong mọi hoàn cảnh', 
    'B': 'Tôi trung thực trong hầu hết các hoàn cảnh',
    'C': 'Tôi có một danh sách việc gì phải trung thực, việc gì thì không nhất thiết',
    'D': 'Tôi không quan tâm đến tính trung thực'}
    q1 = st.radio('1.Nhận định nào sau đây mô tả đúng nhất về bạn:', options= choice1.values())
    # score_tmp = calculate(score_tmp,q1)
    # score_scm += score_tmp
    # Calculate function for Self-concept maintenance
    def cal (score, question, choice):
        score = 0
        if question == choice['A']:
            score += 4
        elif question == choice['B']:
            score += 3
        elif question == choice['C']:
            score += 2
        else:
            score += 1
        return score

    score_scm += cal(score_scm,q1,choice1)

    choice2 = {'A':'Tôi dằn vặt trong đau khổ một thời gian dài',
    'B':'Tôi thấy dằn vặt nhưng nhanh chóng có lý do phù hợp cho việc đó',
    'C':'Tôi chấp nhận vì điều không trung thực đó trong phạm vi cho phép',
    'D':'Tôi không thấy có vấn đề gì'}
    q2 = st.radio('2.Khi làm một điều gì đó thiếu trung thực, bạn thường:', options= choice2.values())
    score_scm += cal(score_scm,q2,choice2)

    choice3 = {'A':'Tôi thấy tệ về bản thân và quyết tâm không bao giờ làm lại hành vi đó nữa',
    'B':'Tôi thấy khó chịu và tìm lý do để bào chữa',
    'C':'Tôi xem xét lại việc thiếu trung thực và cho rằng nó là ngoại lệ có thể chấp nhận',
    'D':'Tôi thấy không có vấn đề gì'}
    q3 = st.radio('3.Bạn thường có xu hướng gì sau khi làm một hành vi thiếu trung thực:', options= choice3.values())
    score_scm += cal(score_scm,q3,choice3)
    st.write('Score: ',score_scm)

    choice4 = {'A':'Chắc chắn không làm dù lý do gì.',
    'B':'Sẽ đắn đo và tìm lý do thuyết phục để làm việc đó hay không',
    'C':'Sẽ xem lại việc này có nằm trong danh sách cho phép của tôi không',
    'D':'Không cần phải đắn đo gì nhiều'}
    q4 = st.radio('4.Đứng trước một cơ hội để thiếu trung thực (để có một lợi ích hoặc tránh một nỗi đau) nhưng không bị ai phát hiện, tôi sẽ:', options= choice4.values())
    score_scm += cal(score_scm,q4,choice4)

    st.write('Score: ',score_scm)

def page_fourth():
    st.title("Open Mind")
    score_om = 0
    q1 = st.radio('1. Tôi tôn trọng các suy nghĩ, góc nhìn của người khác khi cùng đối diện một vấn đề.', options= choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_om += calculate(score_om,q1)
    q2 = st.radio('2. Tôi sẵn sàng thay đổi quan điểm, góc nhìn của mình nếu có đủ dẫn chứng thuyết phục.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_tmp = calculate(score_om,q2)
    score_om += score_tmp

    q3 = st.radio('3. Khi người khác bảo rằng ý kiến của tôi là sai, tôi không cảm thấy khó chịu.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_om += calculate(score_om,q3)


    q4 = st.radio('4. Tôi sẵn sàng lắng nghe ý kiến của người khác, ngay cả khi quan điểm của họ có thể trái ngược với tôi.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_om += calculate(score_om,q4)

    q5 = st.radio('5. Tôi thường cho rằng ý kiến của mình có thể sai.',options=choices)
    score_om += calculate(score_om,q5)
    st.write('Score: ',score_om)
    if score_om >= 14 and st.button('Submit'):
        page_seventh()

def page_fifth():
    st.title("Motivation")

    score_mov = 0
    #Questions
    q1 = st.radio('1. Khả năng chịu đựng áp lực học tập/công việc của tôi cao.', options= choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_mov += calculate(score_mov,q1)

    q2 = st.radio('2. Tôi sẵn sàng làm thêm giờ để hoàn thành công việc mà không cần ai ép buộc.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_mov += calculate(score_mov,q2)

    q3 = st.radio('3. Tôi kiên định với mục tiêu mà bản thân đặt ra, dù nó có thể đi ngược lại ý kiến của người khác.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_mov += calculate(score_mov,q3)


    q4 = st.radio('4. Những lợi ích vật chất KHÔNG là động lực lớn nhất của tôi.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_mov += calculate(score_mov,q4)

    q5 = st.radio('5. Tôi phấn đấu nỗ lực không chỉ vì chức danh, địa vị của mình.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_mov += calculate(score_mov,q5)

    q6 = st.radio('6. Tôi thích khoe những thành tích của tôi lên mạng xã hội.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_mov += calculate(score_mov,q6)
    st.write('Score: ',score_mov)

def page_sixth():
    st.title("Reflexivity")
    score_ref = 0 #score for reflexivity
     #Questions
    q1 = st.radio('1. Tôi hiếm khi xem xét lại góc nhìn, hướng xử lý của mình khi giải quyết vấn đề.', options= choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ref += calculate(score_ref,q1)

    q2 = st.radio('2. Tôi luôn phân loại mọi thứ theo tiêu chuẩn tốt - xấu, đúng sai rõ ràng.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ref += calculate(score_ref,q2)

    q3 = st.radio('3. Khi có ai đó chỉ ra điểm không hợp lý trong hệ thống niềm tin của tôi, tôi có xu hướng nghi ngờ với nhận định đó thay vì tìm hiểu thêm về nó.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ref += calculate(score_ref,q3)


    q4 = st.radio('4. Tôi tin rằng bất kỳ vấn đề nào cũng có một giải pháp hoàn hảo.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ref += calculate(score_ref,q4)

    q5 = st.radio('5. Khi tôi đã quyết định đưa ra một giải pháp, tôi thường thực thi đến cùng thay vì cân nhắc, kiểm chứng lại.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ref += calculate(score_ref,q5)

    q6 = st.radio('6. Tôi có những nguyên tắc đạo đức làm nền tảng và hiếm khi chất vấn chúng.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ref += calculate(score_ref,q6)
    st.write('Score: ',score_ref)


def page_seventh():
    st.title("Open Heart and Open Will")
    st.text('This is second level of Open Mind. There are 2 parts of this level: Open Heart and Open Will')
    st.text("Now, let's get started")

    score_oh = 0
    score_ow = 0
    q1 = st.radio('1. Là người lãnh đạo, tôi sẵn lòng trao quyền cho người phù hợp khi cần.', options= choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_oh += calculate(score_oh,q1)
    q2 = st.radio('2. Khi người khác nói tôi đã sai, tôi dễ dàng chấp nhận chuyện đó.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_oh += calculate(score_oh,q2)

    q3 = st.radio('3. Khi lãnh đạo đội nhóm, tôi sẵn sàng chia sẻ những khó khăn của cá nhân mình.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_oh += calculate(score_oh,q3)


    q4 = st.radio('4. Tôi có thể nhìn thấy những điều hay nơi người khác để học hỏi.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_oh += calculate(score_oh,q4)

    q5 = st.radio('5. Tôi thường lắng nghe người khác chia sẻ mà không nghi ngờ.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_oh += calculate(score_oh,q5)

    q6 = st.radio('6. Tôi thường lắng nghe người khác chia sẻ mà không nghi ngờ.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_oh += calculate(score_oh,q6)
    st.write('Score: ',score_oh)

    #Open Will
    q1 = st.radio('1. Trong trường hợp cấp bách, tôi chấp nhận ra quyết định khi không đủ thông tin hơn là trì hoãn để thu thập thêm thông tin.', options= choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ow += calculate(score_ow,q1)

    q2 = st.radio('2. Trong công việc, tôi thường tìm kiếm những cách thức mới thay vì chọn những giải pháp sẵn có.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ow += calculate(score_ow,q2)

    q3 = st.radio('3. Tôi thường xem xét lại để cải tiến phương pháp làm việc của mình.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ow += calculate(score_ow,q3)


    q4 = st.radio('4. Tôi thường tìm kiếm những cơ hội phát triển mới hơn là chọn công việc ổn định.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ow += calculate(score_ow,q4)

    q5 = st.radio('5. Tôi thường để các thành viên trong đội nhóm tự do trình bày ý tưởng của mình.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ow += calculate(score_ow,q5)

    q6 = st.radio('6. Khi đứng trước cơ hội mới, tôi sẵn sàng đón nhận dù biết rằng mình có thể thất bại.',options=choices)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    score_ow += calculate(score_ow,q6)
    st.write('Score: ',score_ow)



if __name__ == "__main__":
    main()
    page_second()
    page_third()
    page_fourth()