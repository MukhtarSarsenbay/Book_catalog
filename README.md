# Book Catalog API

## Description

The Book Catalog API is a backend project aimed at managing a catalog of books with functionalities to add reviews and mark books as favorites. The API is built using Django and Django REST Framework (DRF) and uses Docker for containerization. It includes a simple HTML frontend to display book details and allows content management through the Django admin page.

## Stack

- Python
- Django REST Framework (DRF)
- PostgreSQL (for production, SQLite for development)
- Docker
- Postman (for API testing)

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.12

## Installation

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements_dev.txt
    ```

4. **Build and run Docker containers:**
    ```sh
    docker-compose up --build
    ```

5. **Run database migrations:**
    ```sh
    docker-compose exec web python manage.py migrate
    ```

6. **Create a superuser to access the admin page:**
    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

## Usage

- **Access the admin page:** 
    - URL: `http://0.0.0.0:8000/admin`
    - Use the superuser credentials to log in.
- **Access the API documentation (if using Swagger):**
    - URL: `http://0.0.0.0:8000/swagger/`
- **Register a new user using Postman:**
    - URL: `http://0.0.0.0:8000/auth/users/`
    - Method: `POST`
    - Body:
      ```json
      {
          "email": "testuser@example.com",
          "first_name": "Test",
          "last_name": "User",
          "password": "testpassword123"
      }
      ```

## API Endpoints

### Authentication
- **Register a new user:** `POST /auth/users/`
- **Obtain JWT token:** `POST /auth/jwt/create/`

### Books
- **Get list of books:** `GET /api/books/`
- **Get book details:** `GET /api/books/{id}/`
- **Add book to favorites:** `POST /api/books/{id}/favorite/`

### Reviews
- **Create a review:** `POST /api/reviews/`
- **Get book reviews:** `GET /api/books/{id}/reviews/`

### Favorites
- **Get user's favorite books:** `GET /api/users/me/favorites/`

## Testing

- Use Postman to test the API. Postman collection can be found in the `postman_test` folder.
- Example test cases include user registration, adding books to favorites, and creating reviews.

## Deployment

For deployment, you can use the provided Docker setup. Ensure that your production environment variables are correctly set, particularly for the database and email configurations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
