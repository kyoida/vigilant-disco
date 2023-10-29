from app import app
from api.main import app as api_app

if __name__ == '__main__':
    app.run(debug=True)
    api_app.run(host="0.0.0.0", port=8000)
