from src.setting import HOST, PORT
from src import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(host=HOST, port=PORT)
