# 🔍 Semantic Search Engine using Pinecone & Sentence Transformers

## 📌 Overview

This project implements a **Semantic Search Engine** that retrieves relevant information based on meaning rather than exact keyword matching. It uses **Sentence Transformers** to generate embeddings and **Pinecone** as a vector database for fast similarity search.

The system allows users to upload text documents (Q&A format) and perform intelligent queries through a **Streamlit web interface**.

---

## 🚀 Features

* 🔎 Semantic search (context-based retrieval)
* 🤖 Sentence embeddings using transformer models
* ☁️ Vector database powered by Pinecone
* 🌐 Interactive UI using Streamlit
* 📂 Upload custom `.txt` datasets
* ⚡ Fast and scalable retrieval

---

## 🧠 How It Works

1. 📄 Upload a `.txt` file (Q&A format)
2. 🧹 Preprocess and combine text
3. 🤖 Convert text into embeddings using Sentence Transformers
4. ☁️ Store embeddings in Pinecone vector database
5. 🔍 Query → embedding → similarity search
6. 📊 Return most relevant results

---

## 🗂️ Project Structure

```id="2xq1mt"
Rag-Project/
│
├── app.py              # Main Streamlit app
├── .env                # API keys (not uploaded to GitHub)
├── requirements.txt    # Dependencies
├── .gitignore          # Ignore sensitive files
```

---

## ⚙️ Installation & Setup

### 🔹 Step 1: Clone Repository

```id="nklf08"
git clone https://github.com/your-username/semantic-search-engine.git
cd semantic-search-engine
```

---

### 🔹 Step 2: Install Dependencies

```id="y1e3kx"
pip install -r requirements.txt
```

---

### 🔹 Step 3: Add Pinecone API Key

Create a `.env` file:

```id="3l2t8y"
PINECONE_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

### 🔹 Run the Streamlit App

```id="g0bnhl"
streamlit run app.py
```

---

### 🔹 Open in Browser

```id="pg6r8f"
http://localhost:8501
```

---

## 📂 Input Format (Important)

Your `.txt` file must follow:

```id="8d0t0t"
Question 1
Answer 1
Question 2
Answer 2
```

---

## 🎯 Example Output

* Enter a query like:
  👉 *"What is leave policy?"*

* System returns:

  * Most relevant Q&A pairs
  * Similarity score

---

## 🖥️ Technologies Used

* Python
* Streamlit
* Sentence Transformers
* Pinecone (Vector Database)
* NumPy

---

## 🔥 Future Improvements

* 📄 PDF document support
* 💬 ChatGPT-style chatbot (RAG)
* 🌐 Deploy online (Render / Hugging Face)
* 📊 Better UI & ranking improvements

---

## 🧠 Key Concepts

* Semantic Search
* Embeddings
* Vector Databases
* Retrieval-Augmented Generation (RAG)

---

## 👨‍💻 Author

**Tarun SR**

---

## ⭐ Conclusion

This project demonstrates how modern AI techniques like embeddings and vector databases can be used to build intelligent and scalable search systems beyond traditional keyword-based methods.

---

⭐ *If you like this project, consider giving it a star!*
