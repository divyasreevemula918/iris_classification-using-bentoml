# 🌸 Iris Classification using BentoML

🚀 A production-ready Machine Learning project that classifies Iris flowers using a trained model and serves predictions via **BentoML API**.

---

## 📌 Project Overview

This project demonstrates how to:

* Train a Machine Learning model on the Iris dataset 🌼
* Save and version the model
* Serve predictions using **BentoML**
* Build a simple and scalable ML service

---

## 🧠 Problem Statement

Given features of a flower:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

👉 Predict the species:

* Setosa 🌸
* Versicolor 🌿
* Virginica 🌺

---

## 🛠️ Tech Stack

* 🐍 Python
* 🤖 Scikit-learn
* 📊 Pandas
* 📦 BentoML

---

## 📂 Project Structure

```
MLService/
│── bentofile.yaml        # BentoML build config
│── service.py            # API service
│── train.py              # Model training script
│── test.py               # Testing script
│── requirements.txt      # Dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/divyasreevemula918/iris_classification-using-bentoml.git
cd iris_classification-using-bentoml
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 🏋️‍♂️ Train the Model

```
python train.py
```

👉 This will:

* Train the model
* Save it using BentoML

---

## 🚀 Build BentoML Service

```
bentoml build
```

---

## 🌐 Run the API Service

```
bentoml serve
```

👉 Open in browser:

```
http://127.0.0.1:3000
```

---

## 📥 Example Input

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

---

## 📤 Example Output

```json
{
  "prediction": "setosa"
}
```

---
## output
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8d5ac79f-eaea-4c85-a1c1-339d181329a8" />



## 🎯 Key Features

✨ Simple ML pipeline
✨ Model serving using BentoML
✨ Clean project structure
✨ Ready for deployment

---

## 🔥 Future Improvements

* Add UI (Streamlit / React) 🎨
* Deploy on AWS / Docker ☁️
* Add model monitoring 📊

---

## 👩‍💻 Author

**Divya Sree Vemula**
💼 Aspiring ML Engineer

---

## ⭐ Support

If you like this project:
👉 Give it a ⭐ on GitHub
👉 Share with others 🚀

---
