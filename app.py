import streamlit as st
import pandas as pd
from database import add_student, get_students
from services import calculate_grade, calculate_statistics

st.title("🎓 Student Performance Dashboard")

# Yeni tələbə əlavə etmə formu
st.header("Yeni Tələbə Əlavə Et")
with st.form("student_form"):
    name = st.text_input("Student Name")
    score = st.number_input("Score", min_value=0.0, max_value=100.0, step=1.0)

    submitted = st.form_submit_button("Add Student")
    if submitted and name.strip() != "":
        add_student(name, score)
        st.success("Tələbə uğurla əlavə edildi!")
        st.rerun()

st.divider()

# Axtarış və Siyahı
st.header("Tələbələrin Siyahısı")
search = st.text_input("Search Student (Ada görə axtar)")
raw_data = get_students(search)

# Grade hesablamasını siyahıya əlavə etmək
data = []
for s in raw_data:
    # sqlite3 məlumatı (Name, Score) tuple kimi qaytarır: s[0] = Name, s[1] = Score
    student_name = s[0]
    student_score = s[1]
    grade = calculate_grade(student_score)
    data.append({
        "Name": student_name,
        "Score": student_score,
        "Grade": grade
    })

if data:
    st.dataframe(pd.DataFrame(data), use_container_width=True)
else:
    st.info("Heç bir məlumat tapılmadı.")