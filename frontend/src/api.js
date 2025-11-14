import axios from 'axios'
const B='http://localhost:8000'
export const up=f=>{let d=new FormData();d.append("file",f);return axios.post(B+"/upload",d)}
export const sc=(p,kw)=>{let d=new FormData();d.append("p",JSON.stringify(p));d.append("kw",kw);return axios.post(B+"/score",d)}
export const en=(p,t,kw)=>{let d=new FormData();d.append("p",JSON.stringify(p));d.append("title",t);d.append("kw",kw);return axios.post(B+"/enhance",d)}
export const gen=(e,n,em,ph,h)=>{let d=new FormData();d.append("e",JSON.stringify(e));d.append("name",n);d.append("email",em);d.append("phone",ph);d.append("hl",h);return axios.post(B+"/generate_docx",d,{responseType:"blob"})}
