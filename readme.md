# 📚 Book Recommender System

A hybrid **Book Recommender System** that combines **Popularity-Based Filtering** and **Collaborative Filtering** to provide accurate and personalized book recommendations.

---

## 🔍 What is a Recommender System?

A **Recommender System** is an information filtering system that predicts user preferences and suggests relevant items such as books, movies, or products.

### 🎯 Types of Recommender Systems

**1. Popularity-Based Recommendation**
- Recommends items based on overall popularity
- Uses metrics like average ratings and number of ratings
- Same recommendations for all users

**2. Collaborative Filtering**
- Recommends items based on user behavior and preferences
- Finds similarity between users or items
- Provides personalized recommendations

**3. Content-Based Filtering**
- Recommends items similar to what a user liked before
- Uses features like genre, author, etc.

**4. Hybrid Recommendation System (Used in this Project)**
- Combines multiple techniques
- Improves recommendation accuracy
- Overcomes limitations of individual methods

---

## 🚀 Project Overview

This project builds a **Hybrid Book Recommender System** using:

- 📈 **Popularity-Based Filtering** → Recommends top-rated and trending books  
- 🤝 **Collaborative Filtering** → Recommends books based on user similarity  

It uses real-world datasets of books, users, and ratings to generate meaningful recommendations.

---

## 🗂️ Project Structure

BOOK-RECOMMENDER-SYSTEM/
│
├── data/
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
│
├── models/
│   ├── books.pkl
│   ├── popular.pkl
│   ├── pt.pkl
│   └── similarity_scores.pkl
│
├── env/
│
├── app.py
├── book-recommender-system.ipynb
├── requirements.txt
├── readme.md
└── .gitignore

---

## ⚙️ How It Works

### 1. Data Preprocessing
- Merged Books, Users, and Ratings datasets
- Removed missing and invalid values
- Filtered active users and popular books

### 2. Popularity-Based Recommendation
- Based on:
  - Average rating
  - Number of ratings
- Outputs globally popular books

### 3. Collaborative Filtering
- Created a User-Item Matrix
- Applied Cosine Similarity
- Recommends books similar to user preferences

### 4. Model Saving
- Stored trained models using Pickle:
  - popular.pkl → Popular books
  - pt.pkl → Pivot table
  - similarity_scores.pkl → Similarity matrix
  - books.pkl → Processed books data

---

## 💡 Features

- 📊 Top popular book recommendations  
- 👤 Personalized book suggestions  
- ⚡ Fast predictions using precomputed models  
- 🧠 Hybrid recommendation system  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Pickle  
- Jupyter Notebook  
- Flask / Streamlit  

---

## ▶️ How to Run the Project (Step-by-Step)

### Step 1: Clone Repository
Open terminal and run:
git clone https://github.com/your-username/book-recommender-system.git

### Step 2: Go Inside Project Folder
cd book-recommender-system

### Step 3: Create Virtual Environment
python -m venv env

### Step 4: Activate Virtual Environment

For Windows:
env\Scripts\activate

For Mac/Linux:
source env/bin/activate

### Step 5: Install Required Libraries
pip install -r requirements.txt

### Step 6: Run the Application
python app.py

---

## 📊 Dataset

The system uses:
- Books dataset  
- Users dataset  
- Ratings dataset  

---

## 📌 Use Cases

- Online bookstores  
- Library systems  
- E-learning platforms  
- Personalized recommendation engines  

---

## 🔮 Future Improvements

- Add Content-Based Filtering  
- Improve UI/UX  
- Deploy on cloud platforms  
- Add real-time recommendations  
- Use Deep Learning  

---

## 🙌 Conclusion

This project demonstrates how combining **Popularity-Based** and **Collaborative Filtering** creates a powerful hybrid recommendation system that delivers both general and personalized recommendations.

---

## 📬 Contact

Kunal Kashyap