from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# CSS 樣式（含背景圖）
style = """
<style>
    body {
        background-image: url('/static/2507.jpg');
        background-size: cover;
        background-position: center;
        margin: 0;
        padding: 0;
        font-family: "微軟正黑體", sans-serif;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 12px;
        max-width: 700px;
        text-align: center;
        overflow-y: auto;
    }
    h1 {
        font-size: 48px;
        margin-bottom: 20px;
    }
    p {
        font-size: 22px;
        line-height: 1.6;
    }
    img {
        max-width: 90%;
        max-height: 200px;
        height: auto;
        margin: 15px 0;
        border-radius: 10px;
    }
    button {
        font-size: 20px;
        padding: 12px 24px;
        margin-top: 25px;
        background-color: #f27979;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
    }
    button:hover {
        background-color: #d95d5d;
    }
</style>
"""

# 首頁
@app.route('/')
def index():
    return render_template_string(f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>吳昌彥的故事</title>
        {style}
    </head>
    <body>
        <div class="container">
            <h1>我的故事</h1>
            <p>我是吳昌彥，我很慘，我非常慘……</p>
            <a href="/story"><button>閱讀故事</button></a>
        </div>
    </body>
    </html>
    """)

# 故事頁（直接顯示兩張圖片）
@app.route('/story')
def story():
    return render_template_string(f"""
    <html>
    <head>
        <title>破碎的我</title>
        {style}
    </head>
    <body>
        <div class="container">
            <h1>破碎的我</h1>
            <p>我的父親不是世界首富，母親也不是台灣富豪，但我從未放棄。</p>
            <img src="/static/6908.jpg" alt="故事圖片 1">
            <img src="/static/4502.jpg" alt="故事圖片 2">
            <p>所以我需要一點幫助。</p>
            <a href="/donate"><button>我要捐款</button></a>
        </div>
    </body>
    </html>
    """)

# 捐款頁
@app.route('/donate')
def donate():
    return render_template_string(f"""
    <html>
    <head>
        <title>我要捐款</title>
        {style}
    </head>
    <body>
        <div class="container">
            <h1>捐款資訊</h1>
            <p>銀行名稱：合作金庫銀行</p>
            <p>帳號：1117872123227</p>
            <p>戶名：吳昌彥</p>
            <a href="/"><button>回首頁</button></a>
        </div>
    </body>
    </html>
    """)

# Google 驗證用 HTML 檔案（請確認檔案已放在根目錄）
@app.route('/google255dd87781a8ec94.html')
def google_verify():
    return send_from_directory('.', 'google255dd87781a8ec94.html')

# 啟動伺服器
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
