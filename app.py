from flask import Flask, render_template_string
import os

app = Flask(__name__)

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
        max-width: 600px;
        padding: 20px;
    }
    h1 {
        font-size: 48px;
        margin-bottom: 20px;
    }
    p {
        font-size: 20px;
        line-height: 1.6;
    }
    img {
        max-width: 100%;
        height: auto;
        margin-top: 20px;
    }
    button {
        font-size: 18px;
        padding: 10px 20px;
        margin-top: 25px;
        background-color: #f27979;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    button:hover {
        background-color: #d95d5d;
    }
</style>
"""

@app.route('/')
def index():
    return render_template_string(f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="吳昌彥的真實故事與募款網站">
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

@app.route('/吳昌彥')
def changyanwu():
    return f"""
    <html>
        <head><title>吳昌彥</title>{style}</head>
        <body>
            <div class="container">
                <h1>這是吳昌彥</h1>
                <img src="/static/4502.jpg" alt="吳昌彥照片" width="300">
                <br><a href="/"><button>回首頁</button></a>
            </div>
        </body>
    </html>
    """

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
            <p>我的父親好賭，母親重病，我從未放棄。</p>
            <img src="/static/4502.jpg" alt="故事圖片">
            <p>我需要一點幫助。</p>
            <a href="/donate"><button>我要捐款</button></a>
        </div>
    </body>
    </html>
    """)

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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
