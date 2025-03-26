from app import app
from app.models.users import User


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)