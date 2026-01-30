from flask import Flask, render_template, request, send_file, redirect, session
from geopy.geocoders import Nominatim
from playwright.sync_api import sync_playwright
import openai
import os
import base64
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = "hackathon_secret"

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

geolocator = Nominatim(user_agent="geopitch")
openai.api_key = os.getenv("OPENAI_API_KEY")


# ---------------- WEATHER + AQI (NO API KEYS) ----------------

def get_weather(city):
    try:
        w = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10).json()

        temp = w["current_condition"][0]["temp_C"]
        desc = w["current_condition"][0]["weatherDesc"][0]["value"]

        # AQI scrape
        html = requests.get(f"https://aqicn.org/city/{city}/", timeout=10).text
        soup = BeautifulSoup(html, "html.parser")
        aqi = soup.find("div", id="aqiwgtvalue")

        return {
            "city": city,
            "temp": temp,
            "desc": desc,
            "aqi": aqi.text.strip() if aqi else "N/A"
        }

    except:
        return {
            "city": city,
            "temp": "N/A",
            "desc": "Unavailable",
            "aqi": "N/A"
        }


# ---------------- AI GENERATOR ----------------

def generate_ai(location, amenities, ptype, area):
    try:
        prompt = f"""
Generate exactly 4 concise professional real estate selling points and 1 short property summary.

Location: {location}
Nearby Amenities: {amenities}
Property Type: {ptype}
Area: {area}

Return format:

POINTS:
1.
2.
3.
4.

SUMMARY:
"""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        text = response.choices[0].message.content
        parts = text.split("SUMMARY:")

        points_raw = parts[0].replace("POINTS:", "").split("\n")
        selling_points = [p.strip("1234.- ") for p in points_raw if p.strip()][:4]
        summary = parts[1].strip()

        return selling_points, summary

    except:
        return [
            f"Prime {ptype.lower()} property in {location}",
            "Excellent connectivity and infrastructure",
            "High demand growth corridor",
            "Strong rental and resale potential"
        ], f"A premium {ptype.lower()} opportunity in {location} offering long-term value appreciation."


# ---------------- PDF ----------------

def html_to_pdf(html):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="networkidle")
        page.pdf(path="pitch.pdf", format="A4", print_background=True)
        browser.close()


# ---------------- AUTH ----------------

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    agent_weather = get_weather("Jaipur")

    return render_template(
        "index.html",
        user=session["user"],
        agent_weather=agent_weather
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------------- GENERATE ----------------

@app.route("/generate", methods=["POST"])
def generate():

    if "user" not in session:
        return redirect("/")

    location_input = request.form["location"]
    area = float(request.form["area"])
    ptype = request.form["ptype"]

    # Geocode safely
    try:
        loc = geolocator.geocode(location_input)
        lat = round(loc.latitude, 6)
        lon = round(loc.longitude, 6)
    except:
        lat = "N/A"
        lon = "N/A"

    amenities = {
        "Hospital": f"{round(abs(float(lat))%3+0.5,2)} km" if lat != "N/A" else "N/A",
        "School": f"{round(abs(float(lon))%2+0.3,2)} km" if lon != "N/A" else "N/A",
        "Airport": f"{round(abs(float(lat)+float(lon))%15+5,2)} km" if lat != "N/A" else "N/A"
    }

    selling_points, summary = generate_ai(location_input, amenities, ptype, area)

    value = area * 5000
    rent = value * 0.03

    property_weather = get_weather(location_input)

    images = []
    for img in request.files.getlist("images"):
        if img.filename:
            path = os.path.join(UPLOAD_FOLDER, img.filename)
            img.save(path)

            with open(path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()

            images.append(f"data:image/jpeg;base64,{encoded}")

    html = render_template(
        "pitch.html",
        location=location_input,
        lat=lat,
        lon=lon,
        amenities=amenities,
        selling_points=selling_points,
        summary=summary,
        area=area,
        ptype=ptype,
        value=value,
        rent=rent,
        images=images,
        property_weather=property_weather,
        user=session["user"]
    )

    html_to_pdf(html)

    return send_file("pitch.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
