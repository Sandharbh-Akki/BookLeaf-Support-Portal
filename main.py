from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import json
import uuid
from seed import init_db, get_db, save_db

app = FastAPI()
templates = Jinja2Templates(directory="templates")

init_db()

@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def handle_login(email: str = Form(...)):
    db = get_db()
    author = next((a for a in db["authors"] if a["email"] == email), None)
    if email == "admin@bookleaf.com":
        return RedirectResponse(url="/admin", status_code=303)
    elif author:
        return RedirectResponse(url=f"/author/{author['author_id']}", status_code=303)
    else:
        raise HTTPException(status_code=400, detail="User not found")

@app.get("/author/{author_id}", response_class=HTMLResponse)
def author_dashboard(request: Request, author_id: str):
    db = get_db()
    author = next((a for a in db["authors"] if a["author_id"] == author_id), None)
    my_tickets = [t for t in db["tickets"] if t["authorId"] == author_id]
    return templates.TemplateResponse("author.html", {"request": request, "author": author, "tickets": my_tickets})

@app.post("/author/{author_id}/ticket")
def create_ticket(author_id: str, subject: str = Form(...), query: str = Form(...)):
    db = get_db()
    
    category = "General Inquiry"
    priority = "Medium"
    if "royalty" in query.lower() or "payment" in query.lower():
        category = "Royalty & Payments"
        priority = "High"
    elif "isbn" in query.lower():
        category = "ISBN & Metadata"
        priority = "Critical"
        
    ai_response = f"Thank you for reaching out. We have logged your query regarding {category}. Our editorial desk will investigate this matter within 48 business hours."

    new_ticket = {
        "id": str(uuid.uuid4())[:8],
        "authorId": author_id,
        "subject": subject,
        "query": query,
        "category": category,
        "priority": priority,
        "status": "Open",
        "aiDraftResponse": ai_response
    }
    db["tickets"].append(new_ticket)
    save_db(db)
    return RedirectResponse(url=f"/author/{author_id}", status_code=303)

@app.get("/admin", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    db = get_db()
    return templates.TemplateResponse("admin.html", {"request": request, "tickets": db["tickets"]})
  
