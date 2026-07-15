from flask import Flask,request,jsonify

app=Flask(__name__)


@app.route("/index")
def index():
    return "成功访问"

#路由参数
@app.route("/index1",methods=["POST","GET"])
def index1():
    return "成功访问1"


#url参数查询
#http://127.0.0.1:5000/index?age=123&pwd=666
@app.route("/index2")
def index2():
    age=request.args.get("age")
    pwd=request.args.get("pwd")
    print(age,pwd)
    return "成功访问2"

#post,json请求体
@app.route("/index3",methods=["POST"])
def index3():

    post1=request.form.get("post1")

    json1=request.get_json()
    return jsonify({"status":True,"str":"123456"})


if __name__ == '__main__':
    app.run()



