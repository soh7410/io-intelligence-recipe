# IO Intelligence Recipe Generator - Tutorial

This tutorial will guide you through setting up a simple **Recipe Generator** using **Vue.js (frontend)** and **FastAPI (backend)**, powered by **IO Intelligence API**.

## 📌 Project Overview
This project allows users to input ingredients, and it generates a **complete recipe** including a title, additional ingredients, cooking steps, and tips using **IO Intelligence API**.

## 🛠 Tech Stack
- **Frontend:** Vue.js (Vite)
- **Backend:** FastAPI
- **API:** IO Intelligence API (DeepSeek-R1 Model)
- **Hosting:** Can be deployed to Vercel (frontend) and Render/Heroku (backend)

---

## 📂 Project Structure
```sh
io-intelligence-recipe/
│── backend/  # FastAPI backend
│   │── main.py  # FastAPI entry point
│   │── .env  # API keys (not committed to Git)
│   │── requirements.txt  # Python dependencies
│
│── frontend/  # Vue.js frontend
│   │── src/
│   │   │── components/
│   │   │── App.vue  # Main Vue file
│   │   │── main.js  # Vue entry point
│   │── package.json  # npm dependencies
│   │── vite.config.js  # Vite settings
│
│── README.md  # This tutorial
```

---

## 🚀 Backend Setup
### 1️⃣ Install Dependencies
```sh
cd backend
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

### 2️⃣ Set Up Environment Variables
Create a `.env` file inside `backend/` with the following content:
```sh
IO_INTEL_API_KEY=your_io_intelligence_api_key_here
```
Refer to the official IO Intelligence API documentation for key setup and authentication: [IO Intelligence Docs](https://docs.io.net/docs/io-intelligence)

### 3️⃣ Run the FastAPI Server
```sh
uvicorn main:app --reload
```
Your backend should now be running at **`http://127.0.0.1:8000`**

---

## 🎨 Frontend Setup
### 1️⃣ Install Vue & Dependencies
```sh
cd frontend
npm install
```

### 2️⃣ Run the Vue App
```sh
npm run dev
```
Access the frontend at **`http://localhost:5173`**

---

## 🔄 Connecting Frontend & Backend
Update `frontend/src/App.vue` to send requests to `http://127.0.0.1:8000/generate-recipe/` when clicking the "Generate" button.

```javascript
const API_ENDPOINT = "http://127.0.0.1:8000/generate-recipe/";
const response = await axios.post(API_ENDPOINT, { ingredients: this.ingredients });
```

---

## 🛠 Deployment (Optional)
### Backend (FastAPI) Deployment
- Use **Render/Heroku** to deploy FastAPI

### Frontend (Vue.js) Deployment
- Use **Vercel/Netlify** for frontend hosting

---

## 🎯 Summary
✅ **Vue.js UI** for entering ingredients
✅ **FastAPI backend** to process requests
✅ **IO Intelligence API** to generate structured recipes
✅ **Deployed using modern cloud platforms**

This completes your **Recipe Generator** setup! 🎉 Feel free to modify and expand this project!

