from fastapi import FastAPI

app = FastAPI()

@app.get('/api/works/{user_id}')
def get_works(user_id: int):
    return {"user_id": user_id, "works": []}
