
import React,{useState} from 'react';
export default function App(){
 const [text,setText]=useState(''); const [result,setResult]=useState('');
 const scan=async()=>{
   const r=await fetch('http://localhost:5000/api/scan',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text})});
   const d=await r.json(); setResult(d.result);
 };
 return <div style={{fontFamily:'Arial',padding:40,background:'#0f172a',minHeight:'100vh',color:'white'}}>
 <h1>🚀 SpamX Startup Modern</h1>
 <textarea value={text} onChange={e=>setText(e.target.value)} style={{width:'100%',height:180,borderRadius:10}} />
 <br/><br/><button onClick={scan}>Scan Email</button>
 <h2>{result}</h2></div>
}
