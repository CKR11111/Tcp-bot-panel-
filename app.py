from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# User Config (तिमीले दिएको विवरण)
USER_ID = "4338314063"
USER_PASS = "CKR_90V42__M22NG"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_friends')
def get_friends():
    url = f"https://danger-friend-management.vercel.app/get_friends_list?uid={USER_ID}&password={USER_PASS}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route('/remove_friend', methods=['POST'])
def remove_friend():
    target_uid = request.json.get('target_uid')
    url = f"https://danger-friend-management.vercel.app/remove_friend?uid={USER_ID}&password={USER_PASS}&friend_uid={target_uid}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route('/add_friend', methods=['POST'])
def add_friend():
    target_uid = request.json.get('target_uid')
    url = f"https://pnl-frind-add-api.vercel.app/adding_friend?uid={USER_ID}&password={USER_PASS}&friend_uid={target_uid}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
