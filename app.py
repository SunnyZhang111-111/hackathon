import model
from flask import Flask,redirect,url_for,render_template,request
from flask_cors import CORS
import os
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("template_ws.html")

@app.route('/messages', methods=['POST',"GET"])
def api_message():
    filepath = './file.wav'
    f = open(filepath, 'wb')
    f.write(request.data)
    f.close()
    print("done with uploading wav files")
    # 返回图片的url
    # imgsrc=model.run_model(filepath)
    # return render_template("template2.html",imgsrc=imgsrc)
    return render_template("template2.html")

# 配置全局变量

# @app.context_processor
# def context_processor():
    
#     detectron=model.detectron()
#     gan=model.gan()
#     # return 是 dictionary type
#     return dict(gan=gan,detectron=detectron)

if __name__=="__main__":
    app.run(debug=True) 