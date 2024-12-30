# My FastAPI App

This project is a simple FastAPI application that includes a health check endpoint to verify the connection between the frontend and backend.

## Project Structure

```
my-fastapi-app
├── src
│   ├── main.py          # Entry point of the FastAPI application
│   └── routers
│       └── health.py    # Health check router
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:

   ```
   git clone <repository-url>
   cd my-fastapi-app
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

Once the application is running, you can access the health check endpoint at:

```
http://localhost:8000/health
```

This will return a JSON response:

```json
{
  "status": true
}
```

## License

This project is licensed under the MIT License.
