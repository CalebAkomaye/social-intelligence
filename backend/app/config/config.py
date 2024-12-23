from dotenv import load_dotenv
import os

load_dotenv()

HOST=os.getenv("HOST")
PORT=int(os.getenv("PORT"))

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

URI=os.getenv('MONGODB_URI')