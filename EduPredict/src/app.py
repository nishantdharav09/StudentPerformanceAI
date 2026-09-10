import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import matplotlib.pyplot as plt


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="EduPredict",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "student_performance_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error("❌ Model file could not be loaded.")
    st.info(f"Expected model location: {MODEL_PATH}")
    st.stop()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Main content width */
    .block-container {
        max-width: 1250px;
        padding-top: 35px;
        padding-bottom: 50px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Main headings */
    h1, h2, h3 {
        color: #172554 !important;
    }

    /* Normal text */
    p {
        color: #475569;
    }

    /* Input labels */
    div[data-testid="stNumberInput"] label {
        color: #172554 !important;
        font-weight: 700 !important;
    }

    /* Input boxes */
    div[data-testid="stNumberInput"] input {
        background-color: white !important;
        color: #111827 !important;
        border-radius: 10px !important;
        border: 1px solid #dbe3ef !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 12px;
        background-color: #2563eb !important;
        color: white !important;
        font-size: 17px;
        font-weight: 700;
        border: none;
    }

    .stButton > button:hover {
        background-color: #1d4ed8 !important;
        color: white !important;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }

    /* Success message */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("# 🎓 EduPredict")

    st.write("Student Performance AI")

    st.divider()

    st.subheader("🤖 Machine Learning")

    st.write("**Model**")
    st.write("Linear Regression")

    st.write("**Task**")
    st.write("Marks Prediction")

    st.write("**Framework**")
    st.write("Scikit-learn")

    st.divider()

    st.subheader("📊 Input Features")

    st.write("📚 Study Hours")
    st.write("📅 Attendance")
    st.write("📈 Previous Marks")
    st.write("📝 Assignment Score")
    st.write("📋 Internal Marks")
    st.write("🙋 Participation")


# ============================================================
# HEADER
# ============================================================

st.title("🎓 EduPredict")

st.subheader(
    "AI-Powered Student Performance Prediction System"
)

st.write(
    "Predict a student's final marks using academic "
    "performance and participation data."
)


# ============================================================
# ABOUT PROJECT
# ============================================================

st.divider()

st.header("📊 Predict Student Performance")

st.write(
    "EduPredict uses Machine Learning to estimate a student's "
    "final marks based on study hours, attendance, previous "
    "marks, assignment score, internal marks and participation."
)


# ============================================================
# STUDENT INFORMATION
# ============================================================

st.header("📝 Student Information")

st.write("Enter the student's academic details below.")


# ============================================================
# INPUT COLUMNS
# ============================================================

col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMN 1
# ============================================================

with col1:

    study_hours = st.number_input(
        "📚 Study Hours",
        min_value=0.0,
        max_value=24.0,
        value=5.0,
        step=0.5
    )

    attendance = st.number_input(
        "📅 Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        step=1.0
    )


# ============================================================
# COLUMN 2
# ============================================================

with col2:

    previous_marks = st.number_input(
        "📈 Previous Marks",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )

    assignment_score = st.number_input(
        "📝 Assignment Score",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=1.0
    )


# ============================================================
# COLUMN 3
# ============================================================

with col3:

    internal_marks = st.number_input(
        "📋 Internal Marks",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )

    participation = st.number_input(
        "🙋 Participation",
        min_value=0.0,
        max_value=10.0,
        value=7.0,
        step=1.0
    )


# ============================================================
# PREDICT BUTTON
# ============================================================

st.write("")

predict_button = st.button(
    "🚀 Predict Final Marks"
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    # Create student dataframe
    student = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_marks": [previous_marks],
        "assignment_score": [assignment_score],
        "internal_marks": [internal_marks],
        "participation": [participation]
    })


    # Prediction
    prediction = model.predict(student)

    final_marks = float(prediction[0])

    # Keep result between 0 and 100
    final_marks = max(
        0,
        min(100, final_marks)
    )


    # Performance category

    if final_marks >= 75:

        performance = "🌟 Excellent"
        message = "Excellent academic performance!"

    elif final_marks >= 60:

        performance = "👍 Good"
        message = "Good academic performance!"

    elif final_marks >= 40:

        performance = "📚 Average"
        message = "Average performance. Keep improving!"

    else:

        performance = "⚠️ Needs Improvement"
        message = "More academic improvement is recommended."


    # ========================================================
    # PREDICTION RESULT
    # ========================================================

    st.divider()

    st.header("🎯 Prediction Result")


    result_col1, result_col2, result_col3 = st.columns(3)


    with result_col1:

        st.metric(
            "🎯 Predicted Final Marks",
            f"{final_marks:.2f} / 100"
        )


    with result_col2:

        st.metric(
            "📊 Performance",
            performance
        )


    with result_col3:

        st.metric(
            "🤖 ML Model",
            "Linear Regression"
        )


    st.success(message)


    # ========================================================
    # AREAS TO IMPROVE
    # ========================================================

    st.subheader("📌 Areas to Improve")

    improvements = []

    if study_hours < 4:
        improvements.append(
            "📚 Increase study hours and follow a regular study schedule."
        )

    if attendance < 75:
        improvements.append(
            "📅 Improve attendance and attend classes regularly."
        )

    if previous_marks < 60:
        improvements.append(
            "📈 Improve previous academic performance through regular revision."
        )

    if assignment_score < 60:
        improvements.append(
            "📝 Focus more on assignments and complete them on time."
        )

    if internal_marks < 60:
        improvements.append(
            "📋 Improve internal marks by preparing well for tests and exams."
        )

    if participation < 5:
        improvements.append(
            "🙋 Participate more actively in class activities."
        )

    if improvements:

        for suggestion in improvements:
            st.warning(suggestion)

    else:

        st.success(
            "🌟 No major improvement area found. "
            "Keep maintaining your performance!"
        )


    # ========================================================
    # PERFORMANCE PROGRESS
    # ========================================================

    st.subheader("📈 Performance Score")

    st.progress(
        int(final_marks)
    )


    # ========================================================
    # GRAPH
    # ========================================================

    st.subheader("📊 Academic Performance Overview")

    graph_data = pd.DataFrame({
        "Feature": [
            "Previous Marks",
            "Assignment Score",
            "Internal Marks",
            "Attendance"
        ],
        "Score": [
            previous_marks,
            assignment_score,
            internal_marks,
            attendance
        ]
    })


    fig, ax = plt.subplots(figsize=(10, 4))

    ax.bar(
        graph_data["Feature"],
        graph_data["Score"]
    )

    ax.set_ylim(0, 100)

    ax.set_ylabel("Score")

    ax.set_title(
        "Student Academic Performance"
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )

    plt.xticks(
        rotation=15
    )

    plt.tight_layout()

    st.pyplot(fig)


    # ========================================================
    # STUDENT SUMMARY
    # ========================================================

    st.subheader("📋 Student Summary")


    summary1, summary2, summary3 = st.columns(3)


    with summary1:

        st.metric(
            "📚 Study Hours",
            f"{study_hours} hrs"
        )

        st.metric(
            "📅 Attendance",
            f"{attendance}%"
        )


    with summary2:

        st.metric(
            "📈 Previous Marks",
            f"{previous_marks}"
        )

        st.metric(
            "📝 Assignment Score",
            f"{assignment_score}"
        )


    with summary3:

        st.metric(
            "📋 Internal Marks",
            f"{internal_marks}"
        )

        st.metric(
            "🙋 Participation",
            f"{participation}/10"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎓 EduPredict | AI-Powered Student Performance Prediction | "
    "Python • Pandas • Scikit-learn • Streamlit"
)