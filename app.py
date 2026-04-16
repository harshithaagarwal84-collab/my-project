
from flask import Flask,render_template,request,jsonify
app=Flask(__name__)
spam_words=['win','prize','lottery','free','urgent','click','claim','money','offer']
def predict_text(t):
    score=sum(w in t.lower() for w in spam_words)
    return ('SPAM', min(99,50+score*10)) if score>=2 else ('SAFE', max(60,95-score*10))
@app.route('/')
def home(): return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    txt=request.form.get('email','')
    pred,conf=predict_text(txt)
    return render_template('index.html',prediction=pred,confidence=conf,email=txt)
@app.route('/api/predict',methods=['POST'])
def api():
    txt=request.json.get('email','')
    pred,conf=predict_text(txt)
    return jsonify({'prediction':pred,'confidence':conf})
if __name__=='__main__': app.run(debug=True)
