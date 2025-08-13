from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from datetime import datetime

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 운세 데이터베이스
fortunes = {
    'love': ['새로운 만남이 기다리고 있습니다', '기존 관계가 더욱 돈독해질 것입니다'],
    'career': ['큰 기회가 찾아올 예정입니다', '꾸준한 노력이 결실을 맺을 것입니다'],
    'health': ['건강 관리에 신경 쓰세요', '활력이 넘치는 하루가 될 것입니다']
}

# Request/Response 모델
class FortuneRequest(BaseModel):
    name: str
    birthdate: str

@app.post('/api/fortune')
async def get_fortune(request: FortuneRequest):
    name = request.name
    birthdate = request.birthdate
    
    # 간단한 시드 생성
    seed = len(name) + int(birthdate.replace('-', ''))
    random.seed(seed)
    
    result = {
        'name': name,
        'date': datetime.now().strftime('%Y-%m-%d'),
        'love': random.choice(fortunes['love']),
        'career': random.choice(fortunes['career']),
        'health': random.choice(fortunes['health']),
        'lucky_number': random.randint(1, 100)
    }
    
    return result

@app.get('/api/stats')
async def get_stats():
    return {
        'total_requests': random.randint(1000, 5000),
        'today_requests': random.randint(50, 200)
    }
