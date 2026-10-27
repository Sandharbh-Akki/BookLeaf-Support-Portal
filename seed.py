import json
import os

DATA_FILE = "db.json"

RAW_DATA = {
    "authors": [
        {
            "author_id": "AUTH001", "name": "Priya Sharma", "email": "priya.sharma@email.com",
            "books": [
                { "book_id": "BK001", "title": "Whispers of the Ganges", "isbn": "978-93-5XXXX-01-1", "genre": "Literary Fiction", "status": "Published & Live", "mrp": 399, "total_copies_sold": 342, "total_royalty_earned": 11970, "royalty_paid": 8400, "royalty_pending": 3570 },
                { "book_id": "BK002", "title": "The Saffron Diaries", "isbn": "978-93-5XXXX-02-8", "genre": "Non-Fiction / Memoir", "status": "Published & Live", "mrp": 450, "total_copies_sold": 189, "total_royalty_earned": 7938, "royalty_paid": 7938, "royalty_pending": 0 }
            ]
        },
        {
            "author_id": "AUTH002", "name": "Rohit Kapoor", "email": "rohit.kapoor@email.com",
            "books": [
                { "book_id": "BK003", "title": "Code & Karma", "isbn": "978-93-5XXXX-03-5", "genre": "Self-Help / Technology", "status": "Published & Live", "mrp": 350, "total_copies_sold": 876, "total_royalty_earned": 26280, "royalty_paid": 21000, "royalty_pending": 5280 },
                { "book_id": "BK004", "title": "Startup Sutra", "isbn": "978-93-5XXXX-04-2", "genre": "Business / Entrepreneurship", "status": "Published & Live", "mrp": 499, "total_copies_sold": 1203, "total_royalty_earned": 57744, "royalty_paid": 50000, "royalty_pending": 7744 }
            ]
        },
        {
            "author_id": "AUTH003", "name": "Ananya Reddy", "email": "ananya.reddy@email.com",
            "books": [
                { "book_id": "BK005", "title": "Between Two Temples", "isbn": "978-93-5XXXX-05-9", "genre": "Historical Fiction", "status": "Published & Live", "mrp": 425, "total_copies_sold": 67, "total_royalty_earned": 2546, "royalty_paid": 0, "royalty_pending": 2546 }
            ]
        }
    ]
}

def init_db():
    if not os.path.exists(DATA_FILE):
        data = RAW_DATA
        data["tickets"] = []
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

def get_db():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
      
