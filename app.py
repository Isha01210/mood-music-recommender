from flask import Flask, render_template, request

app = Flask(__name__)

# ================== PREDEFINED DATASET ==================
music_library = {
    "Happy": {
        "English": [
            ("Happy – Pharrell Williams", "https://music.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("Good Life – OneRepublic", "https://music.youtube.com/watch?v=jZhQOvvV45w"),
            ("On Top of the World – Imagine Dragons", "https://music.youtube.com/watch?v=w5tWYmIOWGk"),
            ("Best Day of My Life – American Authors", "https://music.youtube.com/watch?v=Y66j_BUCBMY"),
            ("Can't Stop the Feeling – Justin Timberlake", "https://music.youtube.com/watch?v=ru0K8uYEZWw"),
            ("Shake It Off – Taylor Swift", "https://music.youtube.com/watch?v=nfWlot6h_JM"),
            ("Good Vibes – Chris Janson", "https://music.youtube.com/watch?v=ls1S5oK4c90"),
            ("Walking on Sunshine – Katrina & The Waves", "https://music.youtube.com/watch?v=iPUmE-tne5U"),
            ("Uptown Funk – Mark Ronson ft. Bruno Mars", "https://music.youtube.com/watch?v=OPf0YbXqDm0"),
            ("Best Song Ever – One Direction", "https://music.youtube.com/watch?v=o_v9MY_FMcw"),
        ],
        "Kannada": [
            ("Belageddu – Kirik Party", "https://music.youtube.com/watch?v=w8g5xADZt50"),
            ("Marali Manasaagide – Gentleman", "https://music.youtube.com/watch?v=3cyz6Vw6Gso"),
            ("Love You Chinna – Love Mocktail 2", "https://music.youtube.com/watch?v=ucO7gyTCCtw"),
            ("Ondu Malebillu – Chakravarthy", "https://music.youtube.com/watch?v=oaB8rGIqS2A"),
            ("Kannu Hodiyaka – Roberrt", "https://music.youtube.com/watch?v=Dyj1T-JUsnY"),
            ("Yenammi Yenammi – Ayogya", "https://music.youtube.com/watch?v=ha_gW1ZBTSw"),
            ("Dostha Kano – Chowka", "https://music.youtube.com/watch?v=3Wn3FhE4Umo"),
            ("Open Hairu – Murali Meets Meera", "https://music.youtube.com/watch?v=KNgh0Qm8cVo"),
            ("Sanjana – Hudugata", "https://music.youtube.com/watch?v=ZkJH6cKKnB0"),
            ("Neene Modalu Neene Kone – Operation Alamelamma", "https://music.youtube.com/watch?v=YVbfi9WWc0g"),
        ],
        "Telugu": [
            ("Butta Bomma – Ala Vaikunthapurramuloo", "https://music.youtube.com/watch?v=0KSOMA3QBU0"),
            ("Samajavaragamana – Ala Vaikunthapurramuloo", "https://music.youtube.com/watch?v=7J_xkWk9te0"),
            ("Seeti Maar – DJ", "https://music.youtube.com/watch?v=kSNtnC3qfV4"),
            ("Nee Kallu Neeli Samudram – Uppena", "https://music.youtube.com/watch?v=Zn06HXh5aYg"),
            ("Darshana – Karthikeya 2", "https://music.youtube.com/watch?v=4yQET2tziiw"),
            ("Oo Antava – Pushpa", "https://music.youtube.com/watch?v=xB7Mtz3hqdw"),
            ("Srivalli – Pushpa", "https://music.youtube.com/watch?v=tYvYaTGQbc4"),
            ("Mind Block – Sarileru Neekevvaru", "https://music.youtube.com/watch?v=YoHD9XEInc0"),
            ("Rowdy Baby – Maari 2", "https://music.youtube.com/watch?v=x6Q7c9RyMzk"),
            ("Ramulo Ramula – Ala Vaikunthapurramuloo", "https://music.youtube.com/watch?v=6Wg8yUQSmZg"),
        ],
        "Hindi": [
            ("Gallan Goodiyaan – Dil Dhadakne Do", "https://music.youtube.com/watch?v=qgULZPgkSBQ"),
            ("Nashe Si Chadh Gayi – Befikre", "https://music.youtube.com/watch?v=WFcsm3j3JHc"),
            ("Kar Gayi Chull – Kapoor & Sons", "https://music.youtube.com/watch?v=QeXhz5f2Eck"),
            ("Badtameez Dil – Yeh Jawaani Hai Deewani", "https://music.youtube.com/watch?v=II2EO3Nw4m0"),
            ("Kala Chashma – Baar Baar Dekho", "https://music.youtube.com/watch?v=k4yXQkG2s1E"),
            ("London Thumakda – Queen", "https://music.youtube.com/watch?v=I0JX7Ebf08c"),
            ("Senorita – Zindagi Na Milegi Dobara", "https://music.youtube.com/watch?v=KRaWnd3LJfs"),
            ("Ude Dil Befikre – Befikre", "https://music.youtube.com/watch?v=6FURuLYrR_Q"),
            ("Cutiepie – Ae Dil Hai Mushkil", "https://music.youtube.com/watch?v=k4xZpBY3ELs"),
            ("Dil Dhadakne Do – Title Track", "https://music.youtube.com/watch?v=5TLHNp9z4Qw"),
        ],
        "Phonk": [
            ("Drift Phonk – DVRST", "https://music.youtube.com/watch?v=FjHGZj2IjBk"),
            ("Phonky Town", "https://music.youtube.com/watch?v=z0Tt9aSMjOg"),
            ("Phonk House – Kordhell", "https://music.youtube.com/watch?v=6M7KgK1e9sQ"),
            ("METAMORPHOSIS – INTERWORLD", "https://music.youtube.com/watch?v=ETrzE6lT1js"),
            ("IN THE CLUB – Phonk Remix", "https://music.youtube.com/watch?v=DpYKn-7n0RI"),
            ("GigaChad Theme – Phonk", "https://music.youtube.com/watch?v=2OKW2v31BLg"),
            ("Tokyo Drift Phonk", "https://music.youtube.com/watch?v=3QvEJpQ7Fbk"),
            ("Slowed + Reverb Phonk", "https://music.youtube.com/watch?v=nVSW2N1Db1M"),
            ("HARD PHONK MIX", "https://music.youtube.com/watch?v=0lq2ZlE6mXU"),
            ("PHONK 2024 Mix", "https://music.youtube.com/watch?v=7F9DbR5JXkg"),
        ],
    },

    "Sad": {
        "English": [
            ("Someone Like You – Adele", "https://music.youtube.com/watch?v=hLQl3WQQoQ0"),
            ("Fix You – Coldplay", "https://music.youtube.com/watch?v=k4V3Mo61fJM"),
            ("Let Her Go – Passenger", "https://music.youtube.com/watch?v=RBumgq5yVrA"),
            ("Stay – Rihanna ft. Mikky Ekko", "https://music.youtube.com/watch?v=JF8BRvqGCNs"),
            ("When I Was Your Man – Bruno Mars", "https://music.youtube.com/watch?v=ekzHIouo8Q4"),
            ("All I Want – Kodaline", "https://music.youtube.com/watch?v=mtf7hC17IBM"),
            ("Someone You Loved – Lewis Capaldi", "https://music.youtube.com/watch?v=zABLecsR5UE"),
            ("Un-break My Heart – Toni Braxton", "https://music.youtube.com/watch?v=p2Rch6WvPJE"),
            ("The Night We Met – Lord Huron", "https://music.youtube.com/watch?v=KtlgYxa6BMU"),
            ("Say Something – A Great Big World", "https://music.youtube.com/watch?v=-2U0Ivkn2Ds"),
        ],
        "Kannada": [
            ("Ondu Male Billu – Chakravarthy", "https://music.youtube.com/watch?v=oaB8rGIqS2A"),
            ("Ninna Snehake – Amma I Love You", "https://music.youtube.com/watch?v=f2PsoMZFo8Y"),
            ("Naguva Nayana – Pallavi Anupallavi", "https://music.youtube.com/watch?v=1D5fZm86qfY"),
            ("Nee Amrutheya – Simple Agi Ondh Love Story", "https://music.youtube.com/watch?v=6-9f9JwH2tk"),
            ("Bombe Helutaithe – Rajkumara", "https://music.youtube.com/watch?v=J8FjG2gsJTA"),
            ("Usire Usire – Hebbuli", "https://music.youtube.com/watch?v=hI02mFgoGmM"),
            ("Naguva Nayana – Pallavi Anupallavi", "https://music.youtube.com/watch?v=QLbqHnKQ9-4"),
            ("Neene Modalu Neene Kone – Operation Alamelamma", "https://music.youtube.com/watch?v=YVbfi9WWc0g"),
            ("Madhura Pisumaatige – Love Mocktail", "https://music.youtube.com/watch?v=0W6QzBl1E0U"),
            ("Kanaso Idu – Kirik Party", "https://music.youtube.com/watch?v=7sH4uEwLDoI"),
        ],
        "Telugu": [
            ("Priyathama Priyathama – Majili", "https://music.youtube.com/watch?v=9FVGyOJwyH8"),
            ("Ye Mantramo – Love Story", "https://music.youtube.com/watch?v=gyxPfm0ayAE"),
            ("Kopamga Kopamga – Darling", "https://music.youtube.com/watch?v=sbyZMHhrpwQ"),
            ("Inkem Inkem Inkem Kaavaale – Geetha Govindam", "https://music.youtube.com/watch?v=NFjE5A4UAJI"),
            ("Em Sandeham Ledu – Oohalu Gusagusalade", "https://music.youtube.com/watch?v=2cpnR8A8DWg"),
            ("Ninnu Kori Varnam – Ninnu Kori", "https://music.youtube.com/watch?v=cJvpoDdLwHQ"),
            ("Samajavaragamana (sad cover)", "https://music.youtube.com/watch?v=H3oMH6aFqgU"),
            ("Tholi Prema Title Song", "https://music.youtube.com/watch?v=5fYh6qdpG9U"),
            ("Pilla Ra – RX 100", "https://music.youtube.com/watch?v=HDtqss0np30"),
            ("Vintunnava – Ye Maya Chesave", "https://music.youtube.com/watch?v=0RkOaFjGmbE"),
        ],
        "Hindi": [
            ("Channa Mereya – Ae Dil Hai Mushkil", "https://music.youtube.com/watch?v=284Ov7ysmfA"),
            ("Tera Ban Jaunga – Kabir Singh", "https://music.youtube.com/watch?v=pq4mjZfzjxE"),
            ("Tum Hi Ho – Aashiqui 2", "https://music.youtube.com/watch?v=Umqb9KENgmk"),
            ("Agar Tum Saath Ho – Tamasha", "https://music.youtube.com/watch?v=sK7riqg2mr4"),
            ("Jeene Bhi De Duniya Humein – Dil Sambhal Jaa Zara", "https://music.youtube.com/watch?v=k2Wb_VB11tM"),
            ("Khairiyat – Chhichhore", "https://music.youtube.com/watch?v=hoNb6HuNmU0"),
            ("Hawayein – Jab Harry Met Sejal", "https://music.youtube.com/watch?v=CcNo07Xp8aQ"),
            ("Raabta – Agent Vinod", "https://music.youtube.com/watch?v=VRlcJtZAk6c"),
            ("Kal Ho Na Ho Title Song", "https://music.youtube.com/watch?v=J1wcbOyQqzs"),
            ("Tujhe Kitna Chahne Lage – Kabir Singh", "https://music.youtube.com/watch?v=AtKZKl7Bgu0"),
        ],
        "Phonk": [
            ("Phonk Sad Mix", "https://music.youtube.com/watch?v=ZyNQwWlQYdY"),
            ("Phonk Rain Mix", "https://music.youtube.com/watch?v=EkOkH37U0xA"),
            ("Emotional Phonk", "https://music.youtube.com/watch?v=tsXnb1WgZ1M"),
            ("Sad Drift Phonk", "https://music.youtube.com/watch?v=hFkfsf19rtw"),
            ("Deep Sad Phonk", "https://music.youtube.com/watch?v=aIN2xT8zBkg"),
            ("Cry Phonk", "https://music.youtube.com/watch?v=1knhEnNh4tU"),
            ("Lost in Memories – Phonk", "https://music.youtube.com/watch?v=y9Z2bl0w2XU"),
            ("Dreamy Phonk", "https://music.youtube.com/watch?v=El5t7Kc5Uw4"),
            ("Pain Phonk", "https://music.youtube.com/watch?v=0L6YUgP5nYA"),
            ("Broken Phonk", "https://music.youtube.com/watch?v=sn1MKeI3DgA"),
        ],
    },

        "Energetic": {
        "English": [
            ("Believer – Imagine Dragons", "https://music.youtube.com/watch?v=7wtfhZwyrcc"),
            ("Stronger – Kelly Clarkson", "https://music.youtube.com/watch?v=Xn676-fLq7I"),
            ("Hall of Fame – The Script ft. will.i.am", "https://music.youtube.com/watch?v=mk48xRzuNvA"),
            ("Don't Stop Me Now – Queen", "https://music.youtube.com/watch?v=HgzGwKwLmgM"),
            ("Thunder – Imagine Dragons", "https://music.youtube.com/watch?v=fKopy74weus"),
            ("Shake It Off – Taylor Swift", "https://music.youtube.com/watch?v=nfWlot6h_JM"),
            ("Stronger – Kanye West", "https://music.youtube.com/watch?v=PsO6ZnUZI0g"),
            ("Can't Stop – Red Hot Chili Peppers", "https://music.youtube.com/watch?v=BfOdWSiyWoc"),
            ("Pump It – Black Eyed Peas", "https://music.youtube.com/watch?v=ZaI2IlHwmgQ"),
            ("Firework – Katy Perry", "https://music.youtube.com/watch?v=QGJuMBdaqIw"),
        ],
        "Kannada": [
            ("Open Hairu – Murali Meets Meera", "https://music.youtube.com/watch?v=KNgh0Qm8cVo"),
            ("Karabuu – Pogaru", "https://music.youtube.com/watch?v=hyLhjOL0ed0"),
            ("Dostha Kano – Chowka", "https://music.youtube.com/watch?v=3Wn3FhE4Umo"),
            ("Hudugaru Title Song – Hudugaru", "https://music.youtube.com/watch?v=3XPSjRLvH7w"),
            ("Selfie Maadkole – Mungaru Male 2", "https://music.youtube.com/watch?v=FuNj7O_UfwA"),
            ("Sandalwood Sa Re Ga Ma – Victory", "https://music.youtube.com/watch?v=ENbMLkHZ8Yc"),
            ("Thamnam Thamnam – Seizer", "https://music.youtube.com/watch?v=FZ1PqBdXUvQ"),
            ("Jokae – Raambo 2", "https://music.youtube.com/watch?v=5MfT0kS8FZg"),
            ("Chuttu Chuttu – Vajrakaya", "https://music.youtube.com/watch?v=FZw4stbUr4s"),
            ("Pakka Local – Jaguar", "https://music.youtube.com/watch?v=n3X9FGCYU0o"),
        ],
        "Telugu": [
            ("Top Lesi Poddi – Iddarammayilatho", "https://music.youtube.com/watch?v=7NQ0kZc6iS4"),
            ("Blockbuster – Sarrainodu", "https://music.youtube.com/watch?v=K7syQ1OrYcA"),
            ("Dhinka Chika – Ready", "https://music.youtube.com/watch?v=8J2uAHgxVAY"),
            ("Ringa Ringa – Arya 2", "https://music.youtube.com/watch?v=l2tQkzYYdQo"),
            ("You Are My MLA – MLA", "https://music.youtube.com/watch?v=r-fIXgpxy_Q"),
            ("Bommali – Billa", "https://music.youtube.com/watch?v=pxb9t2y1sfs"),
            ("Swing Zara – Jai Lava Kusa", "https://music.youtube.com/watch?v=8MZGuP9WxWc"),
            ("Bad Boy – Saaho", "https://music.youtube.com/watch?v=F6a0JZnQ6x8"),
            ("Dhruva Dhruva – Dhruva", "https://music.youtube.com/watch?v=YV1gZXe-B-w"),
            ("Hey Idi Nenena – Rakshasudu", "https://music.youtube.com/watch?v=lWdYJcHgJzI"),
        ],
        "Hindi": [
            ("Malhari – Bajirao Mastani", "https://music.youtube.com/watch?v=h6nE7W9_VT8"),
            ("Zinda – Bhaag Milkha Bhaag", "https://music.youtube.com/watch?v=t1WYXzFZ5PY"),
            ("Apna Time Aayega – Gully Boy", "https://music.youtube.com/watch?v=JfbxcD6biOk"),
            ("Sher Aaya Sher – Gully Boy", "https://music.youtube.com/watch?v=lE-hPHDcgR4"),
            ("Bhaag DK Bose – Delhi Belly", "https://music.youtube.com/watch?v=NHf0hX3c9sU"),
            ("Sadda Haq – Rockstar", "https://music.youtube.com/watch?v=8kQZHYbZkLs"),
            ("Rock On!! Title Track", "https://music.youtube.com/watch?v=t5YskL3_9P4"),
            ("Badri Ki Dulhania – Badrinath Ki Dulhania", "https://music.youtube.com/watch?v=DJ9Z6M9dJUk"),
            ("Main Tera Boyfriend – Raabta", "https://music.youtube.com/watch?v=LCyo565N_6Y"),
            ("Saturday Saturday – Humpty Sharma Ki Dulhania", "https://music.youtube.com/watch?v=f3qv2dSXQXo"),
        ],
        "Phonk": [
            ("Rave Phonk", "https://music.youtube.com/watch?v=EtZ2m2Zm3Y0"),
            ("Extreme Gym Phonk", "https://music.youtube.com/watch?v=U2e3d2_rDNQ"),
            ("Hard Drift Phonk", "https://music.youtube.com/watch?v=3QvEJpQ7Fbk"),
            ("Boss Mode Phonk", "https://music.youtube.com/watch?v=8C6cKQrd0Rw"),
            ("Fast Lane Drift Phonk", "https://music.youtube.com/watch?v=4tBlH1TRoGY"),
            ("Speed Demon Phonk", "https://music.youtube.com/watch?v=3bckM6J6MR8"),
            ("Aggressive Phonk Mix", "https://music.youtube.com/watch?v=7jswAnH4w8Y"),
            ("Destroyer Phonk", "https://music.youtube.com/watch?v=YfO6j2k2N34"),
            ("High BPM Phonk", "https://music.youtube.com/watch?v=sz6M6c1rQ9w"),
            ("Racing Phonk Mix", "https://music.youtube.com/watch?v=wAexVltpP_M"),
        ],
    },

    "Calm": {
        "English": [
            ("Weightless – Marconi Union", "https://music.youtube.com/watch?v=UfcAVejslrU"),
            ("River Flows in You – Yiruma", "https://music.youtube.com/watch?v=7maJOI3QMu0"),
            ("A Thousand Years – Christina Perri", "https://music.youtube.com/watch?v=rtOvBOTyX00"),
            ("Let It Be – The Beatles", "https://music.youtube.com/watch?v=QDYfEBY9NM4"),
            ("All of Me – John Legend", "https://music.youtube.com/watch?v=450p7goxZqg"),
            ("Somewhere Over the Rainbow – Israel Kamakawiwo'ole", "https://music.youtube.com/watch?v=V1bFr2SWP1I"),
            ("Yellow – Coldplay", "https://music.youtube.com/watch?v=yKNxeF4KMsY"),
            ("Say You Won’t Let Go – James Arthur", "https://music.youtube.com/watch?v=0yW7w8F2TVA"),
            ("Photograph – Ed Sheeran", "https://music.youtube.com/watch?v=nSDgHBxUbVQ"),
            ("Fix You – Coldplay", "https://music.youtube.com/watch?v=k4V3Mo61fJM"),
        ],
        "Kannada": [
            ("Ee Sanje Yakagide – Geetha", "https://music.youtube.com/watch?v=wJtLbd0p2eM"),
            ("Mouna Sanjege – Gaalipata", "https://music.youtube.com/watch?v=rO3OEpRyG0c"),
            ("Hrudaya Haadithu – Hrudaya Haadithu", "https://music.youtube.com/watch?v=E6r2TK59SxI"),
            ("Neene Modalu Neene Kone – Operation Alamelamma", "https://music.youtube.com/watch?v=YVbfi9WWc0g"),
            ("Madhura Pisumaatige – Love Mocktail", "https://music.youtube.com/watch?v=0W6QzBl1E0U"),
            ("Usire Usire – Hebbuli", "https://music.youtube.com/watch?v=hI02mFgoGmM"),
            ("Ello Maleyaagide – Amrithadhare", "https://music.youtube.com/watch?v=4L5STiK7hA8"),
            ("Naguva Nayana – Pallavi Anupallavi", "https://music.youtube.com/watch?v=QLbqHnKQ9-4"),
            ("Ondu Malebillu – Chakravarthy", "https://music.youtube.com/watch?v=oaB8rGIqS2A"),
            ("Kannalle Kannitu – Gaalipata 2", "https://music.youtube.com/watch?v=dHzQ4h3iUbM"),
        ],
        "Telugu": [
            ("Priyathama Priyathama – Majili", "https://music.youtube.com/watch?v=9FVGyOJwyH8"),
            ("Inkem Inkem Inkem Kaavaale – Geetha Govindam", "https://music.youtube.com/watch?v=NFjE5A4UAJI"),
            ("Vintunnava – Ye Maya Chesave", "https://music.youtube.com/watch?v=0RkOaFjGmbE"),
            ("Kanulanu Thaake – Manam", "https://music.youtube.com/watch?v=9rYchM90oY8"),
            ("Oohale – Jaanu", "https://music.youtube.com/watch?v=Z8OtbjNP5hA"),
            ("Neeli Neeli Aakasam – 30 Rojullo Preminchadam Ela", "https://music.youtube.com/watch?v=g5bN5T4cz0Y"),
            ("Yemito – A Aa", "https://music.youtube.com/watch?v=DNguWhcXzSY"),
            ("Nuvvostanante Nenoddantana – Title", "https://music.youtube.com/watch?v=wS3a2QWrZjw"),
            ("Tholi Prema Title Song", "https://music.youtube.com/watch?v=5fYh6qdpG9U"),
            ("Manohara – Oohalu Gusagusalade", "https://music.youtube.com/watch?v=2cpnR8A8DWg"),
        ],
        "Hindi": [
            ("Tum Hi Ho – Aashiqui 2", "https://music.youtube.com/watch?v=Umqb9KENgmk"),
            ("Kabira – Yeh Jawaani Hai Deewani", "https://music.youtube.com/watch?v=jHNNMj5bNQw"),
            ("Muskurane – Citylights", "https://music.youtube.com/watch?v=fsL0Rj6kn-w"),
            ("Jeene Laga Hoon – Ramaiya Vastavaiya", "https://music.youtube.com/watch?v=wrPo2VVL8Zo"),
            ("Sun Saathiya – ABCD 2", "https://music.youtube.com/watch?v=SaUvN8UUPpo"),
            ("Raabta – Agent Vinod", "https://music.youtube.com/watch?v=VRlcJtZAk6c"),
            ("Khairiyat – Chhichhore", "https://music.youtube.com/watch?v=hoNb6HuNmU0"),
            ("Samjhawan – Humpty Sharma Ki Dulhania", "https://music.youtube.com/watch?v=t7CHfqg0wd8"),
            ("Shayad – Love Aaj Kal", "https://music.youtube.com/watch?v=8nZ4dco4P9k"),
            ("Hasi – Hamari Adhuri Kahani", "https://music.youtube.com/watch?v=J8P5Xwp9mbU"),
        ],
        "Phonk": [
            ("Lo-Fi Phonk Chill", "https://music.youtube.com/watch?v=wxXbDbOYO3I"),
            ("Relax Phonk", "https://music.youtube.com/watch?v=0e4JUcEl53Y"),
            ("Night Chill Phonk", "https://music.youtube.com/watch?v=I4qBrDQ7fJs"),
            ("Dreamy Phonk", "https://music.youtube.com/watch?v=El5t7Kc5Uw4"),
            ("Soft Drift Phonk", "https://music.youtube.com/watch?v=GJ8X0SxNlzU"),
            ("Peaceful Phonk", "https://music.youtube.com/watch?v=iqA3ax8J4lM"),
            ("Ocean Vibes Phonk", "https://music.youtube.com/watch?v=Th3k0Tq2m0E"),
            ("Deep Relax Phonk", "https://music.youtube.com/watch?v=aA8wjBbdDjk"),
            ("Calm Breeze Phonk", "https://music.youtube.com/watch?v=dCGwYOA4oIU"),
            ("Meditation Phonk", "https://music.youtube.com/watch?v=5K06i40jFlE"),
        ],
    },

}

# ================== ROUTES ==================
@app.route('/')
def index():
    moods = list(music_library.keys())
    languages = ["English", "Kannada", "Telugu", "Hindi", "Phonk"]
    return render_template("index.html", moods=moods, languages=languages)

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form['mood']
    selected_languages = request.form.getlist('languages')

    results = {}
    for lang in selected_languages:
        results[lang] = music_library[mood].get(lang, [])

    return render_template("results.html", mood=mood, results=results)

if __name__ == "__main__":
    app.run(debug=True)
