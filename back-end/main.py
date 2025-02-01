from app import create_app
from waitress import serve

app = create_app()

port = 5000
ip = '0.0.0.0'

if __name__ == "__main__":
    print("Server starting up!")
    print(f"Ip: {ip}, Port: {port}")
    serve(app, host=ip, port=port)
