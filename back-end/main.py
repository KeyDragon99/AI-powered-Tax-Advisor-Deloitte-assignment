from app import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
    print("Server starting up!")
    print(f"Ip: {'0.0.0.0'}, Port: 5000")
    serve(app, port=5000)
