import os
import json
from datetime import datetime
from flask import Flask, render_template_string, request, jsonify, send_from_directory

app = Flask(__name__)

# ==============================================================================
# BRAND, OFFICIAL GMAIL, HIERARCHICAL LEADERSHIP & 20 VERIFIED MANDATES
# ==============================================================================

COMPANY_INFO = {
    "name": "AUREVIA REALTORS",
    "tagline": "ELEVATE YOUR LIVING",
    "address": "1705, E Square, Plot No. C2, Sector 96, Noida, Uttar Pradesh - 201304",
    "email": "aureviarealtors@gmail.com",
    "primary_phone": "+919311111594",
    "primary_phone_styled": "(+91) 93111-11594",
    "whatsapp_default": "919311111594"
}

AUREVIA_MANIFESTO = {
    "headline": "Aurevia Realtors: The Crest of Sovereign Real Estate Advisory in Noida & NCR",
    "subheadline": "Where Architectural Grandeur Meets Institutional Integrity — Elevate Your Living",
    "paragraphs": [
        "Welcome to Aurevia Realtors, where architectural grandeur meets institutional integrity. Headquartered at the nerve center of the Noida-Greater Noida Expressway—1705, E Square, Plot No. C2, Sector 96, Noida—Aurevia Realtors was established with a singular, uncompromising mandate: to 'Elevate Your Living' through precision-engineered real estate advisory, transparent asset valuation, and enduring wealth creation. Derived from the timeless ideals of golden excellence ('Aureus') and a sovereign pathway ('Via'), our emblem—crowned in royal gold above deep emerald architectural peaks—symbolizes the pinnacle of trust, stability, and prosperity that defines every transaction under our banner.",
        "In a rapidly evolving real estate landscape across the National Capital Region, discerning homebuyers, corporate enterprises, and high-net-worth investors require far more than conventional property brokerage. They require a strategic custodian of capital. At Aurevia Realtors, we bridge the gap between aspiration and acquisition across five specialized verticals: Ultra-Luxury Residential Condominiums, Grade-A Commercial and Corporate Suites, Authority and Gated Island Plots, Verified Secondary Market Resale and Executive Leasing, and Bespoke Wilderness Farmhouses and Holiday Villas. Whether securing a primary allotment in a landmark sky-villa along Sector 128, structuring a high-yield corporate floor plate on the Expressway, or acquiring a legacy land parcel, our advisory protocol is anchored in rigorous due diligence.",
        "What distinguishes Aurevia Realtors is our strict zero-tolerance policy toward speculative or inflated listings. Every mandate showcased in our portfolio—spanning flagship developments by Eldeco Group, Godrej Properties, Hero Homes, Max Estates, Kalpataru, Sobha, ACE Group, ATS, and SKA, alongside our curated E Square commercial suites and Casa Corbett luxury retreats—undergoes a comprehensive verification of RERA compliance, clear title lineage, and real-time per-square-foot Base Selling Price (BSP) benchmarking. We empower our clients with factual market intelligence, comparative micro-market appreciation analytics, and direct-to-developer or direct-to-owner negotiation leverage, ensuring that every rupee deployed is fortified against risk and positioned for superior capital growth.",
        "Our organizational architecture is built for seamless execution and personal accountability. Under the supreme executive stewardship of our Director, Mr. Narendar Bhati, Aurevia Realtors operates through specialized departmental verticals led by three seasoned General Managers—Mr. Anand Basista (Resale & Fresh Projects), Mr. Himanshu Bhutai (Fresh Projects), and Mr. Apurv Mishra (Corporate & Luxury Leasing)—ensuring that every client mandate receives dedicated, domain-specific mastery. From initial portfolio consultation and private site walkthroughs to financial structuring, legal documentation, and long-term lease management, we remain a lifelong partner in your real estate journey.",
        "At Aurevia Realtors, we do not merely transact square footage; we curate legacies, fortify generational balance sheets, and shape the skylines where families and enterprises thrive. Step into our corporate suite in Sector 96, Noida, or write to us directly at aureviarealtors@gmail.com to experience real estate advisory elevated to a royal standard."
    ]
}

CATEGORIES = [
    "All",
    "Luxury Residential",
    "Commercial/Corporate Suites",
    "Plots/Land",
    "Resale & Leasing",
    "Farmhouses/Villas"
]

# SLIDE 1: SUPREME AUTHORITY — DIRECTOR PORTFOLIO & FULL JOURNEY
DIRECTOR = {
    "name": "Narendar Bhati",
    "role": "Director of the Company",
    "title_badge": "Supreme Executive Authority • Founder & Director",
    "phone": "9311111594",
    "phone_display": "(+91) 93111-11594",
    "email": "aureviarealtors@gmail.com",
    "initials": "NB",
    "quote": "Real estate is the most enduring vessel of generational wealth. At Aurevia Realtors, my commitment is to ensure that every client who walks through our doors invests with absolute clarity, sovereign security, and unmatched market advantage.",
    "description": [
        "Mr. Narendar Bhati serves as the Director and Supreme Executive Head of Aurevia Realtors. A deeply respected stalwart in the Noida, Greater Noida, and NCR real estate ecosystem, he brings an extraordinary blend of grassroots land intelligence, regulatory mastery, and institutional-grade portfolio advisory. Known for his sharp foresight along the Noida-Greater Noida Expressway and Yamuna corridors, Mr. Bhati has guided hundreds of high-net-worth families, industrialists, and corporate leaders in acquiring high-appreciation real estate assets.",
        "As the guiding force behind Aurevia Realtors, Mr. Bhati personally oversees developer alliances, primary land bank evaluations, ultra-luxury residential mandates, and complex commercial structuring. His leadership philosophy is rooted in absolute transparency: speaking with factual market numbers, safeguarding client capital above all else, and cultivating relationships that span decades rather than single transactions."
    ],
    "journey": [
        {
            "era": "Phase I • The Foundation",
            "title": "Grassroots Mastery of Noida & NCR Land Corridors",
            "detail": "Began his journey at the foundational level of the Gautam Buddha Nagar real estate belt, developing an encyclopedic command over Noida Authority regulations, land titles, sector master plans, and agricultural-to-urban transformation corridors."
        },
        {
            "era": "Phase II • Strategic Expansion",
            "title": "Pioneering High-Value Plots & Tier-1 Developer Mandates",
            "detail": "Transitioned into high-ticket residential plots across central Noida sectors and forged direct advisory relationships with India's premier Grade-A developers, earning a reputation for zero-litigation, high-ROI deal structuring."
        },
        {
            "era": "Phase III • Corporate & HNI Advisory",
            "title": "Structuring Institutional & Ultra-Luxury Portfolios",
            "detail": "Expanded into Grade-A commercial office plates along the Noida Expressway and luxury golf-facing condominiums, advising CXOs, business owners, and NRIs on balanced capital appreciation and rental yield strategies."
        },
        {
            "era": "Phase IV • The Royal Crest",
            "title": "Founding Aurevia Realtors at E Square, Sector 96",
            "detail": "Established Aurevia Realtors at 1705, E Square, Sector 96, Noida—uniting a handpicked leadership team of three specialized General Managers under one royal emblem to deliver transparent, full-spectrum real estate advisory."
        }
    ],
    "pillars": [
        "Supreme Oversight of All Company Mandates & Valuations",
        "Direct Tier-1 Developer & Authority Land Advisory",
        "Ultra-HNI & Family Office Real Estate Wealth Structuring",
        "100% Clean-Title & RERA-Compliant Governance"
    ]
}

# SLIDE 2: THE CORE TEAM — THREE GENERAL MANAGERS PORTFOLIO
GENERAL_MANAGERS = [
    {
        "name": "Anand Basista",
        "role": "General Manager",
        "department": "Resale and Fresh Project",
        "phone": "8287906328",
        "phone_display": "(+91) 82879-06328",
        "email": "aureviarealtors@gmail.com",
        "initials": "AB",
        "badge": "GM — Resale & Fresh Projects",
        "bio": "Operating under the strategic vision of the Director, Mr. Anand Basista leads Aurevia Realtors' verified secondary market resale mandates, authority plots, and flagship builder portfolios across Noida Expressway and Greater Noida.",
        "specialties": [
            "Verified Luxury Resale Inventory",
            "Expressway & Central Island Plots",
            "Flagship Under-Construction Mandates",
            "Direct Owner & Builder Negotiations"
        ]
    },
    {
        "name": "Himanshu Bhutai",
        "role": "General Manager",
        "department": "Fresh Project",
        "phone": "9990005736",
        "phone_display": "(+91) 99900-05736",
        "email": "aureviarealtors@gmail.com",
        "initials": "HB",
        "badge": "GM — Fresh Projects",
        "bio": "Spearheading primary developer launches, priority EOI allotments, and inaugural BSP inventory across Eldeco Group, Godrej Properties, Hero Homes, Sobha Limited, and luxury resort villas.",
        "specialties": [
            "2026 New Launch Priority Allotments",
            "Pre-Launch EOI & Inaugural BSP Deals",
            "Eldeco, Godrej, Hero & Sobha Desk",
            "Builder Payment Plan Structuring"
        ]
    },
    {
        "name": "Apurv Mishra",
        "role": "General Manager",
        "department": "Leasing",
        "phone": "9412880777",
        "phone_display": "(+91) 94128-80777",
        "email": "aureviarealtors@gmail.com",
        "initials": "AM",
        "badge": "GM — Corporate & Luxury Leasing",
        "bio": "Leading the company's Grade-A corporate office leasing along Noida Expressway (E Square, Sector 96 & IT/ITES corridors) alongside ready-to-move luxury residential rentals across Godrej, Eldeco, Kalpataru, and ATS societies.",
        "specialties": [
            "Grade-A Corporate Suites & IT Floor Plates",
            "Pre-Leased Commercial ROI Assets",
            "Expat & CXO Luxury Condominium Leasing",
            "Zero-Friction Tenant & Owner Representation"
        ]
    }
]

# ==============================================================================
# 20 VERIFIED PROJECTS WITH DISTINCT REALISTIC PHOTOS & DETAILED UNIT LAYOUTS
# ==============================================================================

PROPERTIES = [
    {
        "id": 1,
        "title": "Eldeco 7 Peaks Residences",
        "developer": "Eldeco Group",
        "category": "Luxury Residential",
        "stage": "New Launch",
        "status": "2026 New Launch • Open for Booking",
        "rera": "UPRERAPRJ106523/01/2026",
        "location": "Sector Omicron 1A, Greater Noida",
        "rate_per_sqft": "₹ 13,000 / Sq.Ft.",
        "price_range": "₹ 2.37 Cr – ₹ 4.81 Cr",
        "rental_yield": "7.5-Acre Low-Density Estate • 4 Units/Floor",
        "configs": "3 BHK, 3 BHK + Servant & 4 BHK + Servant (1,825 – 3,700 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + 3 Toilets (Luxury)",
                "size": "1,825 Sq.Ft. (Carpet: 1,150 Sq.Ft.)",
                "price": "₹ 2.37 Cr*",
                "inside_layout": "Entrance Foyer (6'x8') • L-Shaped Living & Dining (23'x14') • Master Suite with Dress & Bath (15'x12') • 2 Guest Bedrooms (12'x11') • Modular Kitchen + Utility Balcony • 6' Wide Running Sun-Deck",
                "rooms_blueprint": [
                    {"name": "Living & Dining Lounge", "dim": "23'0\" x 14'0\"", "zone": "Living"},
                    {"name": "Master Bedroom + Dress", "dim": "15'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedroom 2", "dim": "12'6\" x 11'0\"", "zone": "Private"},
                    {"name": "Bedroom 3", "dim": "12'0\" x 11'0\"", "zone": "Private"},
                    {"name": "Kitchen + Wet Utility", "dim": "11'0\" x 9'0\"", "zone": "Service"},
                    {"name": "Panoramic Running Deck", "dim": "24'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "3 BHK + Servant + 4 Toilets",
                "size": "2,250 Sq.Ft. (Carpet: 1,420 Sq.Ft.)",
                "price": "₹ 2.92 Cr*",
                "inside_layout": "Private Lift Foyer • Grand Living & Dining (25'x15') • 3 En-Suite Bedrooms • Enclosed Kitchen with Utility + Separate Servant Room & Toilet • 3-Side Open Wrap Balcony",
                "rooms_blueprint": [
                    {"name": "Grand Living & Dining", "dim": "25'0\" x 15'0\"", "zone": "Living"},
                    {"name": "Master Bedroom Suite", "dim": "16'0\" x 13'0\"", "zone": "Private"},
                    {"name": "Bedroom 2 (En-Suite)", "dim": "13'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedroom 3 (En-Suite)", "dim": "12'6\" x 11'6\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Quarter", "dim": "14'0\" x 10'0\"", "zone": "Service"},
                    {"name": "Wrap-Around Sky Deck", "dim": "28'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant + Family Lounge",
                "size": "2,850 – 3,700 Sq.Ft. (Penthouse/Duplex)",
                "price": "₹ 3.70 Cr – ₹ 4.81 Cr*",
                "inside_layout": "Double-Door Foyer + Powder Room • Formal Living + Family Lounge (28'x16') • 4 En-Suite Bedrooms with Walk-In Closets • Island Kitchen + Servant Quarter • 8' Deep Landscaped Terrace Deck",
                "rooms_blueprint": [
                    {"name": "Formal Living + Family Lounge", "dim": "28'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Presidential Master Suite", "dim": "18'0\" x 14'0\"", "zone": "Private"},
                    {"name": "Bedrooms 2, 3 & 4 (En-Suite)", "dim": "14'0\" x 12'0\" each", "zone": "Private"},
                    {"name": "Island Kitchen + Utility", "dim": "14'0\" x 11'0\"", "zone": "Service"},
                    {"name": "Servant Room + Service Entry", "dim": "8'0\" x 7'6\"", "zone": "Service"},
                    {"name": "Alpine View Sky Deck", "dim": "32'0\" x 8'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["7 Standalone Towers (Denali, Everest, Kili Open)", "All-Room VRV Air Conditioning", "Massive Central Open Greens", "Priority Fresh Allotment Desk"],
        "contact_person": "Himanshu Bhutai",
        "contact_role": "GM — Fresh Project",
        "contact_phone": "9990005736",
        "contact_phone_styled": "(+91) 99900-05736",
        "image": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 2,
        "title": "Eldeco Echoes of Eden",
        "developer": "Eldeco Group",
        "category": "Luxury Residential",
        "stage": "New Launch",
        "status": "2026 New Launch • Yamuna Expressway",
        "rera": "UPRERAPRJ125342/02/2026",
        "location": "Sector 22D, Yamuna Expressway, Greater Noida",
        "rate_per_sqft": "₹ 11,000 / Sq.Ft.",
        "price_range": "₹ 1.95 Cr – ₹ 3.20 Cr",
        "rental_yield": "High Airport & F1 Corridor Capital Appreciation",
        "configs": "3 BHK & 4 BHK Oxy-Rich VRV Homes (1,775 – 2,900 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + 3 Toilets (Eden Classic)",
                "size": "1,775 Sq.Ft.",
                "price": "₹ 1.95 Cr*",
                "inside_layout": "Arrival Foyer • Open-Plan Living & Dining (22'x13'6\") • 3 Well-Ventilated Bedrooms • L-Counter Kitchen with Utility Balcony • F1 Track / Central Park View Deck",
                "rooms_blueprint": [
                    {"name": "Living & Dining Hall", "dim": "22'0\" x 13'6\"", "zone": "Living"},
                    {"name": "Master Bedroom + Dress", "dim": "14'6\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedroom 2 & 3", "dim": "12'0\" x 11'0\"", "zone": "Private"},
                    {"name": "Kitchen + Utility", "dim": "10'6\" x 8'6\"", "zone": "Service"},
                    {"name": "Forest-Facing Balcony", "dim": "20'0\" x 5'6\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant + 5 Toilets (Eden Grand)",
                "size": "2,900 Sq.Ft.",
                "price": "₹ 3.19 Cr*",
                "inside_layout": "Private Lift Lobby • Expansive Living/Dining (27'x15'6\") + Powder Toilet • 4 Corner Bedrooms with Balconies • Closed Kitchen + Servant Room with Independent Access",
                "rooms_blueprint": [
                    {"name": "Grand Drawing & Dining", "dim": "27'0\" x 15'6\"", "zone": "Living"},
                    {"name": "Master Suite + Walk-in Wardrobe", "dim": "17'0\" x 13'0\"", "zone": "Private"},
                    {"name": "3 Additional En-Suite Bedrooms", "dim": "13'6\" x 11'6\"", "zone": "Private"},
                    {"name": "Wet & Dry Kitchen + Servant", "dim": "15'0\" x 10'0\"", "zone": "Service"},
                    {"name": "Corner Panoramic Deck", "dim": "28'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["15 Mins to Noida International Airport (Jewar)", "Adjacent to Buddh International Circuit", "VRV Air-Conditioned Luxury Towers", "Inaugural Launch Price Benefits"],
        "contact_person": "Himanshu Bhutai",
        "contact_role": "GM — Fresh Project",
        "contact_phone": "9990005736",
        "contact_phone_styled": "(+91) 99900-05736",
        "image": "https://images.unsplash.com/photo-1486325212027-8081e485255e?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 3,
        "title": "Eldeco La Vida Bella",
        "developer": "Eldeco Group",
        "category": "Luxury Residential",
        "stage": "Under Construction",
        "status": "Under Construction • RERA Approved",
        "rera": "UPRERAPRJ136219/04/2024",
        "location": "Sector 12, Greater Noida West",
        "rate_per_sqft": "₹ 11,387 / Sq.Ft.",
        "price_range": "₹ 2.16 Cr – ₹ 3.75 Cr",
        "rental_yield": "Spanish-Mediterranean Architecture • 11-Ft Ceiling",
        "configs": "3 BHK & 4 BHK Double-Height Deck Homes (1,905 – 3,300 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + 3 Toilets (Bella Luxe)",
                "size": "1,905 Sq.Ft.",
                "price": "₹ 2.16 Cr*",
                "inside_layout": "9-Ft Grand Digital Main Door • 11-Ft High Living & Dining Room (23'x14') • 3 Bedrooms with Spanish Arched Balconies • Modular Kitchen + Utility",
                "rooms_blueprint": [
                    {"name": "11-Ft High Living & Dining", "dim": "23'0\" x 14'0\"", "zone": "Living"},
                    {"name": "Master Bedroom + Dress", "dim": "15'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3", "dim": "12'0\" x 11'6\"", "zone": "Private"},
                    {"name": "Kitchen + Utility Area", "dim": "11'0\" x 9'0\"", "zone": "Service"},
                    {"name": "Mediterranean Arch Deck", "dim": "22'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant + 4 Toilets",
                "size": "2,755 – 3,300 Sq.Ft.",
                "price": "₹ 3.13 Cr – ₹ 3.75 Cr*",
                "inside_layout": "Private Foyer • Expansive Living/Dining (26'x16') • 4 En-Suite Bedrooms • Large Kitchen with Breakfast Counter + Servant Room • Central Lawn-Facing Deck",
                "rooms_blueprint": [
                    {"name": "Formal Living & Dining", "dim": "26'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Master Suite + Walk-in Closet", "dim": "17'0\" x 13'6\"", "zone": "Private"},
                    {"name": "Bedrooms 2, 3 & 4", "dim": "13'6\" x 12'0\"", "zone": "Private"},
                    {"name": "Gourmet Kitchen + Servant", "dim": "14'6\" x 10'0\"", "zone": "Service"},
                    {"name": "Club-Facing Verandah", "dim": "28'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["9-Foot Entrance Door & 11-Foot Floor-to-Floor Height", "All-Weather Swimming Pool & Rooftop Amenities", "Prime 130m Road Connectivity", "Fresh & Verified Resale Units Available"],
        "contact_person": "Anand Basista",
        "contact_role": "GM — Resale & Fresh",
        "contact_phone": "8287906328",
        "contact_phone_styled": "(+91) 82879-06328",
        "image": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 4,
        "title": "Eldeco Live By The Greens",
        "developer": "Eldeco Group",
        "category": "Resale & Leasing",
        "stage": "Ready to Move",
        "status": "Ready-to-Move Phase-1 & Nearing Possession",
        "rera": "UPRERAPRJ15172",
        "location": "Sector 150, Noida Expressway",
        "rate_per_sqft": "₹ 12,500 / Sq.Ft.",
        "price_range": "Sale: ₹ 1.42 Cr – ₹ 1.89 Cr",
        "rental_yield": "Lease Rate: ₹ 34,000 – ₹ 46,000 / Month",
        "configs": "2 BHK & 3 BHK Sports-Centric Residences (1,137 – 1,500 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "2 BHK + 2 Toilets (Green View)",
                "size": "1,137 Sq.Ft. (Carpet: 695 Sq.Ft.)",
                "price": "Sale: ₹ 1.42 Cr* | Rent: ₹ 34,000/mo",
                "inside_layout": "Living & Dining Room (19'x11'6\") opening to Cricket Ground Balcony • Master Bedroom (13'x11') • Second Bedroom (11'x10'6\") • Modular Kitchen + Utility",
                "rooms_blueprint": [
                    {"name": "Living & Dining Area", "dim": "19'0\" x 11'6\"", "zone": "Living"},
                    {"name": "Master Bedroom", "dim": "13'0\" x 11'0\"", "zone": "Private"},
                    {"name": "Kids / Guest Bedroom", "dim": "11'0\" x 10'6\"", "zone": "Private"},
                    {"name": "Kitchen + Utility", "dim": "9'6\" x 7'6\"", "zone": "Service"},
                    {"name": "Sports Arena Balcony", "dim": "16'0\" x 5'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "3 BHK + 3 Toilets (Corner Unit)",
                "size": "1,404 – 1,500 Sq.Ft. (Carpet: 890 Sq.Ft.)",
                "price": "Sale: ₹ 1.75 Cr – ₹ 1.89 Cr* | Rent: ₹ 45,000/mo",
                "inside_layout": "Spacious L-Living & Dining (21'x13') • 3 Corner Bedrooms with Cross-Ventilation • 3 Toilets • Kitchen with Wet Utility • Shaheed Bhagat Singh Park Facing Deck",
                "rooms_blueprint": [
                    {"name": "L-Shaped Living & Dining", "dim": "21'0\" x 13'0\"", "zone": "Living"},
                    {"name": "Master Bedroom + Dress", "dim": "14'0\" x 11'6\"", "zone": "Private"},
                    {"name": "Bedroom 2 & Bedroom 3", "dim": "11'6\" x 11'0\"", "zone": "Private"},
                    {"name": "Enclosed Kitchen + Utility", "dim": "10'0\" x 8'0\"", "zone": "Service"},
                    {"name": "Orchard View Sun Deck", "dim": "18'0\" x 5'6\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["Cricket Academy by Rohit Sharma (CricKingdom)", "Noida's Greenest Low-Density Sector 150", "Resort-Style Clubhouse & Citrus Orchard", "Immediate Resale & Rental Keys Available"],
        "contact_person": "Apurv Mishra",
        "contact_role": "GM — Leasing",
        "contact_phone": "9412880777",
        "contact_phone_styled": "(+91) 94128-80777",
        "image": "https://images.unsplash.com/photo-1580587771525-78b9dba3b914?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 5,
        "title": "Eldeco Green Meadows & Mystic Greens",
        "developer": "Eldeco Group",
        "category": "Resale & Leasing",
        "stage": "Ready to Move",
        "status": "100% Ready-to-Move Occupied Society",
        "rera": "Completed with OC • Immediate Registry",
        "location": "Sector Pi & Sector Omicron I, Greater Noida",
        "rate_per_sqft": "₹ 9,800 / Sq.Ft.",
        "price_range": "Sale: ₹ 1.35 Cr – ₹ 2.30 Cr",
        "rental_yield": "Lease Rate: ₹ 30,000 – ₹ 45,000 / Month",
        "configs": "2 BHK, 3 BHK & 3+Study Ready Apartments (1,380 – 2,350 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "2 BHK + Study / 3 BHK Classic",
                "size": "1,380 – 1,640 Sq.Ft.",
                "price": "Sale: ₹ 1.35 Cr – ₹ 1.60 Cr* | Rent: ₹ 30,000/mo",
                "inside_layout": "High-Carpet-Ratio Ready Layout • Living/Dining (20'x12') • 3 Spacious Bedrooms • 2/3 Bathrooms • Independent Kitchen • Wide Park-Facing Balconies",
                "rooms_blueprint": [
                    {"name": "Living & Dining Hall", "dim": "20'0\" x 12'6\"", "zone": "Living"},
                    {"name": "Master Bedroom", "dim": "14'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedroom 2 & Study/Bed 3", "dim": "12'0\" x 11'0\"", "zone": "Private"},
                    {"name": "Kitchen + Utility Balcony", "dim": "10'0\" x 8'6\"", "zone": "Service"},
                    {"name": "Meadows Park Balcony", "dim": "18'0\" x 5'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "3 BHK + Servant + Family Lounge",
                "size": "2,150 – 2,350 Sq.Ft.",
                "price": "Sale: ₹ 2.10 Cr – ₹ 2.30 Cr* | Rent: ₹ 45,000/mo",
                "inside_layout": "Low-Density Ready Floor Plan • Drawing + Dining + Lounge • 3 Large Bedrooms with Attached Baths • Servant Room • 3 Open Balconies Overlooking 22-Acre Greens",
                "rooms_blueprint": [
                    {"name": "Drawing, Dining & Lounge", "dim": "24'0\" x 14'6\"", "zone": "Living"},
                    {"name": "Master Suite", "dim": "15'6\" x 13'0\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3", "dim": "13'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Quarter", "dim": "13'0\" x 9'6\"", "zone": "Service"},
                    {"name": "3-Side Open Balconies", "dim": "24'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["22-Acre Lush Established Township", "Immediate Possession & Zero GST", "High Family & Corporate Tenant Occupancy", "Verified Direct Owner Resale & Lease Mandates"],
        "contact_person": "Apurv Mishra",
        "contact_role": "GM — Leasing",
        "contact_phone": "9412880777",
        "contact_phone_styled": "(+91) 94128-80777",
        "image": "https://images.unsplash.com/photo-1567496898669-ee935f5f647a?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 6,
        "title": "Godrej Tropical Isle",
        "developer": "Godrej Properties",
        "category": "Luxury Residential",
        "stage": "New Launch",
        "status": "Flagship Expressway Launch • RERA Approved",
        "rera": "UPRERAPRJ303390",
        "location": "Sector 146, Noida Expressway",
        "rate_per_sqft": "₹ 19,500 / Sq.Ft.",
        "price_range": "₹ 3.51 Cr – ₹ 6.33 Cr",
        "rental_yield": "Zero-Km Noida Expressway & Metro Frontage",
        "configs": "3 BHK, 3.5 BHK & 4 BHK Island-Themed Homes (1,800 – 3,250 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + 3 Toilets (Tropical Luxe)",
                "size": "1,800 Sq.Ft.",
                "price": "₹ 3.51 Cr*",
                "inside_layout": "Smart Foyer • Living & Dining (22'x14') with Lagoon Pool View • Master Bedroom with Walk-in Closet (15'x12') • 2 Bedrooms (12'x11') • Enclosed Kitchen + Utility",
                "rooms_blueprint": [
                    {"name": "Living & Dining Lounge", "dim": "22'0\" x 14'0\"", "zone": "Living"},
                    {"name": "Master Bedroom + Dress", "dim": "15'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3", "dim": "12'0\" x 11'0\"", "zone": "Private"},
                    {"name": "Modular Kitchen + Utility", "dim": "11'0\" x 8'6\"", "zone": "Service"},
                    {"name": "Lagoon-Facing Sun Deck", "dim": "21'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "3 BHK + Servant + Study (2,500 Sq.Ft.)",
                "size": "2,500 Sq.Ft.",
                "price": "₹ 4.87 Cr*",
                "inside_layout": "Private Lift Lobby • Grand Living/Dining (25'x15') • Home Office / Study • 3 En-Suite Bedrooms • Wet/Dry Kitchen + Servant Quarter • Wrap-Around Expressway View Deck",
                "rooms_blueprint": [
                    {"name": "Grand Living + Study", "dim": "25'0\" x 15'0\"", "zone": "Living"},
                    {"name": "Master Suite", "dim": "16'6\" x 13'0\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3 (En-Suite)", "dim": "13'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Room", "dim": "14'0\" x 10'0\"", "zone": "Service"},
                    {"name": "Expressway View Deck", "dim": "26'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant + Lounge (Island Crest)",
                "size": "3,250 Sq.Ft.",
                "price": "₹ 6.33 Cr*",
                "inside_layout": "Biometric Private Lift Foyer • 29'x16' Double-Zone Living & Dining • 4 All-Corner En-Suite Bedrooms • Island Kitchen + Servant Suite • 8-Ft Deep Sky Cabana Deck",
                "rooms_blueprint": [
                    {"name": "Double-Zone Living & Dining", "dim": "29'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Royal Master Suite + Bath", "dim": "18'0\" x 14'0\"", "zone": "Private"},
                    {"name": "3 Additional En-Suite Suites", "dim": "14'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Island Kitchen + Servant", "dim": "15'0\" x 11'0\"", "zone": "Service"},
                    {"name": "Sky Cabana Terrace Deck", "dim": "32'0\" x 8'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["Direct Access to Sector 146 Metro Station", "Lagoon-Style Swimming Pool & Beach Club", "Air Purification Technology in Every Tower", "30:40:30 Executive Payment Structure"],
        "contact_person": "Himanshu Bhutai",
        "contact_role": "GM — Fresh Project",
        "contact_phone": "9990005736",
        "contact_phone_styled": "(+91) 99900-05736",
        "image": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 7,
        "title": "Godrej Arden",
        "developer": "Godrej Properties",
        "category": "Luxury Residential",
        "stage": "New Launch",
        "status": "Fresh Launch • Priority EOI Open",
        "rera": "UPRERA Approved",
        "location": "Sigma III, Greater Noida",
        "rate_per_sqft": "₹ 12,800 / Sq.Ft.",
        "price_range": "₹ 2.30 Cr – ₹ 3.58 Cr",
        "rental_yield": "Direct Connectivity to Yamuna Expressway & Jewar Airport",
        "configs": "3 BHK, 3 BHK + Study & 4 BHK Residences (1,800 – 2,800 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + 3 Toilets (Arden Signature)",
                "size": "1,800 Sq.Ft.",
                "price": "₹ 2.30 Cr*",
                "inside_layout": "Entrance Foyer • Living & Dining (22'x13'6\") • 3 Bedrooms with Floor-to-Ceiling Windows • Modular Kitchen + Utility • Central Greens Balcony",
                "rooms_blueprint": [
                    {"name": "Living & Dining Lounge", "dim": "22'0\" x 13'6\"", "zone": "Living"},
                    {"name": "Master Bedroom", "dim": "14'6\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3", "dim": "12'0\" x 11'0\"", "zone": "Private"},
                    {"name": "Kitchen + Utility", "dim": "10'6\" x 8'6\"", "zone": "Service"},
                    {"name": "Garden Deck", "dim": "20'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant + 4 Toilets",
                "size": "2,800 Sq.Ft.",
                "price": "₹ 3.58 Cr*",
                "inside_layout": "Private Lift Lobby • Grand Living/Dining (26'x15'6\") • 4 En-Suite Bedrooms • Gourmet Kitchen + Servant Quarter • 270-Degree Open Estate Views",
                "rooms_blueprint": [
                    {"name": "Grand Living & Dining", "dim": "26'0\" x 15'6\"", "zone": "Living"},
                    {"name": "Master Suite + Dress", "dim": "16'6\" x 13'0\"", "zone": "Private"},
                    {"name": "3 En-Suite Bedrooms", "dim": "13'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Room", "dim": "14'0\" x 10'0\"", "zone": "Service"},
                    {"name": "Panoramic Estate Balcony", "dim": "28'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["Low-Density Green Sector", "Resort-Style Central Greens", "25 Mins to Noida International Airport", "Confirmed Fresh Allotments"],
        "contact_person": "Himanshu Bhutai",
        "contact_role": "GM — Fresh Project",
        "contact_phone": "9990005736",
        "contact_phone_styled": "(+91) 99900-05736",
        "image": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 8,
        "title": "Godrej Woods",
        "developer": "Godrej Properties",
        "category": "Resale & Leasing",
        "stage": "Ready to Move",
        "status": "Ready Phase-1 & Nearing Possession Towers",
        "rera": "UPRERAPRJ704730",
        "location": "Sector 43, Central Noida",
        "rate_per_sqft": "₹ 19,500 / Sq.Ft.",
        "price_range": "Sale: ₹ 4.07 Cr – ₹ 7.21 Cr",
        "rental_yield": "Lease Rate: ₹ 75,000 – ₹ 1.25 Lakh / Month",
        "configs": "3 BHK, 4 BHK & 5 BHK Forest Residences (2,088 – 3,700 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + Servant (Forest Edge)",
                "size": "2,088 Sq.Ft.",
                "price": "Sale: ₹ 4.07 Cr* | Rent: ₹ 75,000/mo",
                "inside_layout": "Foyer Entry • Living & Dining (23'x14') Overlooking 600+ Tree Urban Forest • 3 Bedrooms • Kitchen + Servant Room • Wooden-Deck Balcony",
                "rooms_blueprint": [
                    {"name": "Forest-View Living & Dining", "dim": "23'0\" x 14'0\"", "zone": "Living"},
                    {"name": "Master Bedroom Suite", "dim": "15'0\" x 12'6\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3", "dim": "12'6\" x 11'0\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Room", "dim": "13'0\" x 9'6\"", "zone": "Service"},
                    {"name": "Canopy Wood Deck", "dim": "22'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant + Lounge (Golf & Forest View)",
                "size": "3,150 – 3,700 Sq.Ft.",
                "price": "Sale: ₹ 6.14 Cr – ₹ 7.21 Cr* | Rent: ₹ 1.25L/mo",
                "inside_layout": "Private Elevator Lobby • Expansive Living/Dining (28'x16') • 4 En-Suite Bedrooms • Island Kitchen + Servant Quarter • Dual Balconies Facing Urban Forest & Noida Golf Course",
                "rooms_blueprint": [
                    {"name": "Private Lobby + Grand Lounge", "dim": "28'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Master Suite + Walk-in Closet", "dim": "17'6\" x 14'0\"", "zone": "Private"},
                    {"name": "3 Additional En-Suite Bedrooms", "dim": "14'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Gourmet Kitchen + Servant", "dim": "15'0\" x 10'6\"", "zone": "Service"},
                    {"name": "Dual Forest & Golf Decks", "dim": "30'0\" x 7'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["600+ Natural Trees Urban Forest", "Elevated Wooden Boardwalk", "Adjacent to Noida Golf Course", "Verified Resale & Rental Keys In Hand"],
        "contact_person": "Apurv Mishra",
        "contact_role": "GM — Leasing",
        "contact_phone": "9412880777",
        "contact_phone_styled": "(+91) 94128-80777",
        "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 9,
        "title": "Godrej Golf Links (Villas & Suites)",
        "developer": "Godrej Properties",
        "category": "Farmhouses/Villas",
        "stage": "Ready to Move",
        "status": "Ready Golf Villas + Newly Launched Golf Residences",
        "rera": "UPRERAPRJ16697",
        "location": "Sector 27, Near Pari Chowk, Greater Noida",
        "rate_per_sqft": "₹ 16,100 / Sq.Ft.",
        "price_range": "Suites: ₹ 2.85 Cr – ₹ 5.30 Cr | Villas: ₹ 6.50 Cr+",
        "rental_yield": "Lease Rate: ₹ 65,000 – ₹ 1.40 Lakh / Month",
        "configs": "3 & 4 BHK Golf Apartments (1,769 – 3,294 Sq.Ft.) & 4 BHK Golf Villas (4,000+ Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK / 4 BHK Golf View Apartment",
                "size": "1,769 – 3,294 Sq.Ft.",
                "price": "₹ 2.85 Cr – ₹ 5.30 Cr*",
                "inside_layout": "Golf-Facing Living & Dining • 3 or 4 Spacious Bedrooms • Modular Kitchen + Servant Room • Direct View of 9-Hole Championship Golf Course",
                "rooms_blueprint": [
                    {"name": "Golf-Facing Living & Dining", "dim": "24'0\" x 14'6\"", "zone": "Living"},
                    {"name": "Master Suite", "dim": "16'0\" x 13'0\"", "zone": "Private"},
                    {"name": "Guest Bedrooms", "dim": "13'0\" x 11'6\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Quarter", "dim": "13'6\" x 9'6\"", "zone": "Service"},
                    {"name": "Fairway View Deck", "dim": "25'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK Triplex Golf Villa (Crest / Evoke)",
                "size": "4,000 – 4,800 Sq.Ft. Built-Up",
                "price": "Sale: ₹ 6.50 Cr – ₹ 8.20 Cr* | Rent: ₹ 1.40L/mo",
                "inside_layout": "Ground + 2 Floors + Private Lawn + Rooftop Terrace • Double-Height Living Room • Private Internal Elevator Provision • 4 Master Suites • 2-Car Covered Porch + Servant Quarter",
                "rooms_blueprint": [
                    {"name": "GF: Double-Height Living & Lawn", "dim": "28'0\" x 18'0\"", "zone": "Living"},
                    {"name": "FF: 2 Master Suites + Family Lounge", "dim": "18'0\" x 14'0\" each", "zone": "Private"},
                    {"name": "SF: 2 Bedrooms + Entertainment Deck", "dim": "15'0\" x 13'0\" each", "zone": "Private"},
                    {"name": "Island Kitchen + Staff Quarters", "dim": "15'0\" x 11'0\"", "zone": "Service"},
                    {"name": "Private Backyard & Golf Terrace", "dim": "30'0\" x 15'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["100-Acre Integrated Golf Township", "9-Hole Championship Golf Course", "Ready-to-Move Villas & New Launch Towers", "5 Mins from Pari Chowk Metro"],
        "contact_person": "Anand Basista",
        "contact_role": "GM — Resale & Fresh",
        "contact_phone": "8287906328",
        "contact_phone_styled": "(+91) 82879-06328",
        "image": "https://images.unsplash.com/photo-1613977257363-707ba9348227?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 10,
        "title": "Godrej Nest & Palm Retreat",
        "developer": "Godrej Properties",
        "category": "Resale & Leasing",
        "stage": "Ready to Move",
        "status": "Ready Phase-1 Towers & Resort Residences",
        "rera": "UPRERAPRJ13521 / UPRERAPRJ745601",
        "location": "Sector 150, Noida Expressway",
        "rate_per_sqft": "₹ 14,800 / Sq.Ft.",
        "price_range": "Sale: ₹ 2.20 Cr – ₹ 4.51 Cr",
        "rental_yield": "Lease Rate: ₹ 48,000 – ₹ 80,000 / Month",
        "configs": "2 BHK, 3 BHK & 4 BHK Low-Rise & Iconic Towers (1,486 – 3,050 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + 3 Toilets (Resort Suite)",
                "size": "1,900 – 2,150 Sq.Ft.",
                "price": "Sale: ₹ 2.81 Cr – ₹ 3.18 Cr* | Rent: ₹ 55,000/mo",
                "inside_layout": "Foyer • Living & Dining (22'x14') Facing Central Lagoon & Skywalk • 3 Bedrooms • Modular Kitchen + Utility • 6-Ft Wide Resort Deck",
                "rooms_blueprint": [
                    {"name": "Living & Dining Hall", "dim": "22'0\" x 14'0\"", "zone": "Living"},
                    {"name": "Master Bedroom + Dress", "dim": "15'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3", "dim": "12'6\" x 11'0\"", "zone": "Private"},
                    {"name": "Kitchen + Utility", "dim": "11'0\" x 8'6\"", "zone": "Service"},
                    {"name": "Resort Pool Balcony", "dim": "22'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant (Iconic Tower)",
                "size": "3,050 Sq.Ft.",
                "price": "Sale: ₹ 4.51 Cr* | Rent: ₹ 80,000/mo",
                "inside_layout": "Private Foyer • 26'x16' Living & Dining • 4 En-Suite Bedrooms • Closed Kitchen + Servant Quarter • Uninterrupted 40-Acre Shaheed Bhagat Singh Park Views",
                "rooms_blueprint": [
                    {"name": "Grand Living & Dining", "dim": "26'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Master Suite", "dim": "17'0\" x 13'6\"", "zone": "Private"},
                    {"name": "3 Additional Bedrooms", "dim": "13'6\" x 12'0\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Room", "dim": "14'0\" x 10'0\"", "zone": "Service"},
                    {"name": "40-Acre Park View Deck", "dim": "28'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["24x7 Concierge & Iconic Glass Facade", "Low-Rise Resort Living next to 40-Acre Park", "Confirmed Resale & Executive Rental Options", "Zero-Overhead Wire Green Sector"],
        "contact_person": "Apurv Mishra",
        "contact_role": "GM — Leasing",
        "contact_phone": "9412880777",
        "contact_phone_styled": "(+91) 94128-80777",
        "image": "https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 11,
        "title": "Leafsong Retreat by Hero Homes",
        "developer": "Hero Homes (Hero Realty)",
        "category": "Luxury Residential",
        "stage": "New Launch",
        "status": "Oct 2026 New Launch • Priority Allotment Open",
        "rera": "UPRERAPRJ414014/10/2026",
        "location": "Sector MU, Greater Noida",
        "rate_per_sqft": "₹ 10,999 / Sq.Ft.",
        "price_range": "₹ 1.82 Cr – ₹ 2.51 Cr",
        "rental_yield": "4.6-Acre Resort-Themed IGBC Platinum Community",
        "configs": "3 BHK + 2T, 3 BHK + 3T & 3 BHK + Servant (1,656 – 2,289 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + 2 Toilets (Smart Wellness)",
                "size": "1,656 Sq.Ft.",
                "price": "₹ 1.82 Cr*",
                "inside_layout": "ERV Air-Purified Living & Dining (21'x13') • Master Bedroom with Italian Marble (14'x12') • 2 Bedrooms • Smart Kitchen + Utility • Healing Garden Balcony",
                "rooms_blueprint": [
                    {"name": "Living & Dining (ERV Filtered)", "dim": "21'0\" x 13'0\"", "zone": "Living"},
                    {"name": "Master Bedroom", "dim": "14'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3", "dim": "11'6\" x 11'0\"", "zone": "Private"},
                    {"name": "Modular Kitchen + Utility", "dim": "10'0\" x 8'6\"", "zone": "Service"},
                    {"name": "Wellness Garden Deck", "dim": "18'0\" x 5'6\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "3 BHK + Servant + 4 Toilets (Retreat Royale)",
                "size": "2,289 Sq.Ft.",
                "price": "₹ 2.51 Cr*",
                "inside_layout": "Private Foyer with Digital Lock • Grand Living & Dining (24'x15') • 3 En-Suite Bedrooms • Large Kitchen + Independent Servant Quarter • Dual Resort-Facing Decks",
                "rooms_blueprint": [
                    {"name": "Grand Living & Dining", "dim": "24'0\" x 15'0\"", "zone": "Living"},
                    {"name": "Master Suite + Dress", "dim": "16'0\" x 12'6\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3 (En-Suite)", "dim": "13'0\" x 11'6\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Room", "dim": "13'6\" x 9'6\"", "zone": "Service"},
                    {"name": "Dual Resort Balconies", "dim": "24'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["ERV AQI-Controlled Air Filtration Homes", "1 Lakh Sq.Ft. Club & Lifestyle Amenities", "Premium Marble Flooring & All-Weather AC", "Backed by the Trusted Hero Group Legacy"],
        "contact_person": "Himanshu Bhutai",
        "contact_role": "GM — Fresh Project",
        "contact_phone": "9990005736",
        "contact_phone_styled": "(+91) 99900-05736",
        "image": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 12,
        "title": "Hero Homes The Palatial & Wellness",
        "developer": "Hero Homes (Hero Realty)",
        "category": "Luxury Residential",
        "stage": "New Launch",
        "status": "New Launch & Ready Phase Options",
        "rera": "RERA Registered Hero Realty Portfolio",
        "location": "NCR Prime Expressway Corridors",
        "rate_per_sqft": "₹ 12,500 / Sq.Ft.",
        "price_range": "₹ 2.25 Cr – ₹ 3.60 Cr",
        "rental_yield": "Smart Home Automation & Zero-Vehicular Surface Movement",
        "configs": "3 BHK + Servant & 4 BHK + Servant (1,800 – 2,880 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + Servant (Wellness Edition)",
                "size": "1,800 – 2,100 Sq.Ft.",
                "price": "₹ 2.25 Cr – ₹ 2.62 Cr*",
                "inside_layout": "Voice-Automated Living & Dining (22'x14') • 3 Bedrooms with Wooden Flooring • Modular Kitchen + Servant Room • 85% Open Green View Deck",
                "rooms_blueprint": [
                    {"name": "Smart Living & Dining", "dim": "22'0\" x 14'0\"", "zone": "Living"},
                    {"name": "Master Bedroom Suite", "dim": "15'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3", "dim": "12'0\" x 11'0\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Quarter", "dim": "12'6\" x 9'0\"", "zone": "Service"},
                    {"name": "Central Greens Deck", "dim": "21'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant + Lounge (The Palatial)",
                "size": "2,880 Sq.Ft.",
                "price": "₹ 3.60 Cr*",
                "inside_layout": "Private Lift Lobby • Palatial Living & Dining (27'x16') • 4 En-Suite Bedrooms • Island Kitchen + Servant Suite • Wrap-Around Sky Verandah",
                "rooms_blueprint": [
                    {"name": "Palatial Living & Dining", "dim": "27'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Royal Master Suite", "dim": "17'0\" x 13'6\"", "zone": "Private"},
                    {"name": "3 En-Suite Bedrooms", "dim": "13'6\" x 12'0\"", "zone": "Private"},
                    {"name": "Wet/Dry Kitchen + Servant", "dim": "14'6\" x 10'0\"", "zone": "Service"},
                    {"name": "Wrap-Around Verandah", "dim": "28'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["85% Open Landscaped Greens & Healing Gardens", "Biometric Digital Locks & Smart Controls", "Dedicated Sports Arena & Heated Pool", "Direct Builder Price & Early-Bird Benefits"],
        "contact_person": "Himanshu Bhutai",
        "contact_role": "GM — Fresh Project",
        "contact_phone": "9990005736",
        "contact_phone_styled": "(+91) 99900-05736",
        "image": "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 13,
        "title": "Max Estates 128",
        "developer": "Max Estates",
        "category": "Luxury Residential",
        "stage": "Under Construction",
        "status": "Under Construction • RERA Approved",
        "rera": "UPRERAPRJ446459",
        "location": "Sector 128, Noida Expressway",
        "rate_per_sqft": "₹ 28,500 / Sq.Ft.",
        "price_range": "₹ 12.54 Cr – ₹ 15.96 Cr",
        "rental_yield": "Ultra-HNI Estate Living • 2 Units Per Core",
        "configs": "4 BHK & 5 BHK Bespoke Sky Villas (4,400 – 5,600 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "4 BHK + Family Lounge + 2 Staff Rooms",
                "size": "4,400 Sq.Ft. Built-Up",
                "price": "₹ 12.54 Cr*",
                "inside_layout": "2 Private Elevators Opening into Personal Foyer • 32'x18' Living & Dining + Family Lounge • 4 En-Suite Master Suites • Show Kitchen + Wet Kitchen + 2 Staff Quarters • 11-Ft Deep Wrap-Around Sky Deck",
                "rooms_blueprint": [
                    {"name": "Grand Salon, Dining & Family Lounge", "dim": "32'0\" x 18'0\"", "zone": "Living"},
                    {"name": "Presidential Master Suite + His/Her Dress", "dim": "20'0\" x 15'0\"", "zone": "Private"},
                    {"name": "3 Additional En-Suite Master Bedrooms", "dim": "16'0\" x 13'6\"", "zone": "Private"},
                    {"name": "Show Kitchen + Wet Kitchen + 2 Staff", "dim": "18'0\" x 12'0\"", "zone": "Service"},
                    {"name": "11-Ft Deep Wrap-Around Sky Deck", "dim": "42'0\" x 11'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "5 BHK Sky Villa + Study + 2 Staff Rooms",
                "size": "5,600 Sq.Ft. Built-Up",
                "price": "₹ 15.96 Cr*",
                "inside_layout": "Full-Floor-Plate Privacy • Formal Drawing + Informal Family Lounge + Private Study • 5 En-Suite Bedrooms with Spa Bathrooms • Dual Kitchens • 360-Degree Golf & Expressway Panorama",
                "rooms_blueprint": [
                    {"name": "Formal Salon + Lounge + Study", "dim": "38'0\" x 19'0\"", "zone": "Living"},
                    {"name": "Primary Master Suite + Spa Bath", "dim": "22'0\" x 16'0\"", "zone": "Private"},
                    {"name": "4 En-Suite Suites", "dim": "16'6\" x 14'0\"", "zone": "Private"},
                    {"name": "Chef's Kitchen + Service Block", "dim": "20'0\" x 13'0\"", "zone": "Service"},
                    {"name": "Panoramic Estate Terrace Deck", "dim": "50'0\" x 11'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["3 Towers on 10 Acres (80% Greens)", "Private Lift Lobby", "46,000 Sq.Ft. The Hub Clubhouse", "IGBC Platinum Pre-Certified"],
        "contact_person": "Anand Basista",
        "contact_role": "GM — Resale & Fresh",
        "contact_phone": "8287906328",
        "contact_phone_styled": "(+91) 82879-06328",
        "image": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 14,
        "title": "Kalpataru Vista",
        "developer": "Kalpataru Group",
        "category": "Resale & Leasing",
        "stage": "Ready to Move",
        "status": "Ready-to-Move / Nearing Occupation",
        "rera": "UPRERAPRJ14980",
        "location": "Sector 128, Wish Town, Noida Expressway",
        "rate_per_sqft": "₹ 21,500 / Sq.Ft.",
        "price_range": "Sale: ₹ 6.47 Cr – ₹ 8.91 Cr",
        "rental_yield": "Lease Rate: ₹ 1.15 Lakh – ₹ 1.60 Lakh / Month",
        "configs": "3 BHK + Servant & 4 BHK + Servant Golf Residences (3,011 – 4,145 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + Servant + Powder Room (Golf Facing)",
                "size": "3,011 Sq.Ft. (Carpet: 1,920 Sq.Ft.)",
                "price": "Sale: ₹ 6.47 Cr* | Rent: ₹ 1.15 Lakh/mo",
                "inside_layout": "Private Lift Foyer • 26'x16' Living & Dining Overlooking 18-Hole Golf Course • 3 En-Suite Bedrooms • Island Kitchen + Servant Room • 3-Side Open Wrap-Around Golf Deck",
                "rooms_blueprint": [
                    {"name": "Golf-Facing Living & Dining", "dim": "26'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Master Suite + Walk-in Wardrobe", "dim": "17'0\" x 13'6\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3 (En-Suite)", "dim": "14'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Kitchen + Utility + Servant", "dim": "14'6\" x 10'6\"", "zone": "Service"},
                    {"name": "18-Hole Golf Course Deck", "dim": "30'0\" x 7'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant + Family Lounge",
                "size": "3,905 – 4,145 Sq.Ft. (Carpet: 2,580 Sq.Ft.)",
                "price": "Sale: ₹ 8.39 Cr – ₹ 8.91 Cr* | Rent: ₹ 1.60 Lakh/mo",
                "inside_layout": "Biometric Private Lift Lobby • Grand Living + Dining + Family Lounge (30'x17') • 4 En-Suite Corner Bedrooms • Gourmet Kitchen + Servant Suite • Uninterrupted Golf Greens Panorama",
                "rooms_blueprint": [
                    {"name": "Grand Salon + Family Lounge", "dim": "30'0\" x 17'0\"", "zone": "Living"},
                    {"name": "Primary Golf Master Suite", "dim": "18'6\" x 14'6\"", "zone": "Private"},
                    {"name": "3 En-Suite Guest Suites", "dim": "14'6\" x 12'6\"", "zone": "Private"},
                    {"name": "Gourmet Kitchen + Staff Suite", "dim": "16'0\" x 11'0\"", "zone": "Service"},
                    {"name": "Wrap-Around Golf Verandah", "dim": "36'0\" x 7'6\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["18-Hole Graham Cooke Golf Course View", "3-Side Open Layouts", "Infinity Edge Pool", "Confirmed Resale & Lease Inventory"],
        "contact_person": "Apurv Mishra",
        "contact_role": "GM — Leasing",
        "contact_phone": "9412880777",
        "contact_phone_styled": "(+91) 94128-80777",
        "image": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 15,
        "title": "E Square Corporate Suites",
        "developer": "E Square Commercial",
        "category": "Commercial/Corporate Suites",
        "stage": "Ready to Move",
        "status": "Ready & Operational Grade-A Building",
        "rera": "Approved Commercial IT/ITES Plot C2",
        "location": "Plot No. C2, Sector 96, Noida Expressway",
        "rate_per_sqft": "Sale: ₹ 18,500 / Sq.Ft. | Lease: ₹ 95 / Sq.Ft.",
        "price_range": "Suites from ₹ 1.57 Cr | Lease from ₹ 80,000/mo",
        "rental_yield": "7.5% – 8.5% Pre-Leased & Warm-Shell ROI",
        "configs": "Executive Suites (850 – 1,500 Sq.Ft.) & Full Floor Plates (5,000 – 15,000 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "Furnished Executive Corporate Suite",
                "size": "850 – 1,500 Sq.Ft. Super Area",
                "price": "Sale: ₹ 1.57 Cr – ₹ 2.77 Cr* | Lease: ₹ 80K–1.42L/mo",
                "inside_layout": "Reception & Waiting Lounge • 1 MD Cabin + 2 Manager Cabins • 8-Seater Glass Boardroom • 12 to 22 Modular Workstations • Dry Pantry • Central HVAC & 100% Power Backup",
                "rooms_blueprint": [
                    {"name": "Reception & Visitor Lounge", "dim": "14'0\" x 10'0\"", "zone": "Living"},
                    {"name": "Director / MD Cabin", "dim": "15'0\" x 12'0\"", "zone": "Private"},
                    {"name": "8-Seater Conference Room", "dim": "16'0\" x 11'0\"", "zone": "Private"},
                    {"name": "Open Workstation Bay (16 Seats)", "dim": "24'0\" x 16'0\"", "zone": "Service"},
                    {"name": "Pantry & Server Room", "dim": "10'0\" x 8'0\"", "zone": "Service"}
                ]
            },
            {
                "unit_type": "Enterprise Corporate Floor Plate",
                "size": "5,000 – 15,000 Sq.Ft.",
                "price": "Lease: ₹ 95 / Sq.Ft. | Custom Sale Mandate",
                "inside_layout": "High-Speed 6-Passenger Lift Lobby • Column-Free Span • Dedicated Executive Restrooms & AHU Room • 80 to 200 Workstations + 6 Cabins + 20-Seater Boardroom + Cafeteria",
                "rooms_blueprint": [
                    {"name": "Exclusive Lift Lobby & Reception", "dim": "28'0\" x 14'0\"", "zone": "Living"},
                    {"name": "Executive Suite + 6 Cabins", "dim": "40'0\" x 18'0\"", "zone": "Private"},
                    {"name": "20-Seater Boardroom + 2 Meeting Rooms", "dim": "32'0\" x 16'0\"", "zone": "Private"},
                    {"name": "Main Workstation Floor (120+ Seats)", "dim": "85'0\" x 45'0\"", "zone": "Service"},
                    {"name": "Cafeteria, Server & Dedicated Washrooms", "dim": "30'0\" x 18'0\"", "zone": "Service"}
                ]
            }
        ],
        "highlights": ["Direct Zero-Km Noida Expressway Frontage", "100% Power Backup & Central HVAC", "Multi-Level Basement Parking", "Aurevia HQ Building — Instant Site Visit"],
        "contact_person": "Apurv Mishra",
        "contact_role": "GM — Leasing",
        "contact_phone": "9412880777",
        "contact_phone_styled": "(+91) 94128-80777",
        "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 16,
        "title": "Sobha Rivana",
        "developer": "Sobha Limited",
        "category": "Luxury Residential",
        "stage": "New Launch",
        "status": "New Launch • Fresh Booking",
        "rera": "UPRERA Registered Phase-1",
        "location": "Sector 1, Greater Noida West",
        "rate_per_sqft": "₹ 13,500 / Sq.Ft. (Inaugural BSP)",
        "price_range": "₹ 2.97 Cr – ₹ 4.38 Cr",
        "rental_yield": "Backward-Integrated Sobha Construction Quality",
        "configs": "3 BHK + Servant & 4 BHK + Servant Luxury Homes (2,200 – 3,250 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3 BHK + Servant + 4 Toilets",
                "size": "2,200 Sq.Ft.",
                "price": "₹ 2.97 Cr*",
                "inside_layout": "Sobha German-Precision Layout • Foyer + Living/Dining (24'x14'6\") • 3 En-Suite Bedrooms • Closed Kitchen + Utility + Servant Room • 6'6\" Deep Podium-Facing Balcony",
                "rooms_blueprint": [
                    {"name": "Living & Dining Lounge", "dim": "24'0\" x 14'6\"", "zone": "Living"},
                    {"name": "Master Bedroom + Dress", "dim": "15'6\" x 12'6\"", "zone": "Private"},
                    {"name": "Bedrooms 2 & 3 (En-Suite)", "dim": "13'0\" x 11'6\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Quarter", "dim": "13'6\" x 9'6\"", "zone": "Service"},
                    {"name": "Podium Garden Deck", "dim": "23'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4 BHK + Servant + Family Lounge",
                "size": "3,250 Sq.Ft.",
                "price": "₹ 4.38 Cr*",
                "inside_layout": "Private Lift Foyer • Grand Living/Dining + Family Lounge (28'x16') • 4 En-Suite Bedrooms • Large Kitchen + Servant Quarter • Dual Panoramic Decks",
                "rooms_blueprint": [
                    {"name": "Grand Living + Family Lounge", "dim": "28'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Master Suite", "dim": "17'6\" x 13'6\"", "zone": "Private"},
                    {"name": "3 En-Suite Bedrooms", "dim": "14'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Suite", "dim": "15'0\" x 10'6\"", "zone": "Service"},
                    {"name": "Olympic Pool View Deck", "dim": "30'0\" x 7'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["Low-Density Podium Design", "Olympic-Size Swimming Pool", "5 Mins from FNG & Hindon Bridge", "Priority Fresh Allotment Desk"],
        "contact_person": "Himanshu Bhutai",
        "contact_role": "GM — Fresh Project",
        "contact_phone": "9990005736",
        "contact_phone_styled": "(+91) 99900-05736",
        "image": "https://images.unsplash.com/photo-1582407947304-fd86f028f716?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 17,
        "title": "ACE Hanei",
        "developer": "ACE Group",
        "category": "Luxury Residential",
        "stage": "Under Construction",
        "status": "Under Construction • RERA Approved",
        "rera": "UPRERAPRJ677887",
        "location": "Sector 12, Greater Noida West",
        "rate_per_sqft": "₹ 13,200 / Sq.Ft.",
        "price_range": "₹ 4.21 Cr – ₹ 5.53 Cr",
        "rental_yield": "2 Units Per Core • Private Lift Lobby",
        "configs": "3.5 BHK + Servant (3,190 Sq.Ft.) & 4.5 BHK + Servant (4,190 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "3.5 BHK + Study + Servant (3,190 Sq.Ft.)",
                "size": "3,190 Sq.Ft.",
                "price": "₹ 4.21 Cr*",
                "inside_layout": "Private Elevator Foyer • 27'x16' Living & Dining + Powder Toilet • 3 En-Suite Bedrooms + Study/Puja Room • Island Kitchen + Servant Room • 8-Ft Wide Wrap-Around Sky Deck",
                "rooms_blueprint": [
                    {"name": "Private Foyer + Grand Living", "dim": "27'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Master Suite + Walk-in Closet", "dim": "17'6\" x 14'0\"", "zone": "Private"},
                    {"name": "2 En-Suite Bedrooms + Study", "dim": "14'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Island Kitchen + Servant", "dim": "15'0\" x 11'0\"", "zone": "Service"},
                    {"name": "8-Ft Wide Wrap Sky Deck", "dim": "34'0\" x 8'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "4.5 BHK + Lounge + Servant (4,190 Sq.Ft.)",
                "size": "4,190 Sq.Ft.",
                "price": "₹ 5.53 Cr*",
                "inside_layout": "2-Per-Core Mansion Floor Plan • 31'x17'6\" Living/Dining + Family Lounge • 4 En-Suite Master Suites • Wet & Dry Kitchen + Servant Quarter • 270-Degree Wrap-Around Balcony",
                "rooms_blueprint": [
                    {"name": "Mansion Living, Dining & Lounge", "dim": "31'0\" x 17'6\"", "zone": "Living"},
                    {"name": "Presidential Master Suite", "dim": "19'0\" x 15'0\"", "zone": "Private"},
                    {"name": "3 Additional En-Suite Suites", "dim": "15'0\" x 13'0\"", "zone": "Private"},
                    {"name": "Wet/Dry Kitchen + Servant", "dim": "16'6\" x 11'6\"", "zone": "Service"},
                    {"name": "270° Wrap-Around Sky Deck", "dim": "42'0\" x 8'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["6.5-Acre Corner Plot on 130m Road", "2 Apartments Per Core", "Wrap-Around Sky Balconies", "Grand Triple-Height Entrance Lobby"],
        "contact_person": "Anand Basista",
        "contact_role": "GM — Resale & Fresh",
        "contact_phone": "8287906328",
        "contact_phone_styled": "(+91) 82879-06328",
        "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 18,
        "title": "SKA Orion & ATS One Hamlet",
        "developer": "SKA Group & ATS Infrastructure",
        "category": "Resale & Leasing",
        "stage": "Ready to Move",
        "status": "100% Ready-to-Move Expressway Condominiums",
        "rera": "UPRERAPRJ186008 • OC Received",
        "location": "Sector 143B & Sector 104, Noida Expressway",
        "rate_per_sqft": "₹ 13,800 – ₹ 17,500 / Sq.Ft.",
        "price_range": "Sale: ₹ 2.62 Cr – ₹ 5.60 Cr",
        "rental_yield": "Lease Rate: ₹ 50,000 – ₹ 1.15 Lakh / Month",
        "configs": "3 BHK, 3+Study (1,900 – 2,500 Sq.Ft.) & 4 BHK + Servant (3,200 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "SKA Orion — 3 BHK + Study (Sec 143B)",
                "size": "1,900 – 2,500 Sq.Ft.",
                "price": "Sale: ₹ 2.62 Cr – ₹ 3.45 Cr* | Rent: ₹ 50K–65K/mo",
                "inside_layout": "Mivan Construction • Living & Dining (23'x14') • 3 Bedrooms + Study Room • 4 Toilets • Kitchen + Utility • Running Balcony Facing Expressway & Metro",
                "rooms_blueprint": [
                    {"name": "Living & Dining Hall", "dim": "23'0\" x 14'0\"", "zone": "Living"},
                    {"name": "Master Bedroom + Dress", "dim": "15'0\" x 12'0\"", "zone": "Private"},
                    {"name": "2 Bedrooms + Study Room", "dim": "12'6\" x 11'6\"", "zone": "Private"},
                    {"name": "Modular Kitchen + Utility", "dim": "11'6\" x 9'0\"", "zone": "Service"},
                    {"name": "Expressway View Deck", "dim": "24'0\" x 6'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "ATS One Hamlet — 4 BHK + Servant (Sec 104)",
                "size": "2,850 – 3,200 Sq.Ft.",
                "price": "Sale: ₹ 4.98 Cr – ₹ 5.60 Cr* | Rent: ₹ 95K–1.15L/mo",
                "inside_layout": "2 Apartments Per Floor • Entrance Foyer + Drawing & Dining (26'x16') • 4 En-Suite Bedrooms • Large Kitchen + Servant Quarter • Lush Central Lawn Views",
                "rooms_blueprint": [
                    {"name": "Drawing & Dining Lounge", "dim": "26'0\" x 16'0\"", "zone": "Living"},
                    {"name": "Master Bedroom Suite", "dim": "17'0\" x 13'6\"", "zone": "Private"},
                    {"name": "3 En-Suite Bedrooms", "dim": "14'0\" x 12'0\"", "zone": "Private"},
                    {"name": "Kitchen + Servant Quarter", "dim": "14'6\" x 10'0\"", "zone": "Service"},
                    {"name": "Central Greens Verandah", "dim": "28'0\" x 6'6\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["Walking Distance to Metro & Expressway", "Zero-Vacancy Corporate & Expat Rental Demand", "Immediate Registry & Key Handover", "Verified Direct Owner Inventory"],
        "contact_person": "Apurv Mishra",
        "contact_role": "GM — Leasing",
        "contact_phone": "9412880777",
        "contact_phone_styled": "(+91) 94128-80777",
        "image": "https://images.unsplash.com/photo-1515263487990-61b07816b324?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 19,
        "title": "Central Island & Expressway Plots",
        "developer": "Noida Authority & Gated Township Mandates",
        "category": "Plots/Land",
        "stage": "Ready to Move",
        "status": "Clear Title • Immediate Transfer",
        "rera": "Authority / Township Sanctioned",
        "location": "Sector 128, Sector 105 & Sector 93B, Noida",
        "rate_per_sqft": "₹ 2,40,000 – ₹ 2,95,000 / Sq.Yd.",
        "price_range": "₹ 6.00 Cr – ₹ 14.75 Cr",
        "rental_yield": "18%–24% Historical Annual Land Appreciation",
        "configs": "250 Sq.Yd. (2,250 Sq.Ft.), 300 Sq.Yd. (2,700 Sq.Ft.) & 500 Sq.Yd. (4,500 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "250 – 300 Sq.Yd. Authority / Gated Plot",
                "size": "2,250 – 2,700 Sq.Ft. Land Area",
                "price": "₹ 6.00 Cr – ₹ 7.80 Cr*",
                "inside_layout": "Plot Dimensions: 36' x 62.5' (or 40' x 67.5') • Sanctioned for Stilt Parking + 3 Independent Floors (Up to 6,000 Sq.Ft. Collectible Built-Up Area) • 12m/18m Road Frontage",
                "rooms_blueprint": [
                    {"name": "Stilt Floor: 4-6 Car Parking + Staff", "dim": "36'0\" x 62'6\" Plot", "zone": "Service"},
                    {"name": "Floor 1: 4 BHK Duplex / Independent Floor", "dim": "2,000 Sq.Ft. Per Floor", "zone": "Living"},
                    {"name": "Floor 2: 4 BHK Luxury Floor", "dim": "2,000 Sq.Ft. Per Floor", "zone": "Private"},
                    {"name": "Floor 3 + Rooftop Terrace Garden", "dim": "2,000 Sq.Ft. + Roof", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "450 – 500 Sq.Yd. Corner / Park-Facing Plot",
                "size": "4,050 – 4,500 Sq.Ft. Land Area",
                "price": "₹ 11.25 Cr – ₹ 14.75 Cr*",
                "inside_layout": "Plot Dimensions: 50' x 90' • Ideal for Bespoke Family Mansion with Private Lift, Basement Home Theatre, Front Lawn & Stilt + 3 Floors (Up to 10,500 Sq.Ft. Built-Up)",
                "rooms_blueprint": [
                    {"name": "Front Setback Lawn & 8-Car Stilt", "dim": "50'0\" x 90'0\" Plot", "zone": "Outdoor"},
                    {"name": "Ground/First: Grand Family Triplex", "dim": "3,400 Sq.Ft. Per Level", "zone": "Living"},
                    {"name": "6-8 En-Suite Master Suites + Lift", "dim": "18'0\" x 15'0\" each", "zone": "Private"},
                    {"name": "Rooftop Pool & Entertainment Deck", "dim": "3,000 Sq.Ft. Terrace", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["12m to 24m Wide Internal Roads", "Park-Facing & Corner Plot Options", "FAR Approved for Stilt + 3 Floors", "Direct Verified Seller Meetings"],
        "contact_person": "Anand Basista",
        "contact_role": "GM — Resale & Fresh",
        "contact_phone": "8287906328",
        "contact_phone_styled": "(+91) 82879-06328",
        "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=85"
    },
    {
        "id": 20,
        "title": "Casa Corbett Wilderness Villas",
        "developer": "Casa Corbett Hospitality",
        "category": "Farmhouses/Villas",
        "stage": "New Launch",
        "status": "Managed Luxury Holiday Villas & Cottages",
        "rera": "Freehold Registered Land Title",
        "location": "Jim Corbett National Park Corridor, Uttarakhand",
        "rate_per_sqft": "₹ 11,500 / Sq.Ft. (Fully Furnished)",
        "price_range": "₹ 1.66 Cr – ₹ 2.87 Cr",
        "rental_yield": "7% – 9% Assured Revenue Share + Complimentary Owner Stays",
        "configs": "1 BHK Luxury Pool Cottage (1,450 Sq.Ft.) & 2/3 BHK Private Pool Villa (2,500 Sq.Ft.)",
        "unit_layouts": [
            {
                "unit_type": "1 BHK Luxury Wilderness Suite + Plunge Pool",
                "size": "1,450 Sq.Ft. (Turnkey Furnished)",
                "price": "₹ 1.66 Cr*",
                "inside_layout": "Double-Height Timber-Roof Living Lounge (20'x14') • Master Suite with Open-to-Sky Rain Shower (16'x13') • Pantry & Bar Counter • Private Heated Plunge Pool & Wooden Gazebo",
                "rooms_blueprint": [
                    {"name": "Timber-Roof Living & Bar Lounge", "dim": "20'0\" x 14'0\"", "zone": "Living"},
                    {"name": "Master Suite + Skylight Bath", "dim": "16'0\" x 13'0\"", "zone": "Private"},
                    {"name": "Heated Plunge Pool + Sun Deck", "dim": "18'0\" x 10'0\"", "zone": "Outdoor"},
                    {"name": "Private Landscaped Lawn & Gazebo", "dim": "25'0\" x 16'0\"", "zone": "Outdoor"}
                ]
            },
            {
                "unit_type": "2 / 3 BHK Presidential Pool Villa",
                "size": "2,500 Sq.Ft. (Turnkey Furnished)",
                "price": "₹ 2.87 Cr*",
                "inside_layout": "Grand Glass-Front Living & Dining Pavilion • 2/3 En-Suite Forest Bedrooms • Private Swimming Pool (24'x12') • Bonfire Patio + Butler Quarter • 5-Star Resort Leaseback",
                "rooms_blueprint": [
                    {"name": "Glass-Front Living & Dining Pavilion", "dim": "26'0\" x 16'0\"", "zone": "Living"},
                    {"name": "2/3 Forest-Facing Master Suites", "dim": "16'0\" x 13'6\" each", "zone": "Private"},
                    {"name": "Private Swimming Pool & Jacuzzi", "dim": "24'0\" x 12'0\"", "zone": "Outdoor"},
                    {"name": "Bonfire Lawn & Al-Fresco Deck", "dim": "35'0\" x 20'0\"", "zone": "Outdoor"}
                ]
            }
        ],
        "highlights": ["Private Heated Plunge Pool & Gazebo", "5-Star Resort Operator Leaseback", "Lush Forest & River-Side Microclimate", "Zero Maintenance Hassle for Owners"],
        "contact_person": "Himanshu Bhutai",
        "contact_role": "GM — Fresh Project",
        "contact_phone": "9990005736",
        "contact_phone_styled": "(+91) 99900-05736",
        "image": "https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=1200&q=85"
    }
]

# ==============================================================================
# ULTRA-LUXURY LIGHT IVORY, EMERALD & GOLD FRONTEND TEMPLATE
# ==============================================================================

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ company.name }} — {{ company.tagline }} | Official Noida Real Estate Portal</title>
    <meta name="description" content="Aurevia Realtors (1705 E Square, Sector 96, Noida | aureviarealtors@gmail.com). Led by Director Narendar Bhati, with General Managers Anand Basista, Himanshu Bhutai, and Apurv Mishra.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        ivory: {
                            DEFAULT: '#FAF7F0',
                            warm: '#F3EDE0',
                            card: '#FFFFFF'
                        },
                        emerald: {
                            deep: '#0B2E1C',
                            rich: '#12422B',
                            soft: '#1B5A3C'
                        },
                        gold: {
                            light: '#F1D77E',
                            DEFAULT: '#C89D28',
                            dark: '#967010',
                            metallic: '#D4AF37'
                        }
                    },
                    fontFamily: {
                        serif: ['"Cormorant Garamond"', 'serif'],
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace']
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #FAF7F0;
            color: #0B2E1C;
            background-image: radial-gradient(rgba(212, 175, 55, 0.08) 1px, transparent 1px);
            background-size: 28px 28px;
        }
        .gold-text {
            background: linear-gradient(135deg, #8F6808 0%, #D4AF37 48%, #9B7412 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .gold-btn {
            background: linear-gradient(135deg, #BF9322 0%, #E7C96B 50%, #AE8216 100%);
            color: #0B2E1C;
            box-shadow: 0 8px 24px -6px rgba(200, 157, 40, 0.45);
        }
        .gold-btn:hover {
            filter: brightness(1.06);
            transform: translateY(-1px);
        }
        .emerald-btn {
            background: linear-gradient(135deg, #0B2E1C 0%, #164F33 100%);
            color: #FAF7F0;
        }
        .gold-border {
            border-color: rgba(212, 175, 55, 0.38);
        }
        .card-luxury {
            background: #FFFFFF;
            border: 1px solid rgba(212, 175, 55, 0.38);
            box-shadow: 0 18px 40px -15px rgba(11, 46, 28, 0.09);
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .card-luxury:hover {
            transform: translateY(-6px);
            border-color: #C89D28;
            box-shadow: 0 25px 50px -12px rgba(11, 46, 28, 0.16);
        }

        /* LUXURY PHONE NUMBER PILL STYLE */
        .phone-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.4rem 0.9rem 0.4rem 0.5rem;
            border-radius: 9999px;
            background: linear-gradient(135deg, #0B2E1C 0%, #164930 100%);
            border: 1.5px solid #D4AF37;
            color: #FAF7F0;
            font-family: "Plus Jakarta Sans", sans-serif;
            font-variant-numeric: tabular-nums;
            font-weight: 700;
            letter-spacing: 0.05em;
            box-shadow: 0 6px 18px -4px rgba(11, 46, 28, 0.35);
            transition: all 0.25s ease;
        }
        .phone-pill:hover {
            transform: translateY(-1px);
            border-color: #F1D77E;
            box-shadow: 0 10px 24px -4px rgba(212, 175, 55, 0.45);
        }
        .phone-pill-icon {
            width: 1.65rem;
            height: 1.65rem;
            border-radius: 9999px;
            background: linear-gradient(135deg, #BF9322 0%, #E7C96B 100%);
            color: #0B2E1C;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .phone-pill-light {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.38rem 0.9rem 0.38rem 0.5rem;
            border-radius: 9999px;
            background: #FAF7F0;
            border: 1.5px solid #C89D28;
            color: #0B2E1C;
            font-variant-numeric: tabular-nums;
            font-weight: 800;
            letter-spacing: 0.04em;
            box-shadow: 0 4px 14px -3px rgba(200, 157, 40, 0.25);
            transition: all 0.25s ease;
        }
        .phone-pill-light:hover {
            background: #0B2E1C;
            color: #F1D77E;
            border-color: #F1D77E;
        }
        @keyframes pulse-dot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.45; transform: scale(1.25); }
        }
        .live-dot {
            width: 7px;
            height: 7px;
            border-radius: 9999px;
            background-color: #22C55E;
            animation: pulse-dot 2s infinite;
        }

        @keyframes ticker {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .animate-ticker {
            display: flex;
            width: max-content;
            animation: ticker 55s linear infinite;
        }
        .animate-ticker:hover {
            animation-play-state: paused;
        }
        .drop-cap::first-letter {
            float: left;
            font-family: "Cormorant Garamond", serif;
            font-size: 3.6rem;
            line-height: 0.85;
            padding-right: 0.65rem;
            padding-top: 0.15rem;
            color: #967010;
            font-weight: 700;
        }
        .blueprint-grid {
            background-color: #0B2E1C;
            background-image:
                linear-gradient(rgba(212, 175, 55, 0.12) 1px, transparent 1px),
                linear-gradient(90deg, rgba(212, 175, 55, 0.12) 1px, transparent 1px);
            background-size: 20px 20px;
        }
    </style>
</head>
<body class="font-sans antialiased selection:bg-emerald-deep selection:text-gold-light">

    <!-- LIVE MARKET RATE TICKER BAR -->
    <div class="bg-emerald-deep text-ivory text-xs py-2 border-b border-gold/40 overflow-hidden">
        <div class="animate-ticker flex items-center gap-10 px-4">
            {% for prop in properties %}
            <div class="flex items-center gap-2 whitespace-nowrap">
                <span class="w-1.5 h-1.5 rounded-full bg-gold-light"></span>
                <span class="font-semibold text-gold-light">[{{ prop.stage }}] {{ prop.title }}:</span>
                <span class="text-ivory/90">{{ prop.rate_per_sqft }}</span>
                <span class="text-ivory/50">({{ prop.configs }})</span>
            </div>
            {% endfor %}
            {% for prop in properties %}
            <div class="flex items-center gap-2 whitespace-nowrap">
                <span class="w-1.5 h-1.5 rounded-full bg-gold-light"></span>
                <span class="font-semibold text-gold-light">[{{ prop.stage }}] {{ prop.title }}:</span>
                <span class="text-ivory/90">{{ prop.rate_per_sqft }}</span>
                <span class="text-ivory/50">({{ prop.configs }})</span>
            </div>
            {% endfor %}
        </div>
    </div>

    <!-- EXECUTIVE SUB-HEADER WITH STYLED PHONE PILL & OFFICIAL GMAIL -->
    <div class="bg-ivory-warm/95 text-emerald-deep text-xs py-2.5 px-4 border-b gold-border">
        <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-3">
            <div class="flex flex-wrap items-center gap-4">
                <span class="font-semibold flex items-center gap-1.5">
                    <svg class="w-3.5 h-3.5 text-gold-dark" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"></path></svg>
                    HQ: 1705, E Square, Plot No. C2, Sector 96, Noida
                </span>
                <span class="text-stone-300 hidden sm:inline">|</span>
                <a href="mailto:{{ company.email }}" class="inline-flex items-center gap-1.5 font-bold text-emerald-deep hover:text-gold-dark transition">
                    <span class="w-5 h-5 rounded-full bg-emerald-deep text-gold-light inline-flex items-center justify-center text-[10px]">✉</span>
                    {{ company.email }}
                </a>
            </div>

            <div class="flex flex-wrap items-center gap-2.5 ml-auto">
                <a href="tel:{{ director.phone }}" class="phone-pill text-[11px]">
                    <span class="phone-pill-icon">
                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/></svg>
                    </span>
                    <span class="text-gold-light font-semibold">Director:</span>
                    <span>{{ director.phone_display }}</span>
                    <span class="live-dot"></span>
                </a>
            </div>
        </div>
    </div>

    <!-- MAIN STICKY NAVIGATION -->
    <header class="sticky top-0 z-40 bg-ivory/95 backdrop-blur-md border-b gold-border shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-24 flex items-center justify-between">
            <a href="#" class="flex items-center gap-4 group">
                <div class="w-16 h-16 rounded-full bg-ivory flex items-center justify-center p-1 border-2 border-gold/50 shadow-md overflow-hidden">
                    <img src="/logo.jpeg" alt="Aurevia Realtors Logo" class="w-full h-full object-contain"
                         onerror="this.style.display='none'; document.getElementById('fallback-crest').style.display='flex';">
                    <div id="fallback-crest" style="display:none;" class="w-full h-full items-center justify-center">
                        <svg viewBox="0 0 100 100" class="w-14 h-14">
                            <circle cx="50" cy="50" r="46" fill="none" stroke="#C89D28" stroke-width="3"/>
                            <path d="M30 42 L25 24 L38 33 L50 16 L62 33 L75 24 L70 42 Z" fill="#D4AF37" stroke="#967010" stroke-width="1.5"/>
                            <path d="M16 74 L50 42 L84 74 L73 74 L50 52 L27 74 Z" fill="#0B2E1C"/>
                            <path d="M27 76 L50 54 L73 76" fill="none" stroke="#D4AF37" stroke-width="3.5"/>
                            <rect x="44" y="63" width="4.5" height="4.5" fill="#C89D28"/>
                            <rect x="51" y="63" width="4.5" height="4.5" fill="#C89D28"/>
                            <rect x="44" y="70" width="4.5" height="4.5" fill="#C89D28"/>
                            <rect x="51" y="70" width="4.5" height="4.5" fill="#C89D28"/>
                        </svg>
                    </div>
                </div>
                <div>
                    <span class="block font-serif text-3xl sm:text-4xl font-bold tracking-wider gold-text leading-none">AUREVIA</span>
                    <span class="block text-[11px] font-extrabold tracking-[0.34em] text-emerald-deep mt-1">— REALTORS —</span>
                    <span class="block text-[9px] tracking-[0.24em] text-stone-500 mt-0.5 uppercase font-semibold">Elevate Your Living</span>
                </div>
            </a>

            <nav class="hidden lg:flex items-center gap-6 text-sm font-semibold text-emerald-deep">
                <a href="#top-slide-manifesto" class="hover:text-gold-dark transition">About Aurevia</a>
                <a href="#leadership-showcase" onclick="switchLeadershipSlide(1)" class="hover:text-gold-dark transition">Director's Journey</a>
                <a href="#leadership-showcase" onclick="switchLeadershipSlide(2)" class="hover:text-gold-dark transition">GM Team (3)</a>
                <a href="#portfolio" class="hover:text-gold-dark transition">Projects & Layouts</a>
                <a href="#gmail-desk" class="hover:text-gold-dark transition flex items-center gap-1">
                    <span class="text-gold-dark">✉</span> Official Gmail
                </a>
                <a href="#contact" class="hover:text-gold-dark transition">Contact</a>
            </nav>

            <div class="flex items-center gap-3">
                <a href="#gmail-desk"
                   class="hidden sm:inline-flex items-center gap-2 px-4 py-2.5 rounded-full bg-white border border-gold/50 text-emerald-deep text-xs font-bold hover:bg-emerald-deep hover:text-gold-light transition shadow-sm">
                    ✉ {{ company.email }}
                </a>
                <a href="https://wa.me/919311111594?text=Hello%20Aurevia%20Realtors,%20I%20would%20like%20to%20request%20an%20official%20price%20sheet%20and%20floor%20plan%20brochure."
                   target="_blank"
                   class="gold-btn font-bold text-xs sm:text-sm px-5 py-3 rounded-full transition tracking-wide uppercase">
                    Get Price Sheet
                </a>
            </div>
        </div>
    </header>

    <!-- ========================================================================== -->
    <!-- TOP SLIDE: AUREVIA REALTORS GRAND BRAND SHOWCASE & 500-WORD WRITE-UP       -->
    <!-- ========================================================================== -->
    <section id="top-slide-manifesto" class="relative py-14 lg:py-20 border-b-2 border-gold/50 overflow-hidden"
             style="background: linear-gradient(180deg, #FAF7F0 0%, #F2EBDC 100%);">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-14">

            <div class="grid lg:grid-cols-12 gap-12 items-center">
                <!-- Left Brand Banner -->
                <div class="lg:col-span-7 space-y-6">
                    <div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-white border border-gold/50 shadow-sm">
                        <span class="w-2 h-2 rounded-full bg-emerald-deep"></span>
                        <span class="text-xs uppercase tracking-[0.22em] text-emerald-deep font-bold">
                            AUREVIA REALTORS • ELEVATE YOUR LIVING
                        </span>
                    </div>

                    <h1 class="font-serif text-4xl sm:text-6xl lg:text-[62px] font-bold text-emerald-deep leading-[1.08]">
                        Aurevia Realtors: <br/>
                        <span class="gold-text italic">Sovereign Real Estate</span> Advisory.
                    </h1>

                    <p class="text-stone-700 text-base sm:text-lg leading-relaxed max-w-2xl">
                        Headquartered at <strong>1705, E Square, Plot No. C2, Sector 96, Noida</strong>, <strong>Aurevia Realtors</strong> presents verified architectural floor plans, exact unit sizes, and transparent per-sq.ft. rates across <strong>Eldeco Group, Godrej Properties, Hero Homes, Max Estates, Kalpataru, and Sobha</strong>.
                    </p>

                    <div class="flex flex-wrap gap-2.5 pt-1">
                        <button onclick="filterDeveloper('Eldeco'); document.getElementById('portfolio').scrollIntoView({behavior: 'smooth'});"
                                class="text-xs font-extrabold px-4 py-2.5 rounded-full bg-emerald-deep text-gold-light border border-gold shadow-sm hover:opacity-95 transition">
                            ★ Eldeco Layouts (5)
                        </button>
                        <button onclick="filterDeveloper('Godrej'); document.getElementById('portfolio').scrollIntoView({behavior: 'smooth'});"
                                class="text-xs font-extrabold px-4 py-2.5 rounded-full bg-emerald-deep text-gold-light border border-gold shadow-sm hover:opacity-95 transition">
                            ★ Godrej Layouts (5)
                        </button>
                        <button onclick="filterDeveloper('Hero Homes'); document.getElementById('portfolio').scrollIntoView({behavior: 'smooth'});"
                                class="text-xs font-extrabold px-4 py-2.5 rounded-full bg-emerald-deep text-gold-light border border-gold shadow-sm hover:opacity-95 transition">
                            ★ Hero Homes Layouts (2)
                        </button>
                        <button onclick="filterStage('Ready to Move'); document.getElementById('portfolio').scrollIntoView({behavior: 'smooth'});"
                                class="text-xs font-bold px-4 py-2.5 rounded-full bg-white border border-gold/50 text-emerald-deep hover:bg-emerald-deep hover:text-gold-light transition shadow-sm">
                            🟢 Ready to Move
                        </button>
                        <button onclick="filterStage('New Launch'); document.getElementById('portfolio').scrollIntoView({behavior: 'smooth'});"
                                class="text-xs font-bold px-4 py-2.5 rounded-full bg-white border border-gold/50 text-emerald-deep hover:bg-emerald-deep hover:text-gold-light transition shadow-sm">
                            ✨ 2026 New Launches
                        </button>
                    </div>
                </div>

                <!-- Right Hierarchical Command Card with Restyled Phone Badges -->
                <div class="lg:col-span-5">
                    <div class="bg-white rounded-3xl p-7 border-2 border-gold/50 shadow-2xl space-y-5">
                        <div class="flex items-center gap-4 pb-4 border-b border-stone-200">
                            <img src="/logo.jpeg" alt="Aurevia Realtors Crest" class="w-20 h-20 object-contain rounded-2xl border border-gold/40 p-1 bg-ivory"
                                 onerror="this.style.display='none'">
                            <div>
                                <span class="text-[10px] uppercase tracking-[0.24em] text-gold-dark font-extrabold">Aurevia Realtors</span>
                                <h3 class="font-serif text-2xl font-bold text-emerald-deep mt-0.5">Executive Command Desk</h3>
                                <a href="mailto:{{ company.email }}" class="text-xs font-bold text-gold-dark hover:underline block mt-0.5">
                                    ✉ {{ company.email }}
                                </a>
                            </div>
                        </div>

                        <!-- 1. SUPREME HEAD: DIRECTOR -->
                        <div class="p-5 rounded-2xl bg-emerald-deep text-ivory border-2 border-gold shadow-lg space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="inline-block text-[10px] font-extrabold uppercase tracking-[0.2em] px-3 py-1 rounded-full bg-gold/20 text-gold-light border border-gold/40">
                                    👑 Supreme Head • {{ director.role }}
                                </span>
                                <span class="live-dot"></span>
                            </div>
                            <div class="flex flex-wrap items-center justify-between gap-3">
                                <div>
                                    <p class="font-serif text-2xl font-bold text-white">{{ director.name }}</p>
                                    <a href="tel:{{ director.phone }}" class="phone-pill-light text-xs mt-2">
                                        <span class="phone-pill-icon">
                                            <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/></svg>
                                        </span>
                                        <span class="font-mono tracking-wider">{{ director.phone_display }}</span>
                                    </a>
                                </div>
                                <div class="flex gap-2">
                                    <a href="https://wa.me/91{{ director.phone }}" target="_blank" class="px-4 py-2.5 rounded-xl gold-btn text-xs font-extrabold uppercase tracking-wider">WhatsApp</a>
                                </div>
                            </div>
                        </div>

                        <!-- 2. THREE GENERAL MANAGERS TEAM -->
                        <div>
                            <div class="flex items-center justify-between mb-2.5">
                                <span class="text-[11px] font-extrabold uppercase tracking-widest text-stone-500">General Managers Team (3)</span>
                                <a href="#leadership-showcase" onclick="switchLeadershipSlide(2)" class="text-[11px] font-bold text-gold-dark hover:underline">Open GM Slide →</a>
                            </div>
                            <div class="grid grid-cols-1 gap-2.5">
                                {% for gm in general_managers %}
                                <div class="p-3 rounded-2xl bg-ivory border border-gold/40 flex flex-wrap items-center justify-between gap-2">
                                    <div>
                                        <span class="text-[9px] font-extrabold uppercase tracking-wider text-emerald-rich block">{{ gm.role }} — {{ gm.department }}</span>
                                        <p class="font-serif text-lg font-bold text-emerald-deep leading-snug">{{ gm.name }}</p>
                                    </div>
                                    <div class="flex items-center gap-1.5">
                                        <a href="tel:{{ gm.phone }}" class="phone-pill text-[11px]">
                                            <span class="phone-pill-icon">
                                                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/></svg>
                                            </span>
                                            <span class="font-mono text-[11px]">{{ gm.phone_display }}</span>
                                        </a>
                                        <a href="https://wa.me/91{{ gm.phone }}" target="_blank" class="px-3 py-2 rounded-full gold-btn text-[11px] font-bold">WA</a>
                                    </div>
                                </div>
                                {% endfor %}
                            </div>
                        </div>

                    </div>
                </div>
            </div>

            <!-- 500-WORD EDITORIAL WRITE-UP FOR AUREVIA REALTORS -->
            <div class="bg-white rounded-3xl p-8 sm:p-12 lg:p-14 border-2 border-gold/60 shadow-2xl relative">
                <div class="flex flex-col md:flex-row md:items-center justify-between pb-8 mb-8 border-b border-gold/40 gap-4">
                    <div>
                        <span class="text-xs uppercase tracking-[0.28em] text-gold-dark font-extrabold block">
                            Official Corporate Charter & Brand Chronicle
                        </span>
                        <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-emerald-deep mt-1">
                            {{ manifesto.headline }}
                        </h2>
                        <p class="font-serif italic text-lg sm:text-xl text-gold-dark mt-1">
                            {{ manifesto.subheadline }}
                        </p>
                    </div>
                    <div class="shrink-0 flex items-center gap-3 px-4 py-2.5 rounded-2xl bg-ivory border border-gold/40">
                        <span class="w-3 h-3 rounded-full bg-emerald-deep"></span>
                        <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-deep">Aurevia Realtors • Est. Sector 96, Noida</span>
                    </div>
                </div>

                <div class="grid lg:grid-cols-2 gap-8 text-stone-700 text-sm sm:text-[15px] leading-[1.85] text-justify">
                    <div class="space-y-5">
                        <p class="drop-cap">{{ manifesto.paragraphs[0] }}</p>
                        <p>{{ manifesto.paragraphs[1] }}</p>
                    </div>
                    <div class="space-y-5">
                        <p>{{ manifesto.paragraphs[2] }}</p>
                        <p>{{ manifesto.paragraphs[3] }}</p>
                        <div class="p-5 rounded-2xl bg-emerald-deep text-ivory border border-gold">
                            <p class="font-serif italic text-base sm:text-lg text-gold-light leading-relaxed">
                                "{{ manifesto.paragraphs[4] }}"
                            </p>
                            <p class="text-[11px] uppercase tracking-[0.24em] text-ivory/80 font-bold mt-2">
                                — AUREVIA REALTORS • {{ company.email }}
                            </p>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- ========================================================================== -->
    <!-- DEDICATED TWO-SLIDE LEADERSHIP SHOWCASE (SLIDE 1: DIRECTOR | SLIDE 2: GMs) -->
    <!-- ========================================================================== -->
    <section id="leadership-showcase" class="py-16 lg:py-24 bg-emerald-deep text-ivory relative overflow-hidden border-b-2 border-gold">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

            <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
                <div>
                    <span class="text-xs uppercase tracking-[0.28em] text-gold-light font-extrabold">Aurevia Realtors Corporate Structure</span>
                    <h2 class="font-serif text-3xl sm:text-5xl font-bold text-white mt-1">Leadership & Executive Hierarchy</h2>
                </div>

                <div class="inline-flex p-1.5 rounded-full bg-emerald-rich border border-gold/40 self-start md:self-auto">
                    <button id="tab-slide-1" onclick="switchLeadershipSlide(1)"
                            class="px-5 py-2.5 rounded-full text-xs font-extrabold uppercase tracking-wider transition gold-btn">
                        Slide 1: Director's Portfolio & Journey
                    </button>
                    <button id="tab-slide-2" onclick="switchLeadershipSlide(2)"
                            class="px-5 py-2.5 rounded-full text-xs font-extrabold uppercase tracking-wider transition text-ivory/80 hover:text-white">
                        Slide 2: General Managers Team (3)
                    </button>
                </div>
            </div>

            <!-- SLIDE 1: DIRECTOR'S PORTFOLIO, DESCRIPTION & COMPLETE JOURNEY -->
            <div id="leadership-slide-1" class="slide-panel">
                <div class="bg-gradient-to-br from-ivory via-ivory to-ivory-warm text-emerald-deep rounded-3xl p-8 sm:p-12 lg:p-14 border-2 border-gold shadow-2xl space-y-12">

                    <div class="grid lg:grid-cols-12 gap-10 items-start">
                        <div class="lg:col-span-5">
                            <div class="bg-emerald-deep text-ivory rounded-3xl p-8 border-2 border-gold shadow-xl">
                                <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-gold/20 border border-gold text-gold-light text-[10px] font-extrabold uppercase tracking-[0.2em] mb-6">
                                    👑 Supreme Head of Aurevia Realtors
                                </div>

                                <div class="w-28 h-28 rounded-3xl bg-gradient-to-br from-gold-light via-gold to-gold-dark text-emerald-deep flex items-center justify-center font-serif text-5xl font-bold shadow-lg border-2 border-white/40 mb-6">
                                    {{ director.initials }}
                                </div>

                                <h3 class="font-serif text-4xl sm:text-5xl font-bold text-white leading-none">{{ director.name }}</h3>
                                <p class="text-sm font-extrabold uppercase tracking-[0.22em] text-gold-light mt-2">{{ director.role }}</p>
                                <p class="text-xs text-ivory/75 mt-1">Aurevia Realtors • 1705, E Square, Sector 96, Noida</p>

                                <div class="mt-6 pt-6 border-t border-gold/30 space-y-4">
                                    <div>
                                        <span class="text-[10px] uppercase tracking-widest text-ivory/60 block mb-2">Director's Executive Line</span>
                                        <a href="tel:{{ director.phone }}" class="phone-pill-light text-sm">
                                            <span class="phone-pill-icon">
                                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/></svg>
                                            </span>
                                            <span class="font-mono text-base">{{ director.phone_display }}</span>
                                            <span class="live-dot"></span>
                                        </a>
                                    </div>

                                    <div>
                                        <span class="text-[10px] uppercase tracking-widest text-ivory/60 block mb-1">Official Gmail Desk</span>
                                        <a href="mailto:{{ director.email }}" class="text-xs font-bold text-gold-light hover:underline">
                                            ✉ {{ director.email }}
                                        </a>
                                    </div>

                                    <div class="grid grid-cols-2 gap-3 pt-2">
                                        <a href="tel:{{ director.phone }}"
                                           class="py-3 rounded-xl bg-ivory text-emerald-deep font-bold text-xs uppercase tracking-wider text-center hover:bg-white transition">
                                            Call Director
                                        </a>
                                        <a href="https://wa.me/91{{ director.phone }}?text=Respected%20Mr.%20Narendar%20Bhati%20(Director%20-%20Aurevia%20Realtors),%20I%20would%20like%20to%20schedule%20an%20executive%20consultation."
                                           target="_blank"
                                           class="py-3 rounded-xl gold-btn font-bold text-xs uppercase tracking-wider text-center">
                                            WhatsApp Desk
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="lg:col-span-7 space-y-5">
                            <div class="inline-block px-4 py-1.5 rounded-full bg-emerald-deep/10 border border-gold/50 text-emerald-deep text-xs font-extrabold uppercase tracking-[0.2em]">
                                Slide 01 / 02 — Executive Profile & Description of the Director
                            </div>

                            <h3 class="font-serif text-3xl sm:text-5xl font-bold text-emerald-deep leading-tight">
                                {{ director.name }} — <span class="gold-text italic">Architect of Trust & Vision.</span>
                            </h3>

                            <blockquote class="p-5 rounded-2xl bg-white border-l-4 border-gold shadow-sm font-serif italic text-lg sm:text-xl text-emerald-deep leading-relaxed">
                                "{{ director.quote }}"
                            </blockquote>

                            {% for para in director.description %}
                            <p class="text-stone-700 text-sm sm:text-[15px] leading-relaxed text-justify">
                                {{ para }}
                            </p>
                            {% endfor %}

                            <div class="pt-2">
                                <p class="text-xs font-extrabold uppercase tracking-widest text-gold-dark mb-3">Direct Executive Governance Pillars:</p>
                                <div class="grid sm:grid-cols-2 gap-3">
                                    {% for pillar in director.pillars %}
                                    <div class="p-3.5 rounded-xl bg-white border gold-border flex items-center gap-2.5 text-xs font-bold text-emerald-deep shadow-sm">
                                        <span class="w-5 h-5 rounded-full bg-emerald-deep text-gold-light flex items-center justify-center text-[10px] shrink-0">✓</span>
                                        {{ pillar }}
                                    </div>
                                    {% endfor %}
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- THE JOURNEY OF THE DIRECTOR -->
                    <div class="pt-10 border-t-2 border-gold/40">
                        <div class="flex flex-col sm:flex-row sm:items-end justify-between mb-8 gap-4">
                            <div>
                                <span class="text-xs uppercase tracking-[0.25em] text-gold-dark font-extrabold">Leadership Chronicle</span>
                                <h4 class="font-serif text-3xl sm:text-4xl font-bold text-emerald-deep mt-1">
                                    The Journey of Director Narendar Bhati
                                </h4>
                            </div>
                            <span class="text-xs font-bold text-emerald-rich bg-white px-4 py-2 rounded-full border gold-border">
                                From Grassroots Land Mastery to Founding Aurevia Realtors
                            </span>
                        </div>

                        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                            {% for step in director.journey %}
                            <div class="bg-white rounded-2xl p-6 border-2 border-gold/40 shadow-md flex flex-col justify-between relative">
                                <div>
                                    <span class="inline-block text-[10px] font-extrabold uppercase tracking-widest px-3 py-1 rounded-full bg-emerald-deep text-gold-light mb-3">
                                        {{ step.era }}
                                    </span>
                                    <h5 class="font-serif text-xl font-bold text-emerald-deep leading-snug">
                                        {{ step.title }}
                                    </h5>
                                    <p class="text-xs text-stone-600 leading-relaxed mt-3">
                                        {{ step.detail }}
                                    </p>
                                </div>
                                <div class="mt-4 pt-3 border-t border-stone-100 flex items-center justify-between text-[11px] font-bold text-gold-dark">
                                    <span>Milestone 0{{ loop.index }}</span>
                                    <span>Aurevia Legacy →</span>
                                </div>
                            </div>
                            {% endfor %}
                        </div>

                        <div class="mt-8 pt-6 border-t border-gold/30 flex flex-col sm:flex-row items-center justify-between gap-4">
                            <span class="text-xs text-stone-600 font-semibold">
                                Next Slide: Explore our 3 General Managers executing the Director's vision across Resale, Fresh Projects & Leasing.
                            </span>
                            <button onclick="switchLeadershipSlide(2)"
                                    class="px-6 py-3 rounded-full emerald-btn text-xs font-bold uppercase tracking-wider hover:opacity-95 transition shrink-0">
                                View General Managers Slide (Slide 2) →
                            </button>
                        </div>
                    </div>

                </div>
            </div>

            <!-- SLIDE 2: THREE GENERAL MANAGERS PORTFOLIO -->
            <div id="leadership-slide-2" class="slide-panel hidden">
                <div class="bg-ivory/5 rounded-3xl p-6 sm:p-10 border-2 border-gold/50">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-8 mb-8 border-b border-gold/30 gap-4">
                        <div>
                            <span class="text-xs uppercase tracking-[0.22em] text-gold-light font-extrabold">Slide 02 / 02 — Core Execution Team of Aurevia Realtors</span>
                            <h3 class="font-serif text-3xl sm:text-4xl font-bold text-white mt-1">General Managers Portfolio</h3>
                            <p class="text-xs sm:text-sm text-ivory/75 mt-1">
                                Operating under the supreme leadership of Director Narendar Bhati, our three General Managers spearhead Aurevia Realtors' core operational departments.
                            </p>
                        </div>
                        <button onclick="switchLeadershipSlide(1)"
                                class="self-start sm:self-auto px-4 py-2.5 rounded-full bg-ivory/10 border border-gold/40 text-gold-light text-xs font-bold hover:bg-ivory/20 transition shrink-0">
                            ← Back to Director's Portfolio & Journey
                        </button>
                    </div>

                    <div class="grid lg:grid-cols-3 gap-7">
                        {% for gm in general_managers %}
                        <div class="bg-ivory text-emerald-deep rounded-3xl p-7 border-2 border-gold/60 shadow-2xl flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-5">
                                    <div class="w-14 h-14 rounded-2xl bg-emerald-deep text-gold-light flex items-center justify-center font-serif text-xl font-bold border-2 border-gold">
                                        {{ gm.initials }}
                                    </div>
                                    <span class="text-[10px] font-extrabold uppercase tracking-wider px-3 py-1 rounded-full bg-gold/20 text-emerald-deep border border-gold/40">
                                        {{ gm.badge }}
                                    </span>
                                </div>

                                <h4 class="font-serif text-3xl font-bold text-emerald-deep">{{ gm.name }}</h4>
                                <p class="text-xs font-extrabold text-gold-dark uppercase tracking-wider mt-1">{{ gm.role }}</p>
                                <p class="text-xs font-bold text-emerald-rich mt-1 uppercase tracking-wide">Department: {{ gm.department }}</p>

                                <p class="text-xs text-stone-600 leading-relaxed mt-4 pt-4 border-t border-stone-200">
                                    {{ gm.bio }}
                                </p>

                                <div class="mt-4">
                                    <p class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-deep mb-2">Department Specializations:</p>
                                    <div class="space-y-1.5">
                                        {% for spec in gm.specialties %}
                                        <div class="text-xs bg-white px-3 py-1.5 rounded-xl border border-gold/30 font-medium text-emerald-deep">
                                            • {{ spec }}
                                        </div>
                                        {% endfor %}
                                    </div>
                                </div>
                            </div>

                            <div class="mt-6 pt-5 border-t border-stone-200 space-y-3">
                                <div>
                                    <p class="text-[10px] text-stone-500 uppercase tracking-wider font-bold mb-1.5">Direct Executive Hotline</p>
                                    <a href="tel:{{ gm.phone }}" class="phone-pill text-xs w-full justify-center">
                                        <span class="phone-pill-icon">
                                            <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/></svg>
                                        </span>
                                        <span class="font-mono text-sm">{{ gm.phone_display }}</span>
                                        <span class="live-dot"></span>
                                    </a>
                                </div>
                                <div class="grid grid-cols-2 gap-2.5">
                                    <a href="mailto:{{ gm.email }}?subject=Department%20Inquiry%20for%20{{ gm.name }}%20({{ gm.department }})"
                                       class="py-2.5 rounded-xl bg-white border border-gold text-emerald-deep text-xs font-bold text-center hover:bg-emerald-deep hover:text-gold-light transition">
                                        ✉ Gmail
                                    </a>
                                    <a href="https://wa.me/91{{ gm.phone }}?text=Hello%20{{ gm.name }}%20({{ gm.role }}%20-%20{{ gm.department }}),%20I%20would%20like%20to%20discuss%20a%20property%20requirement%20with%20Aurevia%20Realtors."
                                       target="_blank"
                                       class="py-2.5 rounded-xl gold-btn text-xs font-bold text-center">
                                        WhatsApp GM
                                    </a>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>

            <div class="flex items-center justify-center gap-3 mt-8">
                <button id="dot-1" onclick="switchLeadershipSlide(1)" class="w-10 h-2.5 rounded-full bg-gold transition-all"></button>
                <button id="dot-2" onclick="switchLeadershipSlide(2)" class="w-3 h-2.5 rounded-full bg-ivory/30 hover:bg-ivory/60 transition-all"></button>
            </div>

        </div>
    </section>

    <!-- ========================================================================== -->
    <!-- VERIFIED 20-PROJECT PORTFOLIO WITH UNIT SIZES & INTERIOR FLOOR LAYOUTS     -->
    <!-- ========================================================================== -->
    <section id="portfolio" class="py-16 lg:py-24 bg-ivory">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

            <div class="flex flex-col lg:flex-row lg:items-end justify-between mb-8 gap-6">
                <div>
                    <span class="text-xs uppercase tracking-[0.25em] text-gold-dark font-extrabold">20 Verified Mandates • Unit Sizes & Room-by-Room Interior Layouts</span>
                    <h2 class="font-serif text-3xl sm:text-5xl font-bold text-emerald-deep mt-1">Projects, Unit Sizes & Floor Layouts</h2>
                </div>

                <div class="w-full lg:w-80">
                    <input type="text" id="searchInput" oninput="searchProjects()"
                           placeholder="Search Eldeco, Godrej, Hero, 3 BHK, Sq.Ft..."
                           class="w-full px-4 py-3 rounded-full bg-white border-2 border-gold/40 text-sm focus:outline-none focus:border-emerald-deep shadow-sm">
                </div>
            </div>

            <!-- Filter Row 1: Category Tabs -->
            <div class="flex flex-wrap gap-2 mb-4">
                {% for cat in categories %}
                <button onclick="filterPortfolio('{{ cat }}')"
                        data-cat="{{ cat }}"
                        class="filter-btn text-xs font-bold px-4 py-2.5 rounded-full border transition
                        {% if cat == 'All' %}bg-emerald-deep text-gold-light border-emerald-deep shadow-md{% else %}bg-white text-emerald-deep border-gold/40 hover:border-emerald-deep{% endif %}">
                    {{ cat }}
                </button>
                {% endfor %}
            </div>

            <!-- Filter Row 2: Project Stage & Developer Spotlight Bar -->
            <div class="flex flex-wrap items-center gap-2 mb-10 pb-6 border-b border-gold/30">
                <span class="text-[11px] font-extrabold uppercase tracking-wider text-stone-500 mr-1">Filter by Stage / Builder:</span>
                <button onclick="filterStage('All')" class="stage-btn text-xs font-bold px-3.5 py-1.5 rounded-full bg-ivory-warm text-emerald-deep border border-gold/40 hover:bg-emerald-deep hover:text-gold-light transition">
                    All (20)
                </button>
                <button onclick="filterStage('Ready to Move')" class="stage-btn text-xs font-bold px-3.5 py-1.5 rounded-full bg-white text-emerald-deep border border-gold/40 hover:bg-emerald-deep hover:text-gold-light transition">
                    🟢 Ready to Move In
                </button>
                <button onclick="filterStage('New Launch')" class="stage-btn text-xs font-bold px-3.5 py-1.5 rounded-full bg-white text-emerald-deep border border-gold/40 hover:bg-emerald-deep hover:text-gold-light transition">
                    ✨ New Launch (2026)
                </button>
                <button onclick="filterStage('Under Construction')" class="stage-btn text-xs font-bold px-3.5 py-1.5 rounded-full bg-white text-emerald-deep border border-gold/40 hover:bg-emerald-deep hover:text-gold-light transition">
                    🏗️ Under Construction
                </button>
                <span class="text-stone-300 mx-1">|</span>
                <button onclick="filterDeveloper('Eldeco')" class="text-xs font-extrabold px-3.5 py-1.5 rounded-full bg-gold/20 text-emerald-deep border border-gold hover:bg-emerald-deep hover:text-gold-light transition">
                    Eldeco Group
                </button>
                <button onclick="filterDeveloper('Godrej')" class="text-xs font-extrabold px-3.5 py-1.5 rounded-full bg-gold/20 text-emerald-deep border border-gold hover:bg-emerald-deep hover:text-gold-light transition">
                    Godrej Properties
                </button>
                <button onclick="filterDeveloper('Hero Homes')" class="text-xs font-extrabold px-3.5 py-1.5 rounded-full bg-gold/20 text-emerald-deep border border-gold hover:bg-emerald-deep hover:text-gold-light transition">
                    Hero Homes
                </button>
            </div>

            <!-- Property Cards Grid -->
            <div class="grid md:grid-cols-2 gap-9" id="property-grid">
                {% for prop in properties %}
                <div class="property-card card-luxury rounded-3xl overflow-hidden flex flex-col justify-between"
                     data-category="{{ prop.category }}"
                     data-stage="{{ prop.stage }}"
                     data-developer="{{ prop.developer }}"
                     data-search="{{ prop.title | lower }} {{ prop.location | lower }} {{ prop.category | lower }} {{ prop.developer | lower }} {{ prop.stage | lower }} {{ prop.configs | lower }}">

                    <div>
                        <div class="relative h-72 overflow-hidden">
                            <img src="{{ prop.image }}" alt="{{ prop.title }}" class="w-full h-full object-cover transition duration-700 hover:scale-105">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/35 to-transparent"></div>

                            <span class="absolute top-4 left-4 text-[11px] font-extrabold px-3.5 py-1.5 rounded-full border shadow
                                {% if prop.stage == 'Ready to Move' %}bg-emerald-deep text-gold-light border-gold
                                {% elif prop.stage == 'New Launch' %} gold-btn border-white
                                {% else %}bg-stone-900/90 text-white border-gold/40{% endif %}">
                                {% if prop.stage == 'Ready to Move' %}🟢 READY TO MOVE{% elif prop.stage == 'New Launch' %}✨ NEW LAUNCH{% else %}🏗️ ONGOING{% endif %}
                            </span>

                            <span class="absolute top-4 right-4 bg-ivory/95 text-emerald-deep text-xs font-extrabold px-3.5 py-1.5 rounded-full shadow">
                                {{ prop.rate_per_sqft }}
                            </span>

                            <div class="absolute bottom-4 left-5 right-5 text-white">
                                <div class="flex items-center justify-between gap-2">
                                    <span class="inline-block text-[10px] uppercase tracking-widest px-2.5 py-0.5 rounded bg-gold/30 text-gold-light font-bold">
                                        {{ prop.developer }} • {{ prop.category }}
                                    </span>
                                    <span class="text-[11px] text-white/80 font-medium">{{ prop.rera }}</span>
                                </div>
                                <h3 class="font-serif text-3xl font-bold leading-tight mt-1">{{ prop.title }}</h3>
                                <p class="text-xs text-gold-light font-medium mt-0.5">📍 {{ prop.location }}</p>
                            </div>
                        </div>

                        <div class="p-6 space-y-5">
                            <div class="grid grid-cols-2 gap-3 p-3.5 rounded-2xl bg-ivory border border-gold/40">
                                <div>
                                    <span class="text-[10px] uppercase tracking-wider text-stone-500 font-bold block">Total Ticket Size</span>
                                    <span class="font-serif text-xl font-bold text-emerald-deep">{{ prop.price_range }}</span>
                                </div>
                                <div class="border-l border-gold/30 pl-3">
                                    <span class="text-[10px] uppercase tracking-wider text-stone-500 font-bold block">Official BSP / Rate</span>
                                    <span class="font-serif text-xl font-bold text-gold-dark">{{ prop.rate_per_sqft }}</span>
                                </div>
                            </div>

                            <!-- UNIT CONFIGURATIONS & INTERIOR LAYOUT BREAKDOWN -->
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <p class="text-xs font-extrabold text-emerald-deep uppercase tracking-wider flex items-center gap-1.5">
                                        📐 Unit Sizes & Interior Layout Inside:
                                    </p>
                                    <span class="text-[11px] font-bold text-gold-dark">{{ prop.unit_layouts | length }} Floor Plan Options</span>
                                </div>

                                {% for u in prop.unit_layouts %}
                                <div class="p-3.5 rounded-2xl bg-ivory-warm/70 border border-gold/40 space-y-1.5">
                                    <div class="flex flex-wrap items-center justify-between gap-2">
                                        <span class="text-xs font-extrabold text-emerald-deep">{{ u.unit_type }}</span>
                                        <div class="flex items-center gap-2">
                                            <span class="px-2.5 py-0.5 rounded-md bg-emerald-deep text-gold-light text-[11px] font-bold">
                                                {{ u.size }}
                                            </span>
                                            <span class="text-xs font-extrabold text-gold-dark">{{ u.price }}</span>
                                        </div>
                                    </div>
                                    <p class="text-[11px] text-stone-700 leading-relaxed">
                                        <strong class="text-emerald-rich">Layout Inside:</strong> {{ u.inside_layout }}
                                    </p>
                                </div>
                                {% endfor %}
                            </div>

                            <p class="text-xs text-emerald-rich font-bold">✦ {{ prop.rental_yield }}</p>
                        </div>
                    </div>

                    <!-- Card Footer Actions with Restyled Phone Pill -->
                    <div class="px-6 pb-6 pt-4 border-t border-stone-100 bg-ivory/40">
                        <div class="flex flex-wrap items-center justify-between gap-2 mb-3.5 text-xs">
                            <span class="text-stone-500">Mandate Head: <strong class="text-emerald-deep">{{ prop.contact_person }} ({{ prop.contact_role }})</strong></span>
                            <a href="tel:{{ prop.contact_phone }}" class="phone-pill text-[11px]">
                                <span class="phone-pill-icon">
                                    <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/></svg>
                                </span>
                                <span class="font-mono">{{ prop.contact_phone_styled }}</span>
                            </a>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <button onclick='openModal({{ prop | tojson }})'
                                    class="py-3 px-3 rounded-xl emerald-btn text-xs font-bold hover:opacity-95 transition flex items-center justify-center gap-1.5 shadow">
                                📐 Floor Plans & Blueprint
                            </button>
                            <a href="https://wa.me/91{{ prop.contact_phone }}?text=Hello%20{{ prop.contact_person }},%20please%20share%20the%20PDF%20floor%20plan%20layout%20and%20exact%20cost%20sheet%20for%20{{ prop.title }}%20({{ prop.configs }})."
                               target="_blank"
                               class="py-3 px-3 rounded-xl gold-btn text-xs font-bold text-center flex items-center justify-center">
                                WhatsApp Layout PDF
                            </a>
                        </div>
                    </div>

                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- ========================================================================== -->
    <!-- DEDICATED OFFICIAL GMAIL & ELECTRONIC DOSSIER DESK SECTION                 -->
    <!-- ========================================================================== -->
    <section id="gmail-desk" class="py-16 lg:py-20 bg-emerald-deep text-ivory border-y-2 border-gold relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="bg-gradient-to-br from-emerald-rich to-emerald-deep rounded-3xl p-8 sm:p-12 border-2 border-gold shadow-2xl">
                <div class="grid lg:grid-cols-12 gap-10 items-center">

                    <!-- Left Column: Official Gmail Identity -->
                    <div class="lg:col-span-7 space-y-5">
                        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-gold/20 border border-gold text-gold-light text-xs font-extrabold uppercase tracking-[0.22em]">
                            ✉ Official Corporate Electronic Mail Desk
                        </div>

                        <h2 class="font-serif text-3xl sm:text-5xl font-bold text-white leading-tight">
                            Write to Our Official Gmail Desk
                        </h2>

                        <p class="text-ivory/85 text-sm sm:text-base leading-relaxed">
                            For formal corporate RFPs, NRI portfolio consultations, CAD floor plan dockets, RERA legal verifications, and commercial leasing mandates, connect directly via our official Gmail address:
                        </p>

                        <!-- Big Interactive Gmail Pill Box -->
                        <div class="p-4 sm:p-5 rounded-2xl bg-ivory text-emerald-deep border-2 border-gold flex flex-wrap items-center justify-between gap-4 shadow-xl">
                            <div class="flex items-center gap-3.5">
                                <div class="w-12 h-12 rounded-2xl bg-emerald-deep text-gold-light flex items-center justify-center font-bold text-2xl shrink-0 border border-gold">
                                    ✉
                                </div>
                                <div>
                                    <span class="text-[10px] font-extrabold uppercase tracking-widest text-gold-dark block">Verified Official Gmail ID</span>
                                    <p id="officialGmailText" class="font-mono text-base sm:text-xl font-extrabold text-emerald-deep break-all">
                                        {{ company.email }}
                                    </p>
                                </div>
                            </div>
                            <div class="flex flex-wrap gap-2">
                                <button type="button" onclick="copyGmail()"
                                        id="copyGmailBtn"
                                        class="px-4 py-2.5 rounded-xl bg-emerald-deep text-gold-light text-xs font-bold uppercase tracking-wider hover:opacity-95 transition">
                                    Copy Gmail
                                </button>
                                <a href="https://mail.google.com/mail/?view=cm&fs=1&to={{ company.email }}&su=Property%20Dossier%20%26%20Floor%20Plan%20Inquiry%20—%20Aurevia%20Realtors"
                                   target="_blank"
                                   class="px-4 py-2.5 rounded-xl gold-btn text-xs font-extrabold uppercase tracking-wider">
                                    Compose in Gmail Web ↗
                                </a>
                            </div>
                        </div>

                        <!-- Quick Pre-Filled Gmail Subject Triggers -->
                        <div class="pt-2">
                            <span class="text-[11px] font-extrabold uppercase tracking-widest text-gold-light block mb-2.5">
                                One-Click Department Gmail Templates:
                            </span>
                            <div class="flex flex-wrap gap-2">
                                <a href="mailto:{{ company.email }}?subject=Director%20Desk%20Consultation%20(Mr.%20Narendar%20Bhati)%20—%20Aurevia%20Realtors"
                                   class="text-xs font-bold px-3.5 py-2 rounded-full bg-white/10 border border-gold/40 text-ivory hover:bg-gold hover:text-emerald-deep transition">
                                    👑 Director's Office (Narendar Bhati)
                                </a>
                                <a href="mailto:{{ company.email }}?subject=Resale%20%26%20Plots%20Dossier%20(Attn:%20GM%20Anand%20Basista)"
                                   class="text-xs font-bold px-3.5 py-2 rounded-full bg-white/10 border border-gold/40 text-ivory hover:bg-gold hover:text-emerald-deep transition">
                                    🏢 Resale & Plots (Anand Basista)
                                </a>
                                <a href="mailto:{{ company.email }}?subject=2026%20Fresh%20Project%20Allotment%20(Attn:%20GM%20Himanshu%20Bhutai)"
                                   class="text-xs font-bold px-3.5 py-2 rounded-full bg-white/10 border border-gold/40 text-ivory hover:bg-gold hover:text-emerald-deep transition">
                                    ✨ Fresh Projects (Himanshu Bhutai)
                                </a>
                                <a href="mailto:{{ company.email }}?subject=Corporate%20%26%20Luxury%20Leasing%20Mandate%20(Attn:%20GM%20Apurv%20Mishra)"
                                   class="text-xs font-bold px-3.5 py-2 rounded-full bg-white/10 border border-gold/40 text-ivory hover:bg-gold hover:text-emerald-deep transition">
                                    🔑 Leasing Desk (Apurv Mishra)
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Right Column: Direct Executive Phone & Gmail Directory Card -->
                    <div class="lg:col-span-5">
                        <div class="bg-ivory text-emerald-deep rounded-3xl p-7 border-2 border-gold shadow-xl space-y-3.5">
                            <span class="text-[10px] font-extrabold uppercase tracking-[0.24em] text-gold-dark block">
                                Unified Communication Directory
                            </span>
                            <h3 class="font-serif text-2xl sm:text-3xl font-bold text-emerald-deep">
                                Official Hotlines & Gmail
                            </h3>

                            <div class="space-y-2.5 pt-1">
                                <div class="p-3 rounded-2xl bg-white border gold-border flex items-center justify-between gap-2">
                                    <div>
                                        <span class="text-[9px] font-extrabold uppercase text-gold-dark block">Director of the Company</span>
                                        <p class="font-serif text-lg font-bold text-emerald-deep">{{ director.name }}</p>
                                    </div>
                                    <a href="tel:{{ director.phone }}" class="phone-pill text-xs">
                                        <span class="phone-pill-icon">👑</span>
                                        <span class="font-mono text-[11px]">{{ director.phone_display }}</span>
                                    </a>
                                </div>

                                {% for gm in general_managers %}
                                <div class="p-3 rounded-2xl bg-white border gold-border flex items-center justify-between gap-2">
                                    <div>
                                        <span class="text-[9px] font-extrabold uppercase text-emerald-rich block">GM — {{ gm.department }}</span>
                                        <p class="font-serif text-lg font-bold text-emerald-deep">{{ gm.name }}</p>
                                    </div>
                                    <a href="tel:{{ gm.phone }}" class="phone-pill text-xs">
                                        <span class="phone-pill-icon">📞</span>
                                        <span class="font-mono text-[11px]">{{ gm.phone_display }}</span>
                                    </a>
                                </div>
                                {% endfor %}
                            </div>

                            <div class="p-3.5 rounded-2xl bg-emerald-deep text-ivory border border-gold text-xs space-y-1">
                                <p class="text-gold-light font-bold uppercase tracking-wider">Central Electronic Mail:</p>
                                <p class="font-mono text-sm font-bold">{{ company.email }}</p>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>

    <!-- TRANSPARENT MARKET PRICE MATRIX TABLE -->
    <section id="rate-matrix" class="py-16 bg-ivory-warm border-b gold-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-10">
                <span class="text-xs uppercase tracking-[0.25em] text-gold-dark font-extrabold">Aurevia Realtors 20-Project Rate & Size Benchmark</span>
                <h2 class="font-serif text-3xl sm:text-5xl font-bold text-emerald-deep mt-1">Noida & Greater Noida Official Price & Size Matrix</h2>
            </div>

            <div class="overflow-x-auto bg-white rounded-3xl border-2 border-gold/40 shadow-lg">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-emerald-deep text-gold-light text-xs uppercase tracking-wider">
                            <th class="py-4 px-5">Project Name & Developer</th>
                            <th class="py-4 px-5">Unit Sizes & Configurations</th>
                            <th class="py-4 px-5">Stage</th>
                            <th class="py-4 px-5">Current Rate / BSP</th>
                            <th class="py-4 px-5">Ticket Size / Lease Rate</th>
                            <th class="py-4 px-5 text-right">Blueprint</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-stone-200 text-xs sm:text-sm">
                        {% for prop in properties %}
                        <tr class="hover:bg-ivory transition">
                            <td class="py-4 px-5">
                                <span class="font-serif text-lg font-bold text-emerald-deep block">{{ prop.title }}</span>
                                <span class="text-[11px] text-stone-500 font-semibold">{{ prop.developer }} • {{ prop.location }}</span>
                            </td>
                            <td class="py-4 px-5 text-xs font-semibold text-stone-700">{{ prop.configs }}</td>
                            <td class="py-4 px-5">
                                <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-ivory-warm text-emerald-deep border border-gold/30">
                                    {{ prop.stage }}
                                </span>
                            </td>
                            <td class="py-4 px-5 font-bold text-gold-dark">{{ prop.rate_per_sqft }}</td>
                            <td class="py-4 px-5 font-semibold text-emerald-deep">{{ prop.price_range }}</td>
                            <td class="py-4 px-5 text-right">
                                <button onclick='openModal({{ prop | tojson }})'
                                        class="inline-block px-3.5 py-1.5 rounded-full gold-btn text-xs font-bold">
                                    View Layout →
                                </button>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- PRIVATE CONSULTATION FORM -->
    <section id="contact" class="py-16 lg:py-24 bg-ivory">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="bg-white rounded-3xl p-8 sm:p-12 border-2 border-gold/50 shadow-xl">
                <div class="grid lg:grid-cols-12 gap-10">
                    <div class="lg:col-span-5 space-y-4">
                        <span class="text-xs uppercase tracking-[0.25em] text-gold-dark font-extrabold">Aurevia Realtors Advisory</span>
                        <h2 class="font-serif text-3xl sm:text-4xl font-bold text-emerald-deep">Request Floor Plan PDF & Official Cost Sheet</h2>
                        <p class="text-xs sm:text-sm text-stone-600 leading-relaxed">
                            Submit your requirement to receive CAD/PDF architectural floor plans, unit availability, and payment plans from the Director's Office or our Department General Managers.
                        </p>
                        <div class="p-4 rounded-2xl bg-ivory border gold-border text-xs space-y-3">
                            <p><strong class="text-emerald-deep">Aurevia Realtors HQ:</strong><br/>{{ company.address }}</p>
                            <p><strong class="text-emerald-deep">Official Gmail:</strong><br/>
                                <a href="mailto:{{ company.email }}" class="font-mono font-bold text-gold-dark hover:underline">✉ {{ company.email }}</a>
                            </p>
                            <div class="pt-2 border-t border-gold/30 space-y-1.5">
                                <span class="text-[10px] font-extrabold uppercase tracking-wider text-gold-dark block">Supreme Authority</span>
                                <p class="font-bold text-emerald-deep">{{ director.name }} (Director)</p>
                                <a href="tel:{{ director.phone }}" class="phone-pill text-[11px]">
                                    <span class="phone-pill-icon">📞</span>
                                    <span class="font-mono">{{ director.phone_display }}</span>
                                </a>
                            </div>
                            <div class="pt-2 border-t border-gold/30 space-y-2">
                                <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-rich block">General Managers Team</span>
                                {% for gm in general_managers %}
                                <div>
                                    <p class="font-bold text-emerald-deep mb-1">{{ gm.name }} (GM — {{ gm.department }})</p>
                                    <a href="tel:{{ gm.phone }}" class="phone-pill text-[11px]">
                                        <span class="phone-pill-icon">📞</span>
                                        <span class="font-mono">{{ gm.phone_display }}</span>
                                    </a>
                                </div>
                                {% endfor %}
                            </div>
                        </div>
                    </div>

                    <div class="lg:col-span-7">
                        <form id="leadForm" onsubmit="submitLead(event)" class="space-y-4">
                            <div class="grid sm:grid-cols-2 gap-4">
                                <input type="text" name="name" required placeholder="Full Name *"
                                       class="w-full px-4 py-3.5 rounded-xl bg-ivory border border-gold/40 text-sm focus:outline-none focus:border-emerald-deep">
                                <input type="tel" name="phone" required placeholder="Mobile / WhatsApp Number *"
                                       class="w-full px-4 py-3.5 rounded-xl bg-ivory border border-gold/40 text-sm focus:outline-none focus:border-emerald-deep">
                            </div>
                            <div class="grid sm:grid-cols-2 gap-4">
                                <select name="segment" class="w-full px-4 py-3.5 rounded-xl bg-ivory border border-gold/40 text-sm">
                                    {% for prop in properties %}
                                    <option value="{{ prop.title }} ({{ prop.configs }})">[{{ prop.stage }}] {{ prop.title }} — {{ prop.rate_per_sqft }}</option>
                                    {% endfor %}
                                </select>
                                <select name="specialist" class="w-full px-4 py-3.5 rounded-xl bg-ivory border border-gold/40 text-sm">
                                    <option value="Director Office — Narendar Bhati">👑 Director's Office — Narendar Bhati</option>
                                    <option value="GM Team — Himanshu Bhutai (Fresh Project)">GM — Himanshu Bhutai (Fresh Project)</option>
                                    <option value="GM Team — Anand Basista (Resale & Fresh)">GM — Anand Basista (Resale & Fresh Project)</option>
                                    <option value="GM Team — Apurv Mishra (Leasing)">GM — Apurv Mishra (Leasing Department)</option>
                                </select>
                            </div>
                            <textarea name="message" rows="3" placeholder="Specify preferred unit size (e.g., 3 BHK 1,825 Sq.Ft. or 4 BHK 2,850 Sq.Ft.), floor preference, or site visit date..."
                                      class="w-full px-4 py-3.5 rounded-xl bg-ivory border border-gold/40 text-sm"></textarea>
                            <button type="submit" class="w-full py-4 rounded-xl gold-btn font-bold text-sm uppercase tracking-wider">
                                Request Floor Plans & Verified Cost Sheet
                            </button>
                            <div id="formStatus" class="hidden text-center p-3.5 rounded-xl text-xs font-semibold"></div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ========================================================================== -->
    <!-- INTERACTIVE ARCHITECTURAL FLOOR PLAN & UNIT BLUEPRINT MODAL                -->
    <!-- ========================================================================== -->
    <div id="projectModal" class="fixed inset-0 z-50 hidden bg-black/75 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6">
        <div class="bg-ivory rounded-3xl max-w-4xl w-full p-6 sm:p-8 border-2 border-gold shadow-2xl relative max-h-[92vh] overflow-y-auto">
            <button onclick="closeModal()" class="absolute top-5 right-5 w-10 h-10 rounded-full bg-emerald-deep text-gold-light font-bold text-xl hover:scale-105 transition">&times;</button>

            <span id="modalCategory" class="text-xs font-extrabold uppercase tracking-widest text-gold-dark"></span>
            <h3 id="modalTitle" class="font-serif text-3xl sm:text-4xl font-bold text-emerald-deep mt-1"></h3>
            <p id="modalLocation" class="text-xs text-stone-600 font-semibold mt-0.5"></p>

            <div class="grid sm:grid-cols-3 gap-4 my-5 p-4 rounded-2xl bg-white border gold-border">
                <div>
                    <span class="text-[10px] uppercase tracking-wider text-stone-500 font-bold block">Official Market Rate / BSP</span>
                    <p id="modalRate" class="font-serif text-2xl font-bold text-gold-dark"></p>
                </div>
                <div>
                    <span class="text-[10px] uppercase tracking-wider text-stone-500 font-bold block">Total Ticket Size</span>
                    <p id="modalPrice" class="font-serif text-2xl font-bold text-emerald-deep"></p>
                </div>
                <div>
                    <span class="text-[10px] uppercase tracking-wider text-stone-500 font-bold block">RERA & Possession Status</span>
                    <p id="modalRera" class="text-xs font-bold text-emerald-rich mt-1"></p>
                </div>
            </div>

            <div class="mb-4">
                <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-deep block mb-2">
                    Select Unit Size to Inspect Architectural Floor Plan & Room Dimensions:
                </span>
                <div id="modalUnitTabs" class="flex flex-wrap gap-2"></div>
            </div>

            <div class="blueprint-grid rounded-3xl p-6 text-ivory border-2 border-gold shadow-xl space-y-5">
                <div class="flex flex-wrap items-center justify-between gap-2 border-b border-gold/30 pb-4">
                    <div>
                        <span class="text-[10px] uppercase tracking-[0.22em] text-gold-light font-bold block">Aurevia CAD Floor Plan Schematic</span>
                        <h4 id="blueprintUnitTitle" class="font-serif text-2xl sm:text-3xl font-bold text-white"></h4>
                    </div>
                    <div class="text-right">
                        <span id="blueprintUnitSize" class="inline-block px-3.5 py-1 rounded-full bg-gold text-emerald-deep text-xs font-extrabold"></span>
                        <p id="blueprintUnitPrice" class="font-serif text-xl font-bold text-gold-light mt-1"></p>
                    </div>
                </div>

                <p id="blueprintInsideText" class="text-xs sm:text-sm text-ivory/90 leading-relaxed bg-white/5 p-3.5 rounded-xl border border-gold/30"></p>

                <div>
                    <span class="text-[10px] uppercase tracking-[0.2em] text-gold-light font-bold block mb-2.5">
                        Room-by-Room Interior Dimensions & Zoning Blueprint:
                    </span>
                    <div id="blueprintRoomsGrid" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-3"></div>
                </div>
            </div>

            <div class="mt-6 pt-4 border-t border-gold/40 flex flex-col sm:flex-row items-center justify-between gap-4">
                <span id="modalSpecialist" class="text-xs font-bold text-emerald-deep"></span>
                <div class="flex flex-wrap gap-2.5 w-full sm:w-auto">
                    <a id="modalGmail" href="#" class="flex-1 sm:flex-initial px-5 py-3.5 rounded-xl emerald-btn text-xs font-bold text-center uppercase">
                        ✉ Request via Gmail
                    </a>
                    <a id="modalWhatsapp" href="#" target="_blank" class="flex-1 sm:flex-initial px-6 py-3.5 rounded-xl gold-btn text-xs font-bold text-center uppercase">
                        WhatsApp Layout PDF
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="bg-emerald-deep text-ivory border-t border-gold/40 py-12 text-center text-xs space-y-4">
        <div>
            <p class="font-serif text-3xl gold-text font-bold">{{ company.name }} — {{ company.tagline }}</p>
            <p class="text-ivory/80 mt-1">{{ company.address }}</p>
            <p class="mt-2">
                <a href="mailto:{{ company.email }}" class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 border border-gold/40 text-gold-light font-mono font-bold hover:bg-gold hover:text-emerald-deep transition">
                    ✉ {{ company.email }}
                </a>
            </p>
        </div>

        <div class="flex flex-wrap items-center justify-center gap-3 pt-2">
            <a href="tel:{{ director.phone }}" class="phone-pill text-xs">
                <span class="phone-pill-icon">👑</span>
                <span>Director ({{ director.name }}):</span>
                <span class="font-mono text-gold-light">{{ director.phone_display }}</span>
            </a>
            {% for gm in general_managers %}
            <a href="tel:{{ gm.phone }}" class="phone-pill text-xs">
                <span class="phone-pill-icon">📞</span>
                <span>{{ gm.name }} ({{ gm.department }}):</span>
                <span class="font-mono text-gold-light">{{ gm.phone_display }}</span>
            </a>
            {% endfor %}
        </div>
    </footer>

    <script>
        let currentModalProp = null;

        function copyGmail() {
            navigator.clipboard.writeText("{{ company.email }}");
            const btn = document.getElementById('copyGmailBtn');
            btn.innerText = "✓ Copied Gmail!";
            setTimeout(() => { btn.innerText = "Copy Gmail"; }, 2500);
        }

        function switchLeadershipSlide(slideNumber) {
            const slide1 = document.getElementById('leadership-slide-1');
            const slide2 = document.getElementById('leadership-slide-2');
            const tab1 = document.getElementById('tab-slide-1');
            const tab2 = document.getElementById('tab-slide-2');
            const dot1 = document.getElementById('dot-1');
            const dot2 = document.getElementById('dot-2');

            if (slideNumber === 1) {
                slide1.classList.remove('hidden');
                slide2.classList.add('hidden');
                tab1.className = "px-5 py-2.5 rounded-full text-xs font-extrabold uppercase tracking-wider transition gold-btn";
                tab2.className = "px-5 py-2.5 rounded-full text-xs font-extrabold uppercase tracking-wider transition text-ivory/80 hover:text-white";
                dot1.className = "w-10 h-2.5 rounded-full bg-gold transition-all";
                dot2.className = "w-3 h-2.5 rounded-full bg-ivory/30 hover:bg-ivory/60 transition-all";
            } else {
                slide1.classList.add('hidden');
                slide2.classList.remove('hidden');
                tab2.className = "px-5 py-2.5 rounded-full text-xs font-extrabold uppercase tracking-wider transition gold-btn";
                tab1.className = "px-5 py-2.5 rounded-full text-xs font-extrabold uppercase tracking-wider transition text-ivory/80 hover:text-white";
                dot2.className = "w-10 h-2.5 rounded-full bg-gold transition-all";
                dot1.className = "w-3 h-2.5 rounded-full bg-ivory/30 hover:bg-ivory/60 transition-all";
            }
        }

        function filterPortfolio(category) {
            document.querySelectorAll('.filter-btn').forEach(btn => {
                if (btn.dataset.cat === category) {
                    btn.className = "filter-btn text-xs font-bold px-4 py-2.5 rounded-full border transition bg-emerald-deep text-gold-light border-emerald-deep shadow-md";
                } else {
                    btn.className = "filter-btn text-xs font-bold px-4 py-2.5 rounded-full border transition bg-white text-emerald-deep border-gold/40 hover:border-emerald-deep";
                }
            });
            document.querySelectorAll('.property-card').forEach(card => {
                card.style.display = (category === 'All' || card.dataset.category === category) ? 'flex' : 'none';
            });
        }

        function filterStage(stage) {
            document.querySelectorAll('.property-card').forEach(card => {
                card.style.display = (stage === 'All' || card.dataset.stage === stage) ? 'flex' : 'none';
            });
        }

        function filterDeveloper(devName) {
            document.querySelectorAll('.property-card').forEach(card => {
                card.style.display = card.dataset.developer.toLowerCase().includes(devName.toLowerCase()) ? 'flex' : 'none';
            });
        }

        function searchProjects() {
            const q = document.getElementById('searchInput').value.toLowerCase();
            document.querySelectorAll('.property-card').forEach(card => {
                card.style.display = card.dataset.search.includes(q) ? 'flex' : 'none';
            });
        }

        function renderUnitBlueprint(unitIndex) {
            if (!currentModalProp || !currentModalProp.unit_layouts) return;
            const unit = currentModalProp.unit_layouts[unitIndex];

            document.querySelectorAll('.unit-tab-btn').forEach((btn, idx) => {
                if (idx === unitIndex) {
                    btn.className = "unit-tab-btn px-4 py-2 rounded-xl text-xs font-extrabold bg-emerald-deep text-gold-light border-2 border-gold shadow";
                } else {
                    btn.className = "unit-tab-btn px-4 py-2 rounded-xl text-xs font-bold bg-white text-emerald-deep border border-gold/40 hover:border-emerald-deep";
                }
            });

            document.getElementById('blueprintUnitTitle').innerText = unit.unit_type;
            document.getElementById('blueprintUnitSize').innerText = unit.size;
            document.getElementById('blueprintUnitPrice').innerText = unit.price;
            document.getElementById('blueprintInsideText').innerHTML = "<strong>Interior Layout Breakdown:</strong> " + unit.inside_layout;

            const grid = document.getElementById('blueprintRoomsGrid');
            grid.innerHTML = "";
            unit.rooms_blueprint.forEach(room => {
                const box = document.createElement('div');
                box.className = "p-3.5 rounded-2xl bg-emerald-rich/90 border border-gold/50 flex flex-col justify-between";
                box.innerHTML = `
                    <div class="flex items-center justify-between">
                        <span class="text-[10px] uppercase tracking-widest px-2 py-0.5 rounded bg-gold/20 text-gold-light font-bold">${room.zone} Zone</span>
                        <span class="text-[10px] text-ivory/60">CAD Scaled</span>
                    </div>
                    <p class="font-serif text-lg font-bold text-white mt-2">${room.name}</p>
                    <p class="text-xs font-extrabold text-gold-light mt-1">📐 ${room.dim}</p>
                `;
                grid.appendChild(box);
            });
        }

        function openModal(prop) {
            currentModalProp = prop;
            document.getElementById('modalCategory').innerText = prop.stage + " • " + prop.category + " • " + prop.developer;
            document.getElementById('modalTitle').innerText = prop.title;
            document.getElementById('modalLocation').innerText = "📍 " + prop.location;
            document.getElementById('modalRate').innerText = prop.rate_per_sqft;
            document.getElementById('modalPrice').innerText = prop.price_range;
            document.getElementById('modalRera').innerText = prop.rera + " • " + prop.status;
            document.getElementById('modalSpecialist').innerText = "Mandate Head: " + prop.contact_person + " (" + prop.contact_phone_styled + ")";
            document.getElementById('modalWhatsapp').href = "https://wa.me/91" + prop.contact_phone + "?text=Hello%20" + encodeURIComponent(prop.contact_person) + ",%20please%20share%20the%20official%20floor%20plan%20PDF%20and%20cost%20sheet%20for%20" + encodeURIComponent(prop.title);
            document.getElementById('modalGmail').href = "mailto:{{ company.email }}?subject=" + encodeURIComponent("Floor Plan & Cost Sheet Request: " + prop.title) + "&body=" + encodeURIComponent("Hello Aurevia Realtors Team,\n\nPlease share the CAD floor plans and official price sheet for " + prop.title + " (" + prop.location + ").\n\nMy Name:\nMy Phone Number:");

            const tabsContainer = document.getElementById('modalUnitTabs');
            tabsContainer.innerHTML = "";
            if (prop.unit_layouts && prop.unit_layouts.length > 0) {
                prop.unit_layouts.forEach((u, idx) => {
                    const btn = document.createElement('button');
                    btn.type = "button";
                    btn.innerText = u.unit_type + " (" + u.size.split('(')[0].trim() + ")";
                    btn.onclick = () => renderUnitBlueprint(idx);
                    tabsContainer.appendChild(btn);
                });
                renderUnitBlueprint(0);
            }

            document.getElementById('projectModal').classList.remove('hidden');
        }

        function closeModal() {
            document.getElementById('projectModal').classList.add('hidden');
        }

        async function submitLead(e) {
            e.preventDefault();
            const f = e.target;
            const res = await fetch('/api/inquiry', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    name: f.name.value, phone: f.phone.value,
                    segment: f.segment.value, specialist: f.specialist.value, message: f.message.value
                })
            });
            const data = await res.json();
            const box = document.getElementById('formStatus');
            box.className = "text-center p-3.5 rounded-xl text-xs font-bold bg-emerald-deep text-gold-light";
            box.innerText = data.message;
            f.reset();
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML_TEMPLATE,
        company=COMPANY_INFO,
        manifesto=AUREVIA_MANIFESTO,
        categories=CATEGORIES,
        director=DIRECTOR,
        general_managers=GENERAL_MANAGERS,
        properties=PROPERTIES
    )

@app.route("/logo.jpeg")
def serve_logo():
    if os.path.exists("logo.jpeg"):
        return send_from_directory(".", "logo.jpeg")
    return ("Logo not found", 404)

@app.route("/api/inquiry", methods=["POST"])
def save_inquiry():
    data = request.get_json()
    lead = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": data.get("name"),
        "phone": data.get("phone"),
        "segment": data.get("segment"),
        "specialist": data.get("specialist"),
        "message": data.get("message")
    }
    leads = []
    if os.path.exists("leads.json"):
        try:
            with open("leads.json", "r") as f:
                leads = json.load(f)
        except Exception:
            leads = []
    leads.append(lead)
    with open("leads.json", "w") as f:
        json.dump(leads, f, indent=4)
    return jsonify({
        "status": "success",
        "message": f"Thank you {lead['name']}! Your floor plan & cost sheet request has been logged and assigned to {lead['specialist']} (Official Gmail: aureviarealtors@gmail.com)."
    })

@app.route("/admin")
def view_leads():
    if request.args.get("key") != "aurevia2026":
        return "Unauthorized. Append ?key=aurevia2026 to URL.", 403
    if not os.path.exists("leads.json"):
        return jsonify([])
    with open("leads.json", "r") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"\n✨ Aurevia Realtors Portal (Director + 3 GMs) is LIVE at: http://127.0.0.1:{port}\n")
    app.run(host="0.0.0.0", port=port, debug=True)