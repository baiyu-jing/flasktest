from flask import Flask,request,jsonify

app=Flask(__name__)
#http://127.0.0.1:5000/index
#http://127.0.0.1:5000/index?age=666&pwd=123
#http://127.0.0.1:5000/index
    #请求体：xx=123&yy=999

@app.route("/index",methods=["POST","GET"])
def index():
    # age=request.args.get("age")
    # pwd=request.args.get("pwd")
    # print(age,pwd)
    #
    # xx=request.form.get("xx")
    # yy=request.form.get("yy")
    # print(xx,yy)
    #
    # print(request.json)
    return jsonify({"status":False,"data":"aasfaifweoibn"})

@app.route("/home")
def home():
    return "失败"

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000)