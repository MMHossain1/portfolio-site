"""
Single source of truth for all portfolio content.

Everything the templates render comes from here. To add a new work
experience, project, education entry, skill group, publication, or map
location, append a dict to the relevant list below. The Jinja templates loop
over these lists, so no HTML changes are needed to add more items. This is what
satisfies the Flask task: "Add a template for adding multiple work
experiences/education/hobbies using Jinja".
"""

# --- Basic identity, used across every page ---
PROFILE = {
    "name": "Gabriela Sierocka",
    "tagline": "Builder & startup co-founder shipping production AI and full-stack systems.",
    "location": "Based in Europe · EU citizen",
    "blurb": (
        "Computer scientist by training and AI-native in practice. I take "
        "products from zero to one, integrate third-party APIs and OAuth "
        "flows, and drive adoption with executive and government stakeholders."
    ),
    # Place your real photo at app/static/img/profile.jpg to replace the placeholder.
    "photo": "img/profile.jpg",
    "email": "gsierocka@gmail.com",
    "phone": "+48 721 622 527",
    "github": "https://github.com/gabrielasie",
    "linkedin": "https://www.linkedin.com/in/gabriela-sierocka",
    # Set this if you have a public Google Scholar profile URL.
    "scholar": "",
}

# --- About section: a few paragraphs ---
ABOUT = [
    (
        "I'm a builder and startup co-founder who ships production AI and "
        "full-stack systems into real-world use. I work across the stack and "
        "in front of people: integrating third-party APIs and OAuth flows, "
        "taking products from zero to one, and driving adoption with executive "
        "and government decision-makers."
    ),
    (
        "I'm finishing a B.S. in Computer Science at the University of Notre "
        "Dame, with minors in Business Economics and Italian and membership in "
        "the Glynn Family Honors Program. Computer scientist by training and "
        "AI-native in practice, I'm most motivated when deploying AI against "
        "concrete customer problems."
    ),
    (
        "I'm an EU citizen based in Europe (no sponsorship required). When I'm "
        "not building, I'm out windsurfing, cooking, or on my bike."
    ),
]

# --- Work experiences (most recent first) ---
WORK = [
    {
        "role": "Production Engineering Fellow (SRE track)",
        "org": "Meta × MLH Fellowship",
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
        "role": "Full Stack Developer & AI Automation Ops Associate",
        "org": "Leadership Tap",
        "dates": "Oct 2025 – Jun 2026",
        "location": "South Bend, IN (Hybrid)",
        "bullets": [
            "Shipped a production full-stack platform (Next.js, TypeScript, "
            "Airtable) for an executive-coaching business, owning it from build "
            "to deployment with role-scoped access control and a relational "
            "data model for multi-coach operations.",
            "Designed and built a Microsoft Graph API integration (OAuth2 "
            "client-credentials, scheduled sync, intelligent filtering) that "
            "connected the product to clients' calendars and surfaced only "
            "genuine client-facing meetings.",
        ],
    },
    {
        "role": "Teaching Assistant, Ethical & Professional Issues in Computing",
        "org": "University of Notre Dame, Dept. of Computer Science & Engineering",
        "dates": "Aug 2025 – May 2026",
        "location": "Notre Dame, IN",
        "bullets": [
            "Led discussions on AI ethics, data privacy, and digital health for "
            "30+ students, translating complex technical and ethical concepts "
            "for non-specialist audiences and mentoring on professional practice.",
        ],
    },
    {
        "role": "Research & Policy Collaborator",
        "org": "Polish Hospital Federation (Donate Your Data Project)",
        "dates": "Apr 2021 – Jan 2026",
        "location": "Warsaw, Poland (Remote)",
        "bullets": [
            "Drove a national medical-data-donation white paper to real-world "
            "adoption — cited by Poland's Patient Ombudsman and shaping policy "
            "for an $80M Digital Medicine Center — engaging government and "
            "executive decision-makers directly.",
            "Co-architected a blockchain-based consent-management system, "
            "translating clinical and policy requirements into technical design "
            "(smart contracts, system architecture).",
            "Applied process mining to oncology patient pathways to surface and "
            "quantify systemic inefficiencies in care delivery.",
        ],
    },
    {
        "role": "Academic Research Assistant",
        "org": "University of Notre Dame, Dept. of Economics",
        "dates": "Aug 2024 – Jan 2025",
        "location": "Notre Dame, IN",
        "bullets": [
            "Designed and built a full-stack mobile cost-calculator (Flutter, "
            "Firebase) for rural Indian households and cleaned large survey "
            "datasets for econometric analysis, contributing to data-quality "
            "standards adopted for a peer-reviewed publication.",
        ],
    },
]

# --- Founding & projects ---
PROJECTS = [
    {
        "name": "CommuniCura",
        "role": "Co-Founder",
        "dates": "Sep 2024 – May 2026",
        "location": "Notre Dame, IN",
        "bullets": [
            "Co-founded and ran an assistive-AI startup that gives people with "
            "profound intellectual and multiple disabilities a voice, turning "
            "gaze and expression into communication with computer vision.",
            "Owned go-to-market, product design, and the early vision build; "
            "coordinated clinicians, university partners, and funding; and "
            "reached the semifinals of Notre Dame's McCloskey New Venture "
            "Competition (top 5%).",
        ],
        "link": {"label": "voice4pimd.org", "url": "https://voice4pimd.org"},
    },
    {
        "name": "Soma",
        "role": "Personal AI assistant with spoken daily briefings",
        "dates": "2026",
        "location": "Personal project",
        "bullets": [
            "Built end to end: pulls Oura, calendar, and weather into a daily "
            "brief, delivered as speech through the ElevenLabs API, with a "
            "deterministic engine making the decisions and an LLM only "
            "narrating. Public repo and demo.",
        ],
        "link": {"label": "github.com/gabrielasie/soma", "url": "https://github.com/gabrielasie/soma"},
    },
]

# --- Education ---
EDUCATION = [
    {
        "degree": "B.S. Computer Science",
        "school": "University of Notre Dame",
        "dates": "May 2026",
        "location": "Notre Dame, IN",
        "summary": (
            "Minors in Business Economics and Italian. Glynn Family Honors "
            "Program."
        ),
    },
    {
        "degree": "IB Diploma, 45/45 (maximum score)",
        "school": "1349 IB World School",
        "dates": "May 2022",
        "location": "Poznań, Poland",
        "summary": "HL Chemistry, Biology, and English.",
    },
]

# --- Skills, grouped by category ---
SKILLS = [
    {
        "category": "Technical",
        "entries": ["Python", "TypeScript (Next.js, React, Node.js)", "SQL", "C", "Flutter", "HTML/CSS"],
    },
    {
        "category": "AI / ML",
        "entries": [
            "LLM application development", "AI agents", "Prompt engineering", "RAG",
            "Computer vision", "AI-assisted dev (Claude Code, Cursor, GitHub Copilot)",
            "Anthropic & OpenAI APIs",
        ],
    },
    {
        "category": "Integrations & Cloud",
        "entries": [
            "REST APIs", "OAuth2", "Microsoft Graph API", "ElevenLabs API",
            "Git/GitHub", "Vercel", "Firebase", "Airtable", "Clerk", "Azure", "Render",
        ],
    },
    {
        "category": "Languages",
        "entries": [
            "English (fluent)", "Polish (native)", "Italian (advanced)", "Spanish (intermediate)",
        ],
    },
]

# --- Honors & awards ---
HONORS = [
    "University of Notre Dame Library Research Award, 1st Place (Capstone/Thesis)",
    "Award for Excellence in Italian Studies",
    "SprintND Hackathon, Force for Good Award",
]

# --- Publications ---
PUBLICATIONS = [
    {
        "authors": "Kornowska L, Slapal O, Sierocka G, et al.",
        "title": (
            "Analyzing the Gaps in Breast Cancer Diagnostics in Poland: A "
            "Retrospective Observational Study in the Data Donation Model."
        ),
        "venue": "Diagnostics (Basel). 2025;15(17):2127.",
        "note": "Impact Factor 3.3",
    },
    {
        "authors": "Sierocki W, Sierocka G, et al.",
        "title": (
            "Treatment Pathways in Breast Cancer in Poland: A Retrospective "
            "Observational Study in the Data Donation Model."
        ),
        "venue": "Nowotwory Journal of Oncology. 2025.",
        "note": "",
    },
]

# --- Hobbies, each with an image ---
# Drop matching images into app/static/img/ to replace the placeholders.
HOBBIES = [
    {
        "name": "Windsurfing",
        "img": "img/hobby-windsurfing.jpg",
        "blurb": "Wind, water, and balance. My favorite way to spend a day on the water.",
    },
    {
        "name": "Cooking",
        "img": "img/hobby-cooking.jpg",
        "blurb": "Mostly Italian, always from scratch. Cooking the way I like to build — slowly and with care.",
    },
    {
        "name": "Cycling",
        "img": "img/hobby-cycling.jpg",
        "blurb": "Long rides to clear my head and see a place at the right speed.",
    },
]

# --- Map: places visited / lived ---
# lat/lng drive the Leaflet markers on the map page. Add a dict to add a pin.
PLACES = [
    {"name": "Toruń, Poland", "lat": 53.0138, "lng": 18.5984, "note": "Home."},
    {"name": "Poznań, Poland", "lat": 52.4064, "lng": 16.9252, "note": "IB World School."},
    {"name": "Warsaw, Poland", "lat": 52.2297, "lng": 21.0122, "note": "Polish Hospital Federation."},
    {"name": "Notre Dame, USA", "lat": 41.7001, "lng": -86.2379, "note": "Undergrad & Leadership Tap."},
    {"name": "Amsterdam, NL", "lat": 52.3676, "lng": 4.9041, "note": "Currently passing through."},
    {"name": "Tokyo, Japan", "lat": 35.6762, "lng": 139.6503, "note": "Trip bookend."},
]
