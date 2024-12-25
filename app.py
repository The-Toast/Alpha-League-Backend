from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 도메인에서 요청을 받을 수 있도록 설정

# 샘플 데이터
data = [
    {
        "name": "문예찬",
        "profile_image_url": "https://s3.makerin.kr/media/6ca53395-2911-43e6-aa36-270eca7825c8.webp",
        "profit_krw": "152,300원",
        "profit_rate": "15.23%",
        "profit_usd": "$130",
        "rank": 1,
        "starting_assets_krw": "1,000,000원",
        "starting_assets_usd": "$850",
        "stocks_purchased": ["단타 중독", "TSLL", "RGTI"],
        "na_rock": False
    },
    {
        "name": "방주원",
        "profile_image_url": "https://s3.makerin.kr/media/c7d38592-5a03-4faa-bdfc-4b0da475f635.jpg",
        "profit_krw": "215,000원",
        "profit_rate": "10.75%",
        "profit_usd": "$182",
        "rank": 2,
        "starting_assets_krw": "2,000,000원",
        "starting_assets_usd": "$1700",
        "stocks_purchased": ["테슬라 사랄때 안산놈", "포지션이 없습니다"],
        "na_rock": False
    },
    # {
    #     "name": "김시현",
    #     "profile_image_url": "https://s3.makerin.kr/media/d24a0af4-b2be-4fd0-9ee7-8fc5690349e6.webp",
    #     "profit_krw": "118,350원",
    #     "profit_rate": "7.89%",
    #     "profit_usd": "$101",
    #     "rank": 3,
    #     "starting_assets_krw": "1,500,000원",
    #     "starting_assets_usd": "$1275",
    #     "stocks_purchased": ["테슬라 신도", "TSLA", "TSLL"],
    #     "na_rock": False
    # },
    {
        "name": "김시현",
        "profile_image_url": "https://s3.makerin.kr/media/73388d45-418f-4f65-a58e-01192ef472eb.webp",
        "profit_krw": "-334,052원",
        "profit_rate": "-12.14%",
        "profit_usd": "나도몰라야발",
        "rank": 3,
        "starting_assets_krw": "1,500,000원",
        "starting_assets_usd": "$1275",
        "stocks_purchased": ["테슬라 신도", "TSLA", "TSLL"],
        "na_rock": True
    }
]


# 엔드포인트: /api/data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Flask 서버 실행 (0.0.0.0으로 설정)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5173, debug=True)
