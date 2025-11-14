import React,{useState} from 'react'
import {up,sc,en,gen} from './api'

export default function App(){
  const[f,sf]=useState();const[p,sp]=useState();const[k,sk]=useState("")
  const[t,st]=useState("");const[r,sr]=useState();const[e,se]=useState()
  const[n,sn]=useState("");const[em,sem]=useState("");const[ph,sph]=useState("");const[h,sh]=useState("")
  const U=async()=>{let x=await up(f);sp(x.data.parsed);sn(x.data.parsed.name||"");sem(x.data.parsed.email||"");sph(x.data.parsed.phone||"")}
  const S=async()=>{let x=await sc(p,k);sr(x.data)}
  const E=async()=>{let x=await en(p,t,k);se(x.data)}
  const G=async()=>{let x=await gen(e,n,em,ph,h);let u=URL.createObjectURL(new Blob([x.data]));let a=document.createElement("a");a.href=u;a.download="res.docx";a.click()}
  return(<div>
    <h1>Resume</h1>
    <input type="file" onChange={z=>sf(z.target.files[0])}/>
    <button onClick={U}>upload</button>
    <pre>{p?JSON.stringify(p,null,2):""}</pre>
    <input value={t} onChange={z=>st(z.target.value)} placeholder="job"/>
    <input value={k} onChange={z=>sk(z.target.value)} placeholder="keywords"/>
    <button onClick={S}>score</button>
    <pre>{r?JSON.stringify(r,null,2):""}</pre>
    <button onClick={E}>enhance</button>
    <pre>{e?JSON.stringify(e,null,2):""}</pre>
    <input value={n} onChange={z=>sn(z.target.value)} placeholder="name"/>
    <input value={em} onChange={z=>sem(z.target.value)} placeholder="email"/>
    <input value={ph} onChange={z=>sph(z.target.value)} placeholder="phone"/>
    <input value={h} onChange={z=>sh(z.target.value)} placeholder="headline"/>
    <button onClick={G}>docx</button>
  </div>)
}