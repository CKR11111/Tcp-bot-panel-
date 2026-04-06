import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

    if action_type == 'get_list':
        url = f"https://danger-friend-management.vercel.app/get_friends_list?uid={USER_ID}&password={USER_PASS}"
    elif action_type == 'add':
        url = f"https://ckrunknown-ff-api-req.hf.space/get_player_info?player_id={target_uid}&uid={USER_ID}&password={USER_PASS}"
    elif action_type == 'remove':
        url = f"https://danger-friend-management.vercel.app/remove_friend?uid={USER_ID}&password={USER_PASS}&friend_uid={target_uid}"
    elif action_type == 'track':
        url = f"https://player-status-api.onrender.com/api/info/{target_uid}"
    else:
        return jsonify({"status": "error", "message": "Invalid Action"}), 400

    try:
        # 15 second timeout to handle slow APIs
        response = requests.get(url, timeout=15)
        
        # Check if API returned valid data
        if response.status_code == 200:
            try:
                return jsonify(response.json())
            except:
                return jsonify({"status": "error", "message": "API returned invalid format (Not JSON)"})
        else:
            return jsonify({"status": "error", "message": f"API Error Code: {response.status_code}"})
            
    except requests.exceptions.Timeout:
        return jsonify({"status": "error", "message": "API Connection Timeout (Slow Server)"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
