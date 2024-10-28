import random
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Set up the Streamlit page configuration
st.set_page_config(page_title="ยินดีต้อนรับสู่เกมทบทวนสำนวนและสุภาษิตในภาษาไทย", page_icon=":tada:", layout="wide")

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/c2756719-9be5-4c98-be83-4b33ab163e4c/uPslLdvkRF.json")

# Introduction section
with st.container():
    st.subheader("นี้คือเกมที่ทบทวนสำนวนและสุภาษิต")
    st.title("ชึ่งจะทบทวนให้คุณได้เข้าใจอย่างนอน")
    st.write("โครงงานภาษาไทยนี้จัดทำขึ้นโดย ด.ช.ชิษณุพงศ์ โรจนเสาวภาคย์ ชั้น ม.1/7")

# Game section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("เกมทบทวนสำนวนและสุภาษิตในภาษาไทย")
        st.write("##")
        st.subheader("ลองเล่นได้เลย")

        # Initialize session state
        if 'score' not in st.session_state:
            st.session_state.score = 0
            st.session_state.current_proverb_index = 0
            st.session_state.proverbs = [
                ('ไก่เห็นตีนงู งูเห็นนมไก่', 'คนเข้าใจความลับของกันและกัน'),
                ('น้ำกลิ้งบนใบบอน', 'การผัดวันประกันพรุ่ง'),
                ('จับปลาสองมือ', 'พยายามทำสองสิ่งในครั้งเดียว'),
                ('ปิดทองหลังพระ', 'ทำดีโดยไม่หวังผลตอบแทน'),
                ('ตีงูให้หลัง', 'ทำร้ายคนที่ช่วยเรา'),
                ('ปลาหมออยู่ในน้ำ', 'มีสิ่งที่ควรรู้ในแต่ละสถานการณ์'),
                ('พูดมากหายาก', 'คนที่พูดมากอาจไม่พูดจริง'),
                ('เหรียญสองด้าน', 'มีทั้งด้านดีและด้านไม่ดี'),
                ('นกสองหัว', 'คนที่มีหลายบุคลิก'),
                ('บัวไม่ให้ช้ำ น้ำไม่ให้ขุ่น', 'ไม่ทำให้ใครเดือดร้อน'),
            ]
            random.shuffle(st.session_state.proverbs)

        if st.button("เริ่มเกม"):
            st.session_state.score = 0
            st.session_state.current_proverb_index = 0

        # Check if the game is in progress
        if st.session_state.current_proverb_index < len(st.session_state.proverbs):
            proverb, correct_meaning = st.session_state.proverbs[st.session_state.current_proverb_index]
            st.write(f"สุภาษิต: {proverb}")

            # Create choices if not already created
            if 'choices' not in st.session_state:
                choices = [correct_meaning]
                while len(choices) < 4:
                    meaning = random.choice(st.session_state.proverbs)[1]
                    if meaning not in choices:
                        choices.append(meaning)
                random.shuffle(choices)
                st.session_state.choices = choices
            else:
                choices = st.session_state.choices

            # Display choices and capture user answer
            answer = st.radio("เลือกความหมายที่ถูกต้อง:", choices, key=f"answer_{st.session_state.current_proverb_index}")

            # Use unique keys for the buttons
            if st.button("ส่งคำตอบ", key=f"submit_{st.session_state.current_proverb_index}"):
                if answer == correct_meaning:
                    st.success("ถูกต้อง!")
                    st.session_state.score += 1
                else:
                    st.error(f"ไม่ถูกต้อง! ความหมายที่ถูกต้องคือ: {correct_meaning}")

                # Move to the next proverb
                st.session_state.current_proverb_index += 1
                # Clear choices for the next round
                del st.session_state.choices

        # Display final score when all proverbs have been answered
        if st.session_state.current_proverb_index == len(st.session_state.proverbs):
            st.subheader(f"เกมจบ! คะแนนของคุณคือ: {st.session_state.score}/{len(st.session_state.proverbs)}")

    with right_column:
        st_lottie(lottie_coding, height=400, key="learning_languages")
