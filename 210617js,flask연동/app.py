from flask import Flask, request, render_template
# from dao import EmpDAO

# Flask 인스턴스 생성
app = Flask(__name__)

'''
@ : 장식자
app.route('/') == http://localhost:5000/
methods(호출방식) -> get방식
'''
@app.route('/', methods=['get'])    
def get():      # 함수이름 : get
    print("get")
    # 실행되는지 확인하기위한것

    return render_template('reqres.html')
    # render_template함수를 통해서 reqres.html 파일을 렌더링함!
    # html문서 내에 코드 조각들을 삽입하여 웹 페이지를 동적으로 생성할수 있음!
    # http://127.0.0.1:5000/reqres.html url 의미


@app.route('/getdata', methods=['get']) 
def getdata():      # 함수이름 : getdata()
    print("getdata() -----------------------")
    # 실행 되는지 확인작업

    # 함수가 정상적으로 실행되면 JOSN형식으로 리턴값줌
    return '{"name":"재석", "age":49}'




if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
    # 웹앱 실행요청  localhost라 알려진 루프백 주소를 사용함 port넘버는 5000