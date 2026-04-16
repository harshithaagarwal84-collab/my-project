
from flask import Flask,request,jsonify
from flask_cors import CORS
app=Flask(__name__); CORS(app)
def pred(t):
    return "Spam" if any(w in t.lower() for w in ['free','win','offer','urgent','click']) else "Ham"
@app.route('/api/scan',methods=['POST'])
def scan():
    txt=request.json.get('text','')
    return jsonify({'result':pred(txt)})
@app.route('/api/health')
def h(): return jsonify({'ok':True})
if __name__=='__main__': app.run()
