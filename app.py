from flask import Flask, jsonify, request
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Cross-Origin Resource Sharing 활성화

# 운세 데이터베이스 (실제로는 더 정교한 로직 가능)
fortunes = {
    'love': ['새로운 만남이 기다리고 있습니다', '기존 관계가 더욱 돈독해질 것입니다'],
    'career': ['큰 기회가 찾아올 예정입니다', '꾸준한 노력이 결실을 맺을 것입니다'],
    'health': ['건강 관리에 신경 쓰세요', '활력이 넘치는 하루가 될 것입니다']
}

@app.route('/api/fortune', methods=['POST'])
def get_fortune():
    data = request.json
    name = data.get('name')
    birthdate = data.get('birthdate')
    
    # 간단한 시드 생성 (이름과 날짜 기반)
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
    
    return jsonify(result)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    # 간단한 통계 API (방문자 수, 오늘의 운세 조회 수 등)
    return jsonify({
        'total_requests': random.randint(1000, 5000),
        'today_requests': random.randint(50, 200)
    })
