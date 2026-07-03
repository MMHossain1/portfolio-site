"""
Single source of truth for all portfolio content. 

"""

# --- Basic identity ---
PROFILE = {
    "name": "Mohammed Hossain",
    "tagline": "Shipping production AI and full-stack systems",
    "location": "Dublin, Ireland",
    "blurb": (
        "Computer Scientist by training and Software Engineer by practice. "
        "I build production applications across the stack from systems programming "
        "and cloud infrastructure to modern web applications. I'm particularly " 
        "interested in fintech and enjoy building reliable, scalable software that "
        "solves complex technical challenges."
    ),
    "photo": "img/mh/profile.png",
    "github": "https://github.com/MMHossain1",
    "linkedin": "https://www.linkedin.com/in/mohammed-hossain-379584337"
}

# --- About section: ---
ABOUT = [
    (
        "I'm a full-stack software engineer building production systems across "
        "cloud infrastructure, backend services and frontend applications. "
        "Recently, I've been working on production engineering challenges at Meta, "
        "AI-assisted security platforms at Workday"
    ),
    (
        "I'm in my third year studying Computer Science at Trinity College Dublin, "
        "on track for a strong First Class Honours. My technical foundation spans systems "
        "programming, concurrent systems and software engineering. I'm most "
        "motivated by shipping systems that work reliably at scale."
    ),
    (
        "When I'm not coding, I'm out exploring the world, capturing landscapes through photography :)" 
        ""
    ),
]

# --- Work experiences (most recent first) ---
WORK = [
    {
        "role": "Software Development Engineering Intern",
        "org": "Amazon",
        "logo": "img/mh/amazon_logo.jpg",
        "dates": "Mar 2027 – Jun 2027",
        "location": "On-Site",
        "bullets": [
            "Accepted offer for a Software Development Engineering internship for Spring 2027",
        ],
    },
    {
        "role": "Production Engineering Fellow",
        "org": "Meta × MLH Fellowship",
        "logo": "img/mh/meta_logo.jpg",
        "dates": "Jun 2026 – Present",
        "location": "Remote",
        "bullets": [
            "Selected for the competitive Production Engineering / SRE track of "
            "the MLH Fellowship powered by Meta; working hands-on with Linux, "
            "CI/CD, observability, and incident response — the foundations "
            "behind deploying software at scale.",
        ],
    },
    {
        "role": "Software Engineer (Industry Partnership)",
        "org": "Workday",
        "logo": "img/mh/workday_logo.jpg",
        "dates": "Jan 2026 – May 2026",
        "location": "On-Site",
        "bullets": [
            "Collaborated in an 8-person agile team to build an AI-Assisted Automated Web Penetration Testing Platform by orchestrating OWASP ZAP and Nikto through an automated scanning pipeline",
            "Developed frontend architecture with Next.js (React) and TypeScript, implementing routing, reusable API service layers and modular components",
            "Engineered real-time dashboard views to surface aggregated vulnerability findings, chronological scan histories and live metrics by integrating PostgreSQL-backed scan results via FastAPI endpoints",
        ],
    },
    {
        "role": "Associate",
        "org": "HackEurope",
        "logo": "img/mh/hackeurope_logo.jpg",
        "dates": "Feb 2026 – Feb 2026",
        "location": "On-Site",
        "bullets": [
            "Supporting Operations and Coordinating Sponsor Engagement for Europe's Largest Student Hackathon with over 4000+ applicants",
        ],
    },
    
]

# --- Projects ---
# Same data-driven shape as WORK/HOBBIES: each entry is a dict the projects
# template loops over. name + description are required; link and tech are
# optional (empty string means "no link / no stack shown").
PROJECTS = [
    {
        "name": "Stock Analyser",
        "description": (
            "Python tool for identifying trading patterns and correlations across portfolios. "
            "Surfaces actionable trading signals from thousands of data points in real-time."
        ),
        "tech": "Tech: Python, Pandas, NumPy, Seaborn",
    },
    {
        "name": "2D Game Engine",
        "description": (
            "High-performance C++ engine handling 10,000+ entities at 120 FPS with optimized rendering. "
            "Features robust memory management and 95%+ test coverage."
        ),
        "tech": "Tech: C++20, SFML, CMake, GTest, GitHub Actions",
    },
    {
        "name": "E-Commerce Web App",
        "description": (
            "Full-stack e-commerce web app with user auth, product management and payment integration. "
            "Implemented responsive UI and optimised backend performance for seamless user experience."
        ),
        "tech": "Tech: Next.js (React), TypeScript, Tailwind CSS, Node.js",
    },
]

# --- Education ---
EDUCATION = [
    {
        "degree": "Bachelor of Arts (Moderatorship) in Computer Science",
        "school": "Trinity College Dublin",
        "dates": "May 2028",
        "location": "Dublin, Ireland",
        "bullets": [
            "Entrance Exhibition Award recipient",
            "On track for First Class Honours (1.1)"
        ],
    },
    {
        "degree": "Leaving Certificate, 625 Points (Maximum Score)",
        "school": "St. Mary's CBS",
        "dates": "May 2024",
        "location": "Wexford, Ireland",
        "bullets": [
            "HL Applied Mathematics, HL Mathematics, HL Physics, HL Computer Science, HL Engineering, HL Technology, HL English, HL Irish",
            "Awards: All-Ireland Scholar 2024, Entrance Exhibition Award, 625/625 LC Points."
        ],
    },
]

# --- Skills, grouped by category ---
SKILLS = [
    {
        "category": "Languages",
        "entries": ["Java", "Python", "TypeScript/JavaScript", "C/C++", "VHDL", "ARM Assembly", "R", "HTML/CSS"],
    },
    {
        "category": "Technologies",
        "entries": ["React", "Next.js", "Tailwind CSS", "Git", "Linux/Unix", "REST APIs", "PostgreSQL", "FastAPI"],
    },
    {
        "category": "Certifications",
        "entries": ["Meta Full-Stack Developer (Ongoing)"],
    },
]

# --- Honors & awards ---
HONORS = [
    "JP McManus All-Ireland Scholar 2024",
    "Annual Book Prize - Trinity College Dublin",
    "Entrance Exhibition Award - Trinity College Dublin",
    "625/625 Leaving Certificate Points (Maximum Score)",
]

# --- Hobbies, each with an image ---
# Drop matching images into app/static/img/ to replace the placeholders.
HOBBIES = [
    {
        "name": "Chess",
        "img": "img/mh/chess.jpg",
        "blurb": "Strategy, tactics and foresight. A game where critical thinking shapes the outcome",
    },
    {
        "name": "Photography",
        "img": "img/mh/photography.jpg",
        "blurb": "Capturing nature through the lens. Exploring landscapes, wildlife and natural light to tell visual stories.",
    },
    {
        "name": "Robotics",
        "img": "img/mh/robotics.jpg",
        "blurb": "Tinkering with robotics and electronics. Exploring how robots interact with and perceive the world around them.",
    },
]

# --- Map: places visited / lived ---
# lat/lng drive the Leaflet markers on the map page. Add a dict to add a pin.
PLACES = [
    {"name": "Wexford, Ireland", "lat": 52.3360, "lng": -6.4630, "note": "Home."},
    {"name": "Dublin, Ireland", "lat": 53.3437, "lng": -6.2545, "note": "Trinity College Dublin"},
    {"name": "Enniscorthy, Ireland", "lat": 52.2297, "lng": -6.5678, "note": "Secondary School"},
    {"name": "Lisbon, Portugal", "lat": 38.7169, "lng": -9.1395, "note": "Holiday"},
    {"name": "Albufeira, Portugal", "lat": 37.0890, "lng": -8.2473, "note": "Holiday"},
    {"name": "Faro, Portugal", "lat": 37.0194, "lng": -7.9304, "note": "Holiday"},
    {"name": "Portimao, Portugal", "lat": 37.1310, "lng": -8.5370, "note": "Holiday"},
    {"name": "London, United Kingdom", "lat": 51.5074, "lng": -0.1278, "note": "Holiday"},
    {"name": "Dhaka, Bangladesh", "lat": 23.8103, "lng": 90.4125, "note": "Holiday"},
    {"name": "Pembroke, Wales", "lat": 51.6833, "lng": -4.9167, "note": "Cruise Trip"},
    {"name": "Dubai, United Arab Emirates", "lat": 25.276987, "lng": 55.296249, "note": "Layover"},
]
