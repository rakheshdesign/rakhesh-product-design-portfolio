const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const n of ['one','two']){const p=await b.newPage();await p.goto('file://'+__dirname+'/'+n+'.html');await p.waitForTimeout(500);
await p.pdf({path:__dirname+`/${n}.pdf`,width:'794px',height:'1123px',printBackground:true,margin:{top:0,bottom:0,left:0,right:0}});
// overflow check
const o=await p.evaluate(()=>[...document.querySelectorAll('.page')].map(pg=>{let bad=[];pg.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect(),pr=pg.getBoundingClientRect();if(r.bottom>pr.bottom+1)bad.push((e.className||e.tagName)+':'+Math.round(r.bottom-pr.bottom))});return bad.slice(0,5)}));
console.log(n,JSON.stringify(o));await p.close()}
await b.close()})();
