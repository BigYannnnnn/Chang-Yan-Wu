from flask import Flask, render_template_string
import os

app = Flask(__name__)

# 統一樣式
style = """
<style>
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        font-family: "微軟正黑體", sans-serif;
        background-color: #fff8f0;
    }
    .container {
        text-align: center;
        max-width: 700px;
        padding: 30px;
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
        max-width: 100%;
        height: auto;
        margin-top: 20px;
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

# 故事頁
@app.route('/story')
def story():
    return render_template_string(f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>破碎的我</title>
        {style}
        <style>
            .image-wrapper {{
                position: relative;
                display: none;
                margin-top: 30px;
            }}
            .image-wrapper::before {{
                content: "";
                background-image: url('/static/2507.jpg');  /* 背景圖 */
                background-size: cover;
                background-position: center;
                opacity: 0.3;  /* 背景透明度 */
                position: absolute;
                top: 0; left: 0;
                width: 100%; height: 100%;
                z-index: 0;
                border-radius: 12px;
            }}
            .image-wrapper img {{
                position: relative;
                z-index: 1;
                width: 100%;
                border-radius: 12px;
            }}
        </style>
        <script>
            function showImage() {{
                document.getElementById('image-wrapper').style.display = 'block';
                document.getElementById('show-img-btn').style.display = 'none';
            }}
        </script>
    </head>
    <body>
        <div class="container">
            <h1>破碎的我</h1>
            <p>我的父親好賭，母親重病，我從未放棄。</p>
            <p>我需要一點幫助。</p>
            <button id="show-img-btn" onclick="showImage()">點我看圖片</button><br>
            <div id="image-wrapper" class="image-wrapper">
                <img src="/static/4502.jpg" alt="故事圖片">
            </div>
            <br><br>
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
        <meta charset="UTF-8">
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

# 啟動
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
