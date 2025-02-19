
### **Python Code Explainer**  
A simple web application that analyzes Python code and provides human-readable explanations.  

---

## 🚀 **Live Demo**  
**[Live Demo](https://python-code-explainer-for-beginners.onrender.com)**  

---

## 📌 **Features**  
✅ Paste and analyze Python code in real-time  
✅ Provides explanations for functions, loops, conditions, and assignments  
✅ Simple and clean UI with a dark theme  
✅ Fully responsive for mobile and desktop users  
✅ Flask-based backend with CORS support  

---

## 📂 **Project Structure**  

```
/Python-Code-Explainer
│── backend.py            
│── index.html           
│── requirements.txt     
│── README.md          
```

---

## 🛠 **Setup & Installation**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/AyushGorlawar/Python-Code-Explainer-for-Beginners/
cd Python-Code-Explainer
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Flask Server**  
```sh
python backend.py
```
Your API will be live at: `http://127.0.0.1:5000/explain`

### **4️⃣ Open the Frontend**  
- Open `index.html` in your browser.  
- Paste Python code and click **"Explain Code"** to get explanations.  

---

## 🚀 **Deploy on Render (Free Hosting)**  

### **1️⃣ Create a `requirements.txt` File**
Ensure you have the following dependencies:
```txt
flask
flask-cors
gunicorn
```

### **2️⃣ Push Code to GitHub**
```sh
git add .
git commit -m "Initial commit"
git push origin main
```

### **3️⃣ Deploy on Render**
1. Go to **[Render](https://render.com/)**
2. Click **New Web Service**
3. Connect your GitHub repo
4. Set **Start Command** as:  
   ```sh
   gunicorn backend:app
   ```
5. Click **Deploy**

---

## 🤖 **API Usage**  

**Endpoint:**  
```http
POST /explain
```
**Request Body:**  
```json
{
  "code": "def add(a, b): return a + b"
}
```
**Response:**  
```json
{
  "explanation": "Defines a function `add()` with parameters a, b.\nReturns a value from the function."
}
```

---

## 🤝 **Contributing**  
Want to improve this project? Feel free to **fork** and submit a PR!  

---

## 📜 **License**  
This project is licensed under the **MIT Licensed**.  

---

## ⭐ **Show Your Support**  
If you like this project, give it a ⭐ on GitHub!  

---

