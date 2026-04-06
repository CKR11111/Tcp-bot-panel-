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

    try:
        if action_type == 'get_list':
            url = f"https://danger-friend-management.vercel.app/get_friends_list?uid={USER_ID}&password={USER_PASS}"
        elif action_type == 'add':
            # New Fixed Add Friend API
            url = f"https://ckrunknown-ff-api-req.hf.space/get_player_info?player_id={target_uid}&uid={USER_ID}&password={USER_PASS}"
        elif action_type == 'remove':
            url = f"https://danger-friend-management.vercel.app/remove_friend?uid={USER_ID}&password={USER_PASS}&friend_uid={target_uid}"
        elif action_type == 'track':
            # Updated Tracking API
            url = f"https://player-status-api.onrender.com/api/info/{target_uid}"
        else:
            return jsonify({"error": "Invalid action"}), 400

        # API Request with timeout to prevent hanging
        response = requests.get(url, timeout=10)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": "API Connection Failed", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
