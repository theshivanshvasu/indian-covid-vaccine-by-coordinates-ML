from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import re

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/home')
def home2():
    return render_template('homepage.html')


@app.route('/aboutproject')
def aboutproject():
    return render_template('aboutproject.html')


@app.route('/sourcecode')
def sourcecode():
    return render_template('sourcecode.html')

@app.route('/creator')
def creator():
    return render_template('creator.html')





@app.route('/prediction' , methods=['POST','GET'])
def prediction():
    data1 = int(float(request.form['a']))
    data2 = int(float(request.form['b']))
    print(data1,data2)
    arr = np.array([[data1, data2]])
    output= model.predict(arr)
    # print(output)
    x= output.tolist()
    # print(x)

    a=x[0][0]
    b=x[0][1]
    c=x[0][2]
    d=x[0][3]
    # print(a,b,c,d)

    if (d<5 ):
        return render_template('prediction.html', p=d ,q=a, r=b, s=c, t=" Less Secured! ⚠ ⚠ ⚠ ⚠ ")
    elif (d<8 & d>=5):
        return render_template('prediction.html', p=d ,q=a, r=b, s=c, t=" Risky! ⚠ ⚠ ⚠ ")  
    elif (d<12 & d>=8):
        return render_template('prediction.html', p=d ,q=a, r=b, s=c, t=" Viable! ★ ")  
    elif (d<20 & d>=12):
        return render_template('prediction.html', p=d ,q=a, r=b, s=c, t=" All Right! ★ ★ ")
    elif (d<32 & d>=20):
        return render_template('prediction.html', p=d ,q=a, r=b, s=c, t=" Fine! ★ ★ ★ ")
    elif (d<40 & d>=32):
        return render_template('prediction.html', p=d ,q=a, r=b, s=c, t=" Safe! ★ ★ ★ ★ ")
    elif (d >= 40):
      return render_template('prediction.html', p=d ,q=a, r=b, s=c, t=" Invulnerable! ★ ★ ★ ★ ★")
    else :
        return render_template('prediction.html', p="N.A." ,q="N.A." , r="N.A." , s="N.A." , t="<br> Something Went Wrong! Please Try With Another Value..." )


if __name__ == "__main__":
    app.run(debug=False)





# <! –– Coded by - Shivansh Vasu @theshivanshvasu ––>









