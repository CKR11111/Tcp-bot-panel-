import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Config - User Details
USER_ID = "4338314063"
USER_PASS = "CKR_90V42__M22NG"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/action', methods=['POST'])
def handle_api():
    data = request.json
    action_type = data.get('type')
    target_uid = data.get('target_uid')

    # API Endpoints
    if action_type == 'get_list':
        url = f"https://danger-friend-management.vercel.app/get_friends_list?uid={USER_ID}&password={USER_PASS}"
    elif action_type == 'add':
        # New API link provided in previous chat
        url = f"https://ckrunknown-ff-api-req.hf.space/get_player_info?player_id={target_uid}&uid={USER_ID}&password={USER_PASS}"
    elif action_type == 'remove':
        url = f"https://danger-friend-management.vercel.app/remove_friend?uid={USER_ID}&password={USER_PASS}&friend_uid={target_uid}"
    elif action_type == 'track':
        # Player Tracking API
        url = f"https://player-status-api.onrender.com/api/info/{target_uid}"
    else:
        return jsonify({"status": "error", "message": "Invalid action"}), 400

    try:
        response = requests.get(url, timeout=15)
        
        # Check if response is successful
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"status": "error", "message": f"API Error: {response.status_code}"})
    except Exception as e:
        return jsonify({"status": "error", "message": "Connection Failed", "details": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
