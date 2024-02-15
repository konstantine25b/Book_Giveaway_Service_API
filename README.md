# Book Giveaway Service API

## Objective
The Book Giveaway Service API aims to provide a platform where users can offer books for free and take books offered by others. It includes user registration, book management, and supporting resources such as authors, genres, and book conditions.

## Core Features
1. **User Authentication:**
   - Registration with email.
   
2. **Books Management:**
   - CRUD operations on books.
   - Filtering books based on various parameters like author, genre, etc.
   
3. **Supporting Resources:**
   - Management of authors, genres, conditions, images, or posters.
   
4. **Book Retrieval Information:**
   - Location information for picking up books.
   
5. **Ownership Decision:**
   - Owners can choose the recipient if multiple users are interested in a book.
   
6. **User Roles and Permissions:**
   - Different roles for users (Admin, User, Guest) with distinct permissions for each role.
   
7. **Search and Filtering:**
   - Enhanced search functionality with full-text search capabilities and advanced filters (e.g., publication year, language, user ratings).

## Tech Stack
- Python with Django Rest Framework
- PostgreSQL as the database
- RESTful API
- Git
- Swagger for API Documentation (optional)
- Docker & Docker Compose (optional)

## Installation
1. Clone the repository:
git clone https://github.com/konstantine25b/Book_Giveaway_Service_API
cd book_giveaway_service

2. Set up the environment:
- If using a virtual environment:
  ```
  python3 -m venv env
  source env/bin/activate
3. Install dependencies:
pip install -r requirements.txt

4. Apply database migrations
python manage.py migrate

## API Documentation
- API documentation is available using Swagger. Run the server and navigate to http://localhost:8000/swagger/ to explore the API endpoints.
