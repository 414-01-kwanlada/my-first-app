import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มตรวจข้อ 3, 4 ตรงนี้

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 2:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2

# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4 ตรงนี้


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    # 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📩 ส่งคำตอบ"):
        st.session_state.is_ended = True
        time.sleep(1)
        st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2)

st.divider()
st.write("นางสาวขวัญลดา อุดโน เลขที่ 1 ม.4/14")
st.title("🎮 เกมเติมคำศัพท์ภาษาอังกฤษ")

# 1. เพิ่มการกำหนดค่าเริ่มต้นใน session_state ans3_val และ ans4_val
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

# ปุ่มเริ่มใหม่ / เคลียร์ค่า
if st.button("🔄 เริ่มเกมใหม่"):
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    # 2. เพิ่มการเคลียร์ค่าเมื่อกดปุ่มใหม่ st.session_state.ans3_val และ st.session_state.ans4_val
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.is_ended = False
    st.rerun()

st.session_state.start = True

# 6. เพิ่มช่องรับตอบ ans3 = st.text_input และ ans4 = st.text_input
ans1 = st.text_input("1. Apple แปลว่าอะไร?", value=st.session_state.ans1_val, key="input_ans1")
ans2 = st.text_input("2. Banana แปลว่าอะไร?", value=st.session_state.ans2_val, key="input_ans2")
ans3 = st.text_input("3. Cat แปลว่าอะไร?", value=st.session_state.ans3_val, key="input_ans3")
ans4 = st.text_input("4. Dog แปลว่าอะไร?", value=st.session_state.ans4_val, key="input_ans4")

# 7. เพิ่มการอัปเดตล่าสุดเข้าตัวแปร st.session_state.ans3_val = ans3 และ st.session_state.ans4_val = ans4
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# 8. เพิ่มการแสดง Dialog ผลลัพธ์ ans3, ans4
@st.dialog("📊 สรุปผลคะแนน")
def show_result_dialog(a1, a2, a3, a4):
    # 3. สรุปผลการเล่นเกมใน MessageBox u_ans3 = ans3.strip().lower() และ u_ans4 = ans4.strip().lower()
    u_ans1 = a1.strip().lower()
    u_ans2 = a2.strip().lower()
    u_ans3 = a3.strip().lower()
    u_ans4 = a4.strip().lower()

    score = 0
    if u_ans1 in ["แอปเปิ้ล", "แอปเปิ้ล"]: score += 1
    if u_ans2 in ["กล้วย"]: score += 1
    # 4. เพิ่มข้อ 3 และตรวจข้อ 4
    if u_ans3 in ["แมว"]: score += 1
    if u_ans4 in ["สุนัข", "หมา"]: score += 1

    st.write(f"คะแนนที่คุณได้: **{score} / 4**")
    
    # 5. เพิ่มคะแนน score == 4
    if score == 4:
        st.success("🎉 เก่งมาก! คุณตอบถูกหมดทุกข้อ")
    else:
        st.info("พยายามอีกนิดนะ!")

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📩 ส่งคำตอบ"):
        st.session_state.is_ended = True
        time.sleep(1)
        st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
st.write("นางสาวขวัญลดา อุดโน เลขที่ 1 ม.4/14")
