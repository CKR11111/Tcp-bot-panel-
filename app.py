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

    if action_type == 'get_list':
        url = f"https://danger-friend-management.vercel.app/get_friends_list?uid={USER_ID}&password={USER_PASS}"
    elif action_type == 'add':
        url = f"https://pnl-frind-add-api.vercel.app/adding_friend?uid={USER_ID}&password={USER_PASS}&friend_uid={target_uid}"
    elif action_type == 'remove':
        url = f"https://danger-friend-management.vercel.app/remove_friend?uid={USER_ID}&password={USER_PASS}&friend_uid={target_uid}"
    else:
        return jsonify({"error": "Invalid action"}), 400

    try:
        response = requests.get(url, timeout=15)
        return jsonify(response.json())
    except:
        return jsonify({"error": "API Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
