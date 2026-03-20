from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working 🚀"}

@app.get("/run")
def run():
    subprocess.run(["python", "src/main.py"])
    return {"status": "Digest generated ✅"}