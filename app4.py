# UI 함수들 (버튼 등등)

import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('./data/iris.csv')

    # 버튼 만들기
    # 유저가 버튼을 누르면 데이터프레임을 보여준다.
    if st.button('데이터 보기'):
        st.dataframe(df)

    # '대문자' 버튼을 만들고,
    # 버튼을 누르면, species 컬럼의 값들을 대문자로
    # 변경한 데이터 프레임을 화면에 보여주세요.
    if st.button('대문자'):
        st.dataframe(df['species'].str.upper())
    else:
        st.text('아무것도 안 눌렀습니다.')

    # 라디오 버튼 : 여러 개 중에서 한 개 선택하게 할 때
    my_order = ['오름차순 정렬', '내림차순 정렬']
    status = st.radio('정렬 방법을 선택하세요.', my_order)

    # print(status)

    # petal_length 컬럼으로 정렬해서 df 보여준다.
    if status == my_order[0]:
        st.dataframe(df.sort_values('petal_length', ascending=True))
    elif status == my_order[1]:
        st.dataframe(df.sort_values('petal_length', ascending=False))

    # 체크박스 : 둘 중에 하나만 선택하게끔 만들 때 (체크/해제)
    # 체크하면 헤드 5개 보여주고, 해제하면 안 보여주도록.
    if st.checkbox('헤드 5개 보기', True):
        st.dataframe(df.head())

    # 셀렉트박스 : 여러 개에서 한 개만 고르게 하되
    #             리스트가 많을 때 사용한다.
    language = ['Python', 'C', 'Java', 'Go', 'PHP', 'Dart']
    
    my_choice = st.selectbox('좋아하는 언어 선택', options=language)
    if my_choice == language[0] or my_choice == language[2]:
        st.text('정말 재미있는 언어입니다....')
    elif my_choice == language[3] or my_choice == language[5]:
        st.text('배우고 싶습니다......')
    else:
        st.text('오래된 언어입니다.....')    

    # 멀티셀렉트 : 여러 개 중에서 여러 개를 선택하게 할 때

    # 유저가 선택한 컬럼을 데이터프레임으로 보여주되
    # 아무것도 선택 안하면, 아무것도 나오지 않게 하시오.
    choice_list = st.multiselect('원하는 컬럼을 선택하세요', df.columns)
    if choice_list:
        st.dataframe(df[choice_list])
    else:
        pass
    
    # 1. if len(choice_list) == 0:
    #         st.dataframe(df[choice_list])
    #    else:
    #         st.write()
    # 2. if len(choice_list) != 0:
    #         st.dataframe(df[choice_list])
    #    else:
    #         st.write()
    # 3. if choice_list == []:
    #         st.dataframe(df[choice_list])
    #    else:
    #         st.write()
    

    # 슬라이더 : 숫자 조정하는데 주로 사용
    st.slider('데이터 선택', -5.0, 10.5, 0.0, 0.5)

    # 나이를 슬라이더로 입력받는다.
    # 1세부터 120세 까지 입력받을 수 있도록 한다.
    # 선택한 나이가 웹 화면에 출력되도록 한다.  ex) "선택한 나이는 33세 입니다."
    age = st.slider('나이를 입력해주세요', 1, 120, 1, 1)
    st.info(f'선택한 나이는 {age}세 입니다.')

    # 익스펜더
    with st.expander('Hello'):
        st.text('데이터 프레임 입니다.')
        st.dataframe(df)

if __name__ == '__main__':
    main()