# Flask API Project

This is a simple Flask API project providing timestamp and health check endpoints.

## Prerequisites

- Python 3.x
- pip

## Installation

### Windows

1.  Clone the repository or navigate to the project directory.
2.  Create a virtual environment (optional but recommended):
    ```powershell
    python -m venv venv
    ```
3.  Activate the virtual environment:
    ```powershell
    .\venv\Scripts\activate
    ```
4.  Install the required dependencies:
    ```powershell
    pip install -r requirements.txt
    ```

### Linux / macOS

1.  Clone the repository or navigate to the project directory.
2.  Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    ```
3.  Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
4.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

### Development Environment

To start the server in development mode (with debug enabled):

```bash
python run.py
```

The server will start at `http://localhost:5000`.

### Production Environment

For production, it is recommended to use a production-ready WSGI server.

#### Windows

On Windows, you can use `waitress`.

1.  Install `waitress`:
    ```powershell
    pip install waitress
    ```
2.  Run the application:
    ```powershell
    waitress-serve --port=5000 app:app
    ```

#### Linux

On Linux, `gunicorn` is a popular choice.

1.  Install `gunicorn`:
    ```bash
    pip install gunicorn
    ```
2.  Run the application:
    ```bash
    gunicorn -w 4 -b 0.0.0.0:5000 app:app
    ```

## Endpoints

-   `GET /time`: Returns the current timestamp.
-   `GET /health`: Checks the disk utilization (C: drive on Windows). Returns "Warning" if usage is > 80%, otherwise "OK".
