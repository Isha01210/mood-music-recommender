# Mood-Based Music Recommender

A Flask web application that recommends songs based on the user's mood and preferred language.  
Currently, the project uses a predefined dataset of songs with direct links to YouTube Music and Spotify.  

Future plans include API integration, NLP-based mood detection, and AI/LLM personalization.

---

## Features
- Select a mood (Happy, Sad, Energetic, Calm).
- Filter recommendations by language/genre (English, Kannada, Telugu, Hindi,Phonk).
- Get 10 curated songs per mood per language.
- Songs link directly to YouTube Music or Spotify.
- Stylish UI with Bootstrap and custom CSS.

---

## Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS, Bootstrap
- Data: Predefined dataset (Python dictionary)

---

## Project Structure
mood-music-recommender/
│── app.py # Flask app
│── requirements.txt # Dependencies
│── README.md # Documentation
│
├── templates/
│ ├── index.html # Mood and language selection page
│ ├── results.html # Recommendations display page
│
└── static/
└── style.css # Custom styling

---

## Installation and Usage

1. Clone or download the project.
   ```bash
   git clone https://github.com/Isha01210/mood-music-recommender.git
   cd mood-music-recommender

2. Install dependencies.

pip install -r requirements.txt


3. Run the app.

python app.py


4. Open in browser:

http://127.0.0.1:5000/


How It Works

- User selects mood (Happy, Sad, Energetic, Calm).
- User selects preferred languages (checkbox filters).
- The app displays song recommendations with direct links.
- Future scope: Spotify API, NLP mood detection, AI-driven personalization.

Author

Kurapati Isha Sree – MCA Student @ RVCE

LinkedIn: [https://www.linkedin.com/in/isha-sree-kurapati-a009b026b/](https://www.linkedin.com/in/isha-sree-kurapati-a009b026b/)

GitHub: [https://github.com/Isha01210](https://github.com/Isha01210)