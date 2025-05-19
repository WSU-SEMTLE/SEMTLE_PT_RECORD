from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 허용 (리액트에서 요청 가능하게)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    print(f"[서버 로그] 로그인 시도: {username} / {password}")
    return {"message": "로그인 완료"}
