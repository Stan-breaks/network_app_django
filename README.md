# NETWORK_APP_DJANGO

This is a twitter basic clone built using Django.

## Requirements

- Python 3
- Django
- A database (SQLite, PostgreSQL, MySQL, etc.)

You can install Django using pip:
```bash
pip install Django
```

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Stan-breaks/network_app_django.git
    ```
2. Navigate to the project directory:
    ```bash
    cd network_app_django
    ```
3. Make migrations:
 ```bash
   python3 manage.py makemigrations
```
4. Apply the migrations:
    ```bash
    python3 manage.py migrate
    ```
5. Run the server:
    ```bash
    python3 manage.py runserver
    ```

Now, you can access the website at `http://localhost:8000`.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
