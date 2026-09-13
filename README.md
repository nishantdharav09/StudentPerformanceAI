# 🎓 EduPredict

## AI-Powered Student Performance Prediction System

EduPredict is a Machine Learning project that predicts a student's final marks based on academic performance and participation data.

## 🚀 Features

- 📚 Study Hours based prediction

- 📅 Attendance analysis

- 📈 Previous Marks consideration

- 📝 Assignment Score analysis

- 📋 Internal Marks consideration

- 🙋 Participation analysis

- 🎯 Final Marks Prediction

- 📊 Performance Category

- 📌 Areas to Improve suggestions

- 🌐 Interactive Streamlit Web Application

## 🤖 Machine Learning

**Algorithm:** Linear Regression

### Input Features

- Study Hours

- Attendance

- Previous Marks

- Assignment Score

- Internal Marks

- Participation

### Target

Final Marks

## 🛠️ Technologies Used

- Python

- Pandas

- NumPy

- Matplotlib

- Scikit-learn

- Streamlit

- Joblib

## 📂 Project Structure


EduPredict/

│

├── data/

│   ├── student\_performance.csv

│   └── student\_performance\_500.csv

├── src/

│   ├── app.py

│   ├── data\_cleaning.py

│   ├── data\_analysis.py

│   ├── generate\_dataset.py

│   ├── train\_model.py

│   └── test\_model.py

│

├── student\_performance\_model.pkl

├── requirements.txt

└── README.md





▶️ How to Run

Option 1:-

1\. Install required libraries

pip install -r requirements.txt

2\. Run the application

python -m streamlit run src/app.py

Option 2:- Go to the GitHub repository, download the ZIP file, extract all the files, and double-click run_app.bat to run the project.
  
📊 How It Works

Student enters academic details.

The Machine Learning model receives the input.

The model predicts final marks.

EduPredict displays the predicted marks.

The application shows the performance category.

The application provides areas that may need improvement.

🎯 Project Objective



The objective of EduPredict is to demonstrate how Machine Learning can be used to analyze student academic data and predict final performance through an easy-to-use web application.



👨‍💻 Author

Nishant Dharav
