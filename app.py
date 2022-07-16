import streamlit as st


def wj(x):
    if x <= 2:
        return x
    elif x <= 10:
        return x - 2
    elif x <= 18:
        return x - 10
    elif x <= 20:
        return x - 18
    elif x > 20:
        return st.warning('20이하의 원소를 입력해 주세요.')
        ValueError


def wjp(x):
    if x < 5:
        return -x
    else:
        return 8 - x

wl = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]

snl = ["", "₂", "₃", "₄"]

save = list()

st.title('ㅤㅤ ㅤㅤㅤㅤ   NEON')

menu = st.sidebar.selectbox('메뉴',
options=['회원가입','원소 결합시키기','원소 검색'])

if menu == '회원가입':
    st.subheader('회원가입 폼')
    with st.form('my_form', clear_on_submit=True):
        uid = st.text_input('ID', max_chars=12)
        upw = st.text_input('PW', type='password')
        upw_chk = st.text_input('비밀번호 확인', type='password')
        usex = st.radio('SEX', options=['남', '여'], horizontal=True)

        submitted = st.form_submit_button('제출')
        if submitted :

            if upw != upw_chk :
                st.warning('비밀번호가 일치하지 않습니다   :(')
                st.stop()


elif menu == '원소 결합시키기':
    st.subheader('원소 결합시키기')
    st.caption('20이하의 원소 번호를 숫자로 입력해 주세요')
    with st.form('my_um_form', clear_on_submit=True):
        col1, col2, col3 = st.columns(3)

        with col1 :
            emp_wa = st.empty
            wa = (st.text_input('결합시킬 첫 번재 원소 번호를 입력해 주세요', max_chars=3))

        with col2 :
            st.title('ㅤㅤ+')

        with col3 :
            emp_wb = st.empty
            wb = (st.text_input('결합시킬 두 번재 원소 번호를 입력해 주세요', max_chars=3))


        submitted = st.form_submit_button('제출')
        if submitted :
            wa = int(wa)
            wb = int(wb)

            for a in range(1, 5):
                out = False
                for b in range(1, 5):
                    if wjp(wj(wa)) * a + wjp(wj(wb)) * b == 0:
                        if wjp(wj(wa)) < 0:
                            st.info(wl[wa - 1] + snl[a - 1] + wl[wb - 1] + snl[b - 1])
                        else:
                            st.info(wl[wb - 1] + snl[b - 1] + wl[wa - 1] + snl[a - 1])
                        out = True
                        break
                if out:
                    break

            for i in range(0, 20):
                if wl[wa - 1] == sorted(wl)[i]:
                    waa = i

            for i in range(0, 20):
                if wl[wb - 1] == sorted(wl)[i]:
                    wba = i

            for a in range(1, 8):
                out = False
                for b in range(1, 8):
                    if wjp(wj(wa)) * a == wjp(wj(wb)) * b:
                        if wl[wa - 1] == "N" and wl[wb - 1] == "H" or wl[wb - 1] == "N" and wl[wa - 1] == "H":
                            st.info("NH₃")
                        elif wa == wb:
                            st.info(wl[wa - 1] + "²")
                        elif waa < wba:
                            st.info(wl[wa - 1] + snl[a - 1] + wl[wb - 1] + snl[b - 1])
                        else:
                            st.info(wl[wb - 1] + snl[b - 1] + wl[wa - 1] + snl[a - 1])
                        out = True
                        break
                if out:
                    break


elif menu == '원소 검색':
    st.subheader('원소를 검색해보세요')
    wanso = st.text_input('원소를 검색하세요')
    col4, col5 = st.columns(2)
    with col4 :
        search = st.button('검색')
    with col5 :
        init = st.button('초기화')







