# Flask API Frontend Example

A web-based login interface that integrates with a Flask API backend.

## Features

- 🔐 Beautiful login form with gradient UI
- ✅ Successful login displays authentication token
- ❌ Failed login shows error message with meme
- 🔄 Loading animation during authentication
- 📱 Responsive design

## Installation

1. Clone the repository:
```bash
git clone https://github.com/afmirandad/FlaskApiFrontendExample.git
cd FlaskApiFrontendExample
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## API Integration

The application sends POST requests to:
- **Endpoint**: `https://flaskapiexample-production.up.railway.app/users/login`
- **Method**: POST
- **Body**: JSON with `username` and `password`

### Response Format

**Success (200):**
```json
{
  "token": "your-auth-token"
}
```

**Failure (non-200):**
Any other status code is treated as authentication failure.

## Project Structure

```
FlaskApiFrontendExample/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── login.html     # Login page with styling
└── README.md          # This file
```

## Technologies Used

- **Flask 3.0.0** - Web framework
- **Requests 2.31.0** - HTTP library for API calls
- **HTML/CSS/JavaScript** - Frontend
