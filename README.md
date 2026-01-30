

# 📄 README.txt — GeoPitch AI (Localhost Hackathon Demo)

---

## PROJECT NAME

GeoPitch AI – AI + GPS Powered Real Estate Pitch Generator

---

## PROJECT DESCRIPTION

GeoPitch AI is a full-stack hackathon prototype that converts basic property information into professional real-estate pitches.

The system uses:

• Flask backend
• HTML + Bootstrap frontend
• Geopy for latitude/longitude
• Weather + AQI scraping (no API keys)
• Optional OpenAI AI selling points
• Image upload + preview
• Pitch preview page

This project runs locally on your computer using Python.

PDF generation is disabled. Preview only.

---

## FEATURES

✔ Login system (demo authentication)
✔ Property dashboard
✔ Latitude & longitude detection
✔ Weather + air quality index
✔ AI selling points (fallback supported)
✔ Image upload & preview
✔ Pitch preview screen

---

## SYSTEM REQUIREMENTS

You must have:

• Windows / Mac / Linux
• Python 3.10 or higher
• Internet connection

Check Python:

Open CMD:

python --version

or

py --version

---

## PROJECT STRUCTURE

GeoPitchAI

app.py
requirements.txt
README.txt

templates

* login.html
* index.html
* pitch.html

static

* uploads

---

# HOW TO RUN GEOPITCH AI LOCALLY (STEP BY STEP)

---

### STEP 1 — Download Project

Option A:

Download ZIP from GitHub → Extract folder

Option B:

Using Git:

git clone YOUR_REPOSITORY_URL
cd GeoPitchAI

---

### STEP 2 — Open Command Prompt

Go inside project folder.

Example:

cd Desktop\GeoPitchAI

---

### STEP 3 — Create Virtual Environment

python -m venv venv

Activate:

venv\Scripts\activate

You should see:

(venv)

---

### STEP 4 — Install Dependencies

pip install -r requirements.txt

Wait until finished.

---

### STEP 5 — Optional OpenAI Key

If you want real AI selling points:

set OPENAI_API_KEY=your_api_key

If skipped, fallback text is used automatically.

---

### STEP 6 — Run Application

python app.py

You will see:

Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### STEP 7 — Open Browser

Go to:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## LOGIN

This is demo authentication.

Enter ANY username and password.

Example:

Username: demo
Password: demo

---

## DASHBOARD USAGE

1. Enter location
2. Enter area
3. Select property type
4. Upload images
5. Click Generate Pitch

Preview page will open.

---

## WEATHER FEATURE

Weather and AQI are fetched automatically using public sources.

No API keys required.

---

## AI FEATURE

If OpenAI key exists → real AI

If no key → fallback selling points

System always works.

---

## IMAGE UPLOAD

Images appear immediately in preview.

Saved inside:

static/uploads

---

## IMPORTANT NOTES

• This is LOCALHOST only
• No cloud deployment
• No PDF export
• Preview demo
• Playwright removed
• Hackathon MVP

---

## COMMON ERRORS

---

Python not found:

Install from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Select:

✔ Add Python to PATH

---

Port already used:

Edit app.py:

app.run(port=5001)

---

Packages failing:

pip install --upgrade pip

Then retry.

---

## TECHNOLOGY STACK

Backend: Flask
Frontend: HTML + Bootstrap
Location: Geopy
Weather: wttr.in
AQI: aqicn.org
AI: OpenAI (optional)

---

## HACKATHON CHECKLIST

✔ Full stack
✔ Local deployment
✔ AI integration
✔ GPS location
✔ Weather intelligence
✔ Image handling
✔ Professional UI

---



Demonstrate how AI + location data can accelerate real estate sales presentations.

---


## CREATED FOR HACKATHON

GeoPitch AI
From Plot to Pitch

## Pictures

<img width="1913" height="941" alt="Screenshot 2026-01-31 050405" src="https://github.com/user-attachments/assets/fd0de472-2f54-457a-a1ca-c16ca4271bd1" />
<img width="1882" height="940" alt="Screenshot 2026-01-31 050428" src="https://github.com/user-attachments/assets/813b6e44-bf11-40ca-a8a4-358df6797215" />
<img width="1731" height="926" alt="Screenshot 2026-01-31 050455" src="https://github.com/user-attachments/assets/edf8913d-5de0-43fb-886d-b19afc67bfb8" />
<img width="580" height="821" alt="Screenshot 2026-01-31 050551" src="https://github.com/user-attachments/assets/8653692e-7eb2-4c2a-a54b-e859ddf806c0" />


VIDEO :
[vid.zip](https://github.com/user-attachments/files/24975684/vid.zip)

