from flask import Flask, render_template_string
app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
    <html>
    <head><title>吳昌彥的故事</title></head>
    <body style="text-align: center; font-family: 微軟正黑體;">
        <h1>我的故事</h1>
        <p>我是吳昌彥，我很慘，我非常慘……</p>
        <a href="/story"><button>閱讀故事</button></a>
    </body>
    </html>
    """)

@app.route("/story")
def story():
    return render_template_string("""
    <html>
    <head><title>破碎的我</title></head>
    <body style="text-align: center; font-family: 微軟正黑體;">
        <h1>破碎的我</h1>
        <p>我的父親好賭，母親重病，我從未放棄。</p>
        <img src="/static/4502.jpg" width="300"><br>
        <p>我需要一點幫助。</p>
        <a href="/donate"><button>我要捐款</button></a>
    </body>
    </html>
    """)

@app.route("/donate")
def donate():
    return render_template_string("""
    <html>
    <head><title>捐款資訊</title></head>
    <body style="text-align: center; font-family: 微軟正黑體;">
        <h1>捐款資訊</h1>
        <p>銀行名稱：合作金庫銀行</p>
        <p>帳號：1117872123227</p>
        <p>戶名：吳昌彥</p>
      <br><br>
        <a href="/"><button>回首頁</button></a>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run()
