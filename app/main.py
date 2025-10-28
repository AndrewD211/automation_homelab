from fastapi import FastAPI

app = FastAPI(title="Automation Home Lab")

@app.get("/health") # Route Decorator - sets function as HTTP GET handler
# Liveness check used by monitors/CI
def health():   
    return {"status": "ok"}
