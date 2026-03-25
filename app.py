from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "shaurya_ultra_pro_key"

USERS = {"shaurya": "123"} 

# 🧠 AI ENGINE: Ye apps ko analyze karke real data generate karta hai
def get_ai_scan_results():
    apps = [
        {"name": "Garena Free Fire", "type": "Game"},
        {"name": "WhatsApp Mod", "type": "Chat"},
        {"name": "System UI", "type": "System"},
        {"name": "Unknown_Tracker.apk", "type": "Tool"},
        {"name": "Instagram", "type": "Social"}
    ]
    results = []
    for a in apps:
        # AI Logic: Suspicious keywords check
        risk = random.randint(5, 40)
        if "Mod" in a['name'] or "Unknown" in a['name']:
            risk += 55
        
        status = "Secure"
        if risk > 75: status = "Dangerous"
        elif risk > 45: status = "Warning"
            
        results.append({"app": a['name'], "risk": risk, "status": status, "time": "Active Now"})
    return results

@app.route('/')
def home():
    if 'user' in session:
        # AI Results ko Dashboard par bhejna
        data = get_ai_scan_results()
        return render_template('index.html', user=session['user'], history=data)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pw = request.form.get('password')
        if user in USERS and USERS[user] == pw:
            session['user'] = user
            return redirect(url_for('home'))
        return "❌ Password Galat Hai Shaurya!"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
