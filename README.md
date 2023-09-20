# Travel and Tours Backend

## Description

This is the backend for a Travel and Tours business built using Django. It provides APIs for managing tours, destinations, and bookings.

## Features

- CRUD operations for Tours, Destinations, and Bookings.
- User authentication and authorization.
- Integration with Paystack API for payments.
- User and Admin dashboards.
- ...

## Setup

### Requirements

- Python 3.x
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/travels_backend.git
   cd travels_backend
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv my_env
   source my_env/bin/activate
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for accessing the admin dashboard):

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The project will be accessible at `http://127.0.0.1:8000/`.

## Usage

- Access the admin dashboard at `http://127.0.0.1:8000/admin/` to manage data.
- Use the provided API endpoints for interacting with the backend.

## API Endpoints

- Tours: `/api/tours/`
- Destinations: `/api/destinations/`
- Accommodations: `/api/accommodations/`
- Activities: `/api/activities/`
- Bookings: `/api/bookings/`
- User Dashboard: `/api/user/`

## Authentication

- The backend supports user registration and login.
- User authentication is required for certain operations.

## Payment Integration

- The backend is integrated with the Paystack API for handling payments.

## File Structure

```
travels_backend/
├── accounts/
│   ├── ...
├── accommodations/
│   ├── ...
├── activities/
│   ├── ...
├── bookings/
│   ├── ...
├── destinations/
│   ├── ...
├── media/
├── static/
├── templates/
├── db.sqlite3
├── manage.py
├── Procfile
├── requirements.txt
└── runtime.txt
```

## Contributing

Feel free to contribute to this project. You can submit issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).


This includes the project's current structure and features, as well as the updated file structure to reflect the different apps you've created. If there's any specific information you'd like to add or modify, please let me know!


