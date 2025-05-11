import random
from Core.DatabaseOperation.Event import register_event_function


sample_users = [
    {"username": "jdoe", "first_name": "John", "last_name": "Doe", "email": ""},
    {"username": "asmith", "first_name": "Alice", "last_name": "Smith", "email": ""},
    {"username": "bwayne", "first_name": "Bruce", "last_name": "Wayne", "email": ""},
    {"username": "ckent", "first_name": "Clark", "last_name": "Kent", "email": ""},
    {"username": "dparker", "first_name": "Peter", "last_name": "Parker", "email": ""},
    {"username": "elane", "first_name": "Elaine", "last_name": "Benes", "email": ""},
    {"username": "rgranger", "first_name": "Ron", "last_name": "Granger", "email": ""},
    {"username": "hpotter", "first_name": "Harry", "last_name": "Potter", "email": ""},
    {"username": "hduke", "first_name": "Hazel", "last_name": "Duke", "email": ""},
    {"username": "mscott", "first_name": "Michael", "last_name": "Scott", "email": ""},
    {
        "username": "pschmidt",
        "first_name": "Paula",
        "last_name": "Schmidt",
        "email": "",
    },
    {"username": "kchan", "first_name": "Kevin", "last_name": "Chan", "email": ""},
    {"username": "njohnson", "first_name": "Nina", "last_name": "Johnson", "email": ""},
    {"username": "dluna", "first_name": "Diego", "last_name": "Luna", "email": ""},
    {"username": "sblack", "first_name": "Sarah", "last_name": "Black", "email": ""},
    {"username": "tlee", "first_name": "Tom", "last_name": "Lee", "email": ""},
    {"username": "lchen", "first_name": "Lucy", "last_name": "Chen", "email": ""},
    {
        "username": "ewilliams",
        "first_name": "Ethan",
        "last_name": "Williams",
        "email": "",
    },
    {"username": "rpatel", "first_name": "Riya", "last_name": "Patel", "email": ""},
    {"username": "omurphy", "first_name": "Owen", "last_name": "Murphy", "email": ""},
]

sample_entities = [
    {
        "entity_name": "Inception",
        "entity_type": "Movie",
        "description": "A mind-bending thriller by Christopher Nolan.",
    },
    {
        "entity_name": "The Matrix",
        "entity_type": "Movie",
        "description": "A sci-fi action film about reality and machines.",
    },
    {
        "entity_name": "Interstellar",
        "entity_type": "Movie",
        "description": "Explores space, time, and love.",
    },
    {
        "entity_name": "Parasite",
        "entity_type": "Movie",
        "description": "A Korean film exploring class differences.",
    },
    {
        "entity_name": "The Godfather",
        "entity_type": "Movie",
        "description": "A mafia saga centered on family and power.",
    },
    {
        "entity_name": "Pulp Fiction",
        "entity_type": "Movie",
        "description": "A nonlinear crime drama.",
    },
    {
        "entity_name": "Spirited Away",
        "entity_type": "Movie",
        "description": "A fantasy anime about a girl in a spirit world.",
    },
    {
        "entity_name": "The Dark Knight",
        "entity_type": "Movie",
        "description": "Batman faces the Joker in a dark Gotham.",
    },
    {
        "entity_name": "1984",
        "entity_type": "Book",
        "description": "A dystopian novel by George Orwell.",
    },
    {
        "entity_name": "Brave New World",
        "entity_type": "Book",
        "description": "A futuristic society shaped by conditioning.",
    },
    {
        "entity_name": "Sapiens",
        "entity_type": "Book",
        "description": "A brief history of humankind by Yuval Noah Harari.",
    },
    {
        "entity_name": "To Kill a Mockingbird",
        "entity_type": "Book",
        "description": "Explores racism in the Deep South.",
    },
    {
        "entity_name": "The Catcher in the Rye",
        "entity_type": "Book",
        "description": "A story of teenage alienation.",
    },
    {
        "entity_name": "The Great Gatsby",
        "entity_type": "Book",
        "description": "The American dream and social decay.",
    },
    {
        "entity_name": "The Hobbit",
        "entity_type": "Book",
        "description": "Bilbos unexpected journey in Middle-earth.",
    },
    {
        "entity_name": "Alan Turing",
        "entity_type": "Person",
        "description": "Pioneer of computer science and cryptography.",
    },
    {
        "entity_name": "Marie Curie",
        "entity_type": "Person",
        "description": "Physicist and chemist who discovered radium.",
    },
    {
        "entity_name": "Ada Lovelace",
        "entity_type": "Person",
        "description": "First computer programmer.",
    },
    {
        "entity_name": "Nelson Mandela",
        "entity_type": "Person",
        "description": "Anti-apartheid revolutionary and leader.",
    },
    {
        "entity_name": "Elon Musk",
        "entity_type": "Person",
        "description": "Entrepreneur in tech and space.",
    },
    {
        "entity_name": "Greta Thunberg",
        "entity_type": "Person",
        "description": "Climate activist from Sweden.",
    },
    {
        "entity_name": "Frida Kahlo",
        "entity_type": "Person",
        "description": "Mexican artist known for self-portraits.",
    },
    {
        "entity_name": "Steve Jobs",
        "entity_type": "Person",
        "description": "Co-founder of Apple Inc.",
    },
    {
        "entity_name": "iPhone 13",
        "entity_type": "Product",
        "description": "Smartphone by Apple with A15 Bionic chip.",
    },
    {
        "entity_name": "Tesla Model 3",
        "entity_type": "Product",
        "description": "Electric sedan with autopilot features.",
    },
    {
        "entity_name": "PlayStation 5",
        "entity_type": "Product",
        "description": "Sonys latest gaming console.",
    },
    {
        "entity_name": "MacBook Pro",
        "entity_type": "Product",
        "description": "High-performance laptop by Apple.",
    },
    {
        "entity_name": "Kindle Paperwhite",
        "entity_type": "Product",
        "description": "E-reader by Amazon with backlight.",
    },
    {
        "entity_name": "Samsung Galaxy S22",
        "entity_type": "Product",
        "description": "Flagship Android smartphone.",
    },
    {
        "entity_name": "Nvidia RTX 3080",
        "entity_type": "Product",
        "description": "Powerful graphics card for gaming.",
    },
    {
        "entity_name": "GoPro Hero 10",
        "entity_type": "Product",
        "description": "Action camera for adventure.",
    },
    {
        "entity_name": "Python Basics",
        "entity_type": "Course",
        "description": "An introductory course to Python programming.",
    },
    {
        "entity_name": "Machine Learning 101",
        "entity_type": "Course",
        "description": "Learn the basics of ML algorithms.",
    },
    {
        "entity_name": "Web Development Bootcamp",
        "entity_type": "Course",
        "description": "HTML, CSS, JS in one package.",
    },
    {
        "entity_name": "Data Structures",
        "entity_type": "Course",
        "description": "Learn about trees, graphs, and more.",
    },
    {
        "entity_name": "Intro to Cloud Computing",
        "entity_type": "Course",
        "description": "Basics of AWS, Azure, and GCP.",
    },
    {
        "entity_name": "React for Beginners",
        "entity_type": "Course",
        "description": "Start building front-end apps.",
    },
    {
        "entity_name": "Cybersecurity Essentials",
        "entity_type": "Course",
        "description": "How to secure systems and networks.",
    },
    {
        "entity_name": "New York",
        "entity_type": "City",
        "description": "A bustling metropolis in the USA.",
    },
    {
        "entity_name": "Tokyo",
        "entity_type": "City",
        "description": "A tech-forward city in Japan.",
    },
    {
        "entity_name": "Paris",
        "entity_type": "City",
        "description": "Known for its culture, art, and fashion.",
    },
    {
        "entity_name": "Cairo",
        "entity_type": "City",
        "description": "Home to the ancient pyramids of Egypt.",
    },
    {
        "entity_name": "Sydney",
        "entity_type": "City",
        "description": "Australian city known for its harbor.",
    },
    {
        "entity_name": "Toronto",
        "entity_type": "City",
        "description": "Canada’s most multicultural city.",
    },
    {
        "entity_name": "Rio de Janeiro",
        "entity_type": "City",
        "description": "Famous for beaches and Carnival.",
    },
    {
        "entity_name": "Google",
        "entity_type": "Company",
        "description": "Tech giant known for search and Android.",
    },
    {
        "entity_name": "Microsoft",
        "entity_type": "Company",
        "description": "Makers of Windows and Azure.",
    },
    {
        "entity_name": "Amazon",
        "entity_type": "Company",
        "description": "E-commerce leader and cloud provider.",
    },
    {
        "entity_name": "Netflix",
        "entity_type": "Company",
        "description": "Streaming platform for movies and shows.",
    },
    {
        "entity_name": "Tesla",
        "entity_type": "Company",
        "description": "Electric vehicles and clean energy.",
    },
    {
        "entity_name": "SpaceX",
        "entity_type": "Company",
        "description": "Aerospace company building rockets.",
    },
    {
        "entity_name": "Apple",
        "entity_type": "Company",
        "description": "Makers of iPhones, Macs, and more.",
    },
]


EVENT_TYPES = ["liked", "viewed", "disliked", "followed", "loved"]


def generate_sample_events(user_list, entity_list, num_events=150):
    """
    Randomly creates event interactions between users and entities.
    """
    for _ in range(num_events):
        user = random.choice(user_list)
        entity = random.choice(entity_list)
        event_type = random.choice(EVENT_TYPES)

        username = user["username"]
        entity_name = entity["entity_name"]
        entity_type = entity["entity_type"]

        try:
            register_event_function(
                username=username,
                event_type=event_type,
                entity_name=entity_name,
                entity_type=entity_type,
            )
        except Exception as e:
            print(
                f"Failed to register event for {username} -> {entity_name} ({event_type}): {e}"
            )
