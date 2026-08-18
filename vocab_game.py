import time
import streamlit as st

st.title("🎮 เกมเติมคำศัพท์ภาษาอังกฤษ")

# ---------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state
# ---------------------------------------------
defaults = {
    "ans1_val": "",
    "ans2_val": "",
    "ans3_val": "",
    "ans4_val": "",
    "start": None,
    "is_ended": True,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ---------------------------------------------
# 2. ฟังก์ชันเริ่มเกมใหม่
# ---------------------------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ---------------------------------------------
# 3. Dialog แสดงผลคะแนน
# ---------------------------------------------
@st.dialog("📊 สรุปผลคะแนน")
def show_result_dialog(a1, a2, a3, a4):

    u_ans1 = a1.strip().lower()
    u_ans2 = a2.strip().lower()
    u_ans3 = a3.strip().lower()
    u_ans4 = a4.strip().lower()

    score = 0

    # ข้อ 1
    if u_ans1 == "แอปเปิ้ล":
        st.success("✅ ข้อ 1 ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1 ผิด — คำตอบที่ถูกคือ แอปเปิ้ล")

    # ข้อ 2
    if u_ans2 == "กล้วย":
        st.success("✅ ข้อ 2 ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2 ผิด — คำตอบที่ถูกคือ กล้วย")

    # ข้อ 3
    if u_ans3 == "แมว":
        st.success("✅ ข้อ 3 ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3 ผิด — คำตอบที่ถูกคือ แมว")

    # ข้อ 4
    if u_ans4 in ["สุนัข", "หมา"]:
        st.success("✅ ข้อ 4 ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4 ผิด — คำตอบที่ถูกคือ สุนัข หรือ หมา")

    # แสดงคะแนน
    st.info(f"🏆 คะแนนที่คุณได้: **{score} / 4 คะแนน**")

    if score == 4:
        st.balloons()
        st.success("🎉 เก่งมาก! คุณตอบถูกหมดทุกข้อ")
    elif score >= 2:
        st.warning("👍 ทำได้ดี! พยายามอีกนิดนะ")
    else:
        st.error("💪 พยายามอีกครั้งนะ!")


# ---------------------------------------------
# 4. ปุ่มเริ่มเกมใหม่
# ---------------------------------------------
if st.button("🎮 เริ่มเกมใหม่", type="primary"):
    reset_game()
    st.rerun()


# ---------------------------------------------
# 5. แสดงเวลานับถอยหลัง
# ---------------------------------------------
if st.session_state.start is not None and not st.session_state.is_ended:

    elapsed = time.time() - st.session_state.start
    time_left = max(0, int(30 - elapsed))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ---------------------------------------------
# 6. ช่องตอบคำถาม
# ---------------------------------------------
ans1 = st.text_input(
    "1. Apple แปลว่าอะไร? 🍎",
    value=st.session_state.ans1_val,
)

ans2 = st.text_input(
    "2. Banana แปลว่าอะไร? 🍌",
    value=st.session_state.ans2_val,
)

ans3 = st.text_input(
    "3. Cat แปลว่าอะไร? 🐱",
    value=st.session_state.ans3_val,
)

ans4 = st.text_input(
    "4. Dog แปลว่าอะไร? 🐶",
    value=st.session_state.ans4_val,
)


# ---------------------------------------------
# 7. เก็บคำตอบล่าสุด
# ---------------------------------------------
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# ---------------------------------------------
# 8. ปุ่มส่งคำตอบ
# ---------------------------------------------
if st.session_state.start is not None and not st.session_state.is_ended:

    if st.button("📩 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()


# ---------------------------------------------
# 9. แสดง Dialog เมื่อจบเกม
# ---------------------------------------------
if st.session_state.is_ended and st.session_state.start is not None:
    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val,
    )


# ---------------------------------------------
# 10. ชื่อผู้จัดทำ
# ---------------------------------------------
st.divider()
st.write("นางสาวขวัญลดา อุดโน เลขที่ 1 ม.4/14")
