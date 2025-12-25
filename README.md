# AI Engineer Internship Assignment

This repository contains my complete submission for the **AI Engineer Internship Assignment**.  
The assignment consists of **three independent tasks**, each focusing on a different real-world AI/computer vision problem.

All tasks are implemented in Python and follow a clean folder structure for easy evaluation.

---

## 🔹 Task 1: Thermal Image Overlay

**Objective:**  
Align and overlay thermal images onto corresponding RGB images.

**Key Highlights:**
- Image alignment using control points
- Perspective transformation
- Accurate thermal overlay generation

**Technologies Used:**
- Python
- OpenCV
- NumPy

**Folder:** `Task1/`

---

## 🔹 Task 2: Change Detection Algorithm

**Objective:**  
Detect and highlight missing objects between *before* and *after* images of the same scene.

**Key Highlights:**
- Pixel-level image comparison
- Bounding box generation around detected changes
- Fully automated batch processing

**Technologies Used:**
- Python
- OpenCV

**Folder:** `Task2/`

---

## 🔹 Task 3: Insurance GLR Automation (AI Powered)

**Objective:**  
Automate the process of filling insurance inspection templates using photo reports and AI.

**Key Highlights:**
- Streamlit-based interactive web application
- Upload insurance template (.docx) and inspection reports (.pdf)
- AI-assisted extraction and structured data filling
- Generates a completed insurance report automatically

**Technologies Used:**
- Python
- Streamlit
- PDF Processing
- Large Language Model (LLM via API)

**Folder:** `Task3/`

---

## ▶️ How to Run

Each task is independent and can be executed separately.

### Example: Running Task 3
```bash
python -m streamlit run task_3_code.py
