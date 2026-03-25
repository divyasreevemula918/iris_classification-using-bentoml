# 🌸 Iris Classification using BentoML

## 📌 Project Overview
This project is a **Machine Learning API service** that classifies Iris flowers into one of three species — **Setosa, Versicolor, or Virginica** — using a trained classification model and **BentoML** for model serving.

It demonstrates a simple end-to-end workflow:
- train a machine learning model
- save and package the model
- serve predictions through a BentoML API
- test the prediction service locally

---

## 🌐 Live Deployment
👉 Deployment Link: **https://iris-classification-using-bentoml-6.onrender.com**

Example:
`https://your-bentoml-service-link.com`

> Replace the above with your real deployed API/service link.

---

## 🚀 Features
- Predict Iris flower species 🌸
- Machine Learning model trained on Iris dataset
- API-based serving using BentoML
- Clean project structure
- Easy local setup and testing
- Ready for deployment and further extension

---

## 🧠 Tech Stack
- Python 🐍
- Scikit-learn
- Pandas
- BentoML

---

## 📂 Project Structure
iris_classification-using-bentoml/
│
├── bentofile.yaml        # BentoML build configuration
├── service.py            # BentoML service API
├── train.py              # Model training script
├── test.py               # Testing script
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

---

## ❓ Problem Statement
Given the measurements of an Iris flower:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

the goal is to predict its species:
- Setosa
- Versicolor
- Virginica

This is a classic multiclass classification problem in machine learning.

---
## screenshot
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/57f3ce8a-0764-4606-99fc-bd5f6488eeaf" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/187e2c39-d43b-4347-b00b-a03748ee0162" />


## 📥 Input Features
The model takes the following numeric inputs:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Example Input
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
