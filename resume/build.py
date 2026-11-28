import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import base64,re
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from data import *
from PIL import Image, ImageFilter
ph=base64.b64encode(open('portrait_c2.jpg','rb').read()).decode()
BG='#07090D';CARD='#0F131B';CARD2='#151A22';INK='#F5F7FA';INK2='#A9B4C3';INK3='#8491A3';LINE='#1F2733';ACC='#66F5B2'
LBG='#F7F9FC';LCARD='#FFFFFF';LCARD2='#F1F4F8';LINK='#101318';LINK2='#44505F';LINK3='#5B6879';LACC='#0F7A4D';LLINE='#E4E9F0'
F='fonts/'
CSS=f"""
@font-face{{font-family:Inter;font-weight:400;src:url({F}inter/inter-latin-400-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:500;src:url({F}inter/inter-latin-500-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:600;src:url({F}inter/inter-latin-600-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:700;src:url({F}inter/inter-latin-700-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:400;font-style:italic;src:url({F}inter/inter-latin-400-italic.woff2)}}
@font-face{{font-family:'Space Grotesk';font-weight:500;src:url({F}sg/space-grotesk-latin-500-normal.woff2)}}
@font-face{{font-family:'Space Grotesk';font-weight:700;src:url({F}sg/space-grotesk-latin-700-normal.woff2)}}
@font-face{{font-family:'Instrument Serif';font-style:italic;font-weight:400;src:url({F}is/instrument-serif-latin-400-italic.woff2)}}
@page{{size:794px 1123px;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:Inter,sans-serif;font-size:11px;line-height:1.45;color:{LINK}}}
a{{color:inherit;text-decoration:none}}
b{{font-weight:600}}
.page{{width:794px;height:1123px;position:relative;overflow:hidden;page-break-after:always}}
.page:last-child{{page-break-after:auto}}
.sg{{font-family:'Space Grotesk',sans-serif;letter-spacing:-.02em}}
.ser{{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;letter-spacing:0}}
.kick{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:11px;letter-spacing:.08em;text-transform:uppercase}}
.ci{{display:inline-flex;align-items:center;justify-content:center;border-radius:50%;background:{ACC};color:{BG};flex:none}}
.pill{{display:inline-flex;align-items:center;gap:6px;border-radius:99px;background:#1B2230;color:{INK2};padding:5px 11px;font-size:10px;font-weight:500}}
.tag{{display:inline-block;border-radius:99px;font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:9px;letter-spacing:.06em;text-transform:uppercase;padding:3px 9px}}
.chip{{display:inline-block;border-radius:99px;background:{CARD2};color:{INK2};padding:3.5px 10px;font-size:10px;font-weight:500;margin:0 5px 6px 0}}
ul.b{{list-style:none}}
ul.b li{{position:relative;padding-left:13px}}
ul.b li:before{{content:'';position:absolute;left:1px;top:.6em;width:5px;height:5px;border-radius:50%;background:var(--bc)}}
"""
def circ(name,url,size=24):
    return f'<a class="ci" style="width:{size}px;height:{size}px" href="{url}"><span style="width:{size*0.56}px;height:{size*0.56}px;display:block">{ic(name)}</span></a>'
def bullets(items,fs,gap,bc,col):
    return f'<ul class="b" style="font-size:{fs}px;--bc:{bc};color:{col}">'+''.join(f'<li style="margin-bottom:{gap}px">{i}</li>' for i in items)+'</ul>'
def chips(t,cls='chip',st=''): return ''.join(f'<span class="{cls}" style="{st}">{x}</span>' for x in t.split(' • '))
def photo(size,left=None,right=None,top=0):
    pos=(f'left:{left}px;' if left is not None else f'right:{right}px;')
    r=size*0.5
    return f'<div style="position:absolute;{pos}top:{top}px;width:{size}px;height:{size}px;border-radius:50% 50% 0 50%;overflow:hidden;background:{CARD2}"><img src="data:image/jpeg;base64,{ph}" style="width:100%;height:100%;display:block;object-fit:cover"></div>'
QC=lambda vx,vy,r:f'M{vx} {vy} H{vx-r} A{r} {r} 0 0 0 {vx} {vy+r}Z'
LEAF_OLD='M61 7 L53 13 L44 19 L33 25 L20 31 L9 37 L10 97 L15 102 L36 97 L50 91 L61 85 L69 79 L75 73 L81 67 L85 61 L89 55 L93 49 L95 43 L98 37 L100 31 L101 25 L103 19 L103 7Z'
def contact_dark(sz=30):
    return f"""<div style="display:flex;justify-content:space-between;align-items:center;font-size:11.5px;color:{INK2}">
  <div style="line-height:1.9"><div style="display:flex;gap:9px;align-items:center">{circ('phone','tel:+917036534813',20)}<a href="tel:+917036534813">{PHONE}</a></div><div style="display:flex;gap:9px;align-items:center">{circ('mail','mailto:'+EMAIL,20)}<a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
  <div style="display:flex;gap:10px">{circ('globe',PORT,sz)}{circ('in',LI,sz)}</div></div>"""
def stats(n,l,pad,gap=1):
    return '<div style="display:flex">'+''.join(f'<div style="flex:1;padding-right:{pad}px"><div class="sg" style="font-size:{n}px;font-weight:700;color:{ACC};line-height:1.1">{a}</div><div style="font-size:{l}px;color:{INK3};margin-top:{gap}px;line-height:1.3">{b}</div></div>' for a,b in STATS)+'</div>'
SK=[("AI",["AI-assisted design and building","Claude Design","Claude Code","Replit","Figma Make","Copilot","Human-AI interaction design"]),
("Research &amp; Optimization",["Usability and UAT testing","Journey mapping","A/B experiments","Hypotheses and synthesis"]),
("Design Systems &amp; Scale",["Design systems","Figma Variables","Localization (L10n)","Internationalization (i18n)","Component libraries"]),
("Product &amp; UX",["End-to-end product design","Interaction design","Information architecture","User flows","Prototyping","Accessibility (A11Y)","Product thinking"]),
("Collaboration &amp; Leadership",["Cross-functional partnership","Workshop facilitation","Stakeholder management","Mentoring","Design critique"]),
("Tools",["Figma","FigJam","Miro","Whimsical","Adobe Creative Suite","ClickUp"])]
def two():
    tl=[("Jul 2024 – Present","American Express","Sr. Associate, Product Designer","Lead Designer · Core Portfolio",True),
        ("Feb 2022 – Feb 2024","Saveo HealthTech Pvt. Ltd.","Product Designer","B2B and B2C healthtech products",False),
        ("Jun 2021 – Feb 2022","Bommu Herbals Pvt. Ltd.","Motion Graphic Designer","E-commerce, packaging and motion assets",False),
        ("Jul 2020 – Jun 2021","Strategic Innovative Ads","Graphic-Motion Designer","Web, campaign and motion work",False)]
    n=len(tl);GAP=10
    rows='';top=0;ys=[]
    for i,(d,c,t,sd,cur) in enumerate(tl):
        h=86 if cur else 66
        ny=top+(h-10)/2 if False else top+22
        ys.append(ny)
        node=(f'<div style="position:absolute;left:0;top:{ny-10}px;width:20px;height:20px;border-radius:50%;background:rgba(102,245,178,.22)"></div><div style="position:absolute;left:5px;top:{ny-5}px;width:10px;height:10px;border-radius:50%;background:{ACC}"></div>' if cur else
              f'<div style="position:absolute;left:5px;top:{ny-5}px;width:10px;height:10px;border-radius:50%;background:#3A4656"></div>')
        tag=(f'<span class="tag" style="background:{ACC};color:{BG}">{d}</span>' if cur else f'<span class="tag" style="background:{CARD2};color:{INK2}">{d}</span>')
        desc=f'<div style="font-size:10px;color:{INK3};margin-top:1px">{sd}</div>' if cur else ''
        card=f'<div style="position:absolute;left:34px;right:0;top:{top}px;height:{h}px;border-radius:16px;background:{"#12241E" if cur else CARD2};padding:9px 14px">{tag}<div class="sg" style="font-size:14px;font-weight:700;color:{INK};margin-top:6px;line-height:1.15">{c}</div><div style="font-size:11px;color:{INK};margin-top:2px;font-weight:500">{t}</div>{desc}</div>'
        rows+=node+card; top+=h+GAP
    total=top-GAP
    track=f'<div style="position:absolute;left:8.5px;top:{ys[0]}px;width:3px;height:{ys[-1]-ys[0]}px;border-radius:2px;background:#2A3441"></div><div style="position:absolute;left:8.5px;top:{ys[0]}px;width:3px;height:{(ys[1]-ys[0])*0.5}px;border-radius:2px;background:{ACC}"></div>'
    exp=f'<div style="position:relative;height:{total}px">{track}{rows}</div>'
    skills=''.join(f'<div style="margin-bottom:13px"><div class="kick" style="color:{INK};margin-bottom:6px;display:flex;align-items:center;gap:7px;font-size:10.5px"><span style="width:7px;height:7px;border-radius:50%;background:{ACC};display:inline-block"></span>{h}</div><div>{"".join(f"<span class=chip style=font-size:9.6px;padding:3px:8px;margin:0:4px:4px:0>{x}</span>".replace(":"," ").replace("padding 3px 8px","padding:2.5px 8px").replace("margin 0 4px 4px 0","margin:0 4px 3px 0").replace("font-size 9.6px","font-size:9.6px") for x in t)}</div></div>' for h,t in SK)
    p1=f"""
<div class="page" style="background:{BG};color:{INK}">
 <svg style="position:absolute;left:0;top:0" width="794" height="1123" viewBox="0 0 794 1123"><path d="{QC(794,0,262)}" fill="rgba(102,245,178,.16)"/></svg>
 {photo(300,left=446,top=75)}
 <div style="position:absolute;left:40px;top:36px;width:394px">
  <div class="kick" style="color:{INK3}">Product Designer · Fintech · AI-assisted · Bangalore</div>
  <div class="sg" style="font-size:52px;line-height:1;font-weight:700;margin-top:8px">Rakhesh</div>
  <div class="ser" style="font-size:60px;line-height:.95;color:{ACC};margin-top:2px">Karnati</div>
  <div style="margin-top:12px"><a class="pill" href="{PORT}" style="background:{ACC};color:{BG};font-weight:600">Portfolio ↗</a></div>
  <div style="margin-top:16px;font-size:11.3px;line-height:1.5;color:{INK2}">{SUMMARY}</div>
  <div style="margin-top:7px;font-size:11.3px;line-height:1.5;color:{INK2}">{SUMMARY2}</div>
 </div>
 <div style="position:absolute;left:40px;right:40px;top:396px;border-radius:22px;background:{CARD};padding:12px 22px">{stats(26,9.8,8,2)}</div>
 <div style="position:absolute;left:40px;right:40px;top:486px;bottom:76px;display:flex;gap:14px">
  <div style="width:47%;border-radius:22px;background:{CARD};padding:18px 18px">
   <div class="sg" style="font-size:19px;font-weight:700;margin-bottom:12px">Experience</div>
   {exp}
   <div class="sg" style="font-size:17px;font-weight:700;margin:20px 0 8px">Education</div>
   <div style="font-size:11px;line-height:1.45"><b>B.Tech, Mechanical Engineering (VBIT)</b><div style="color:{INK3}">Jawaharlal Nehru Technological University, Hyderabad</div></div>
   <div class="sg" style="font-size:17px;font-weight:700;margin:20px 0 8px">Certifications</div>
   <div style="font-size:11px;line-height:1.55"><b>Digital Skills:</b> <span style="color:{INK2}">User Experience</span><br><b>Enterprise Design Thinking</b> <span style="color:{INK2}">Practitioner</span></div>
  </div>
  <div style="flex:1;border-radius:22px;background:{CARD};padding:18px 18px">
   <div class="sg" style="font-size:19px;font-weight:700;margin-bottom:12px">Core Skills</div>
   {skills}
  </div>
 </div>
 <div style="position:absolute;left:40px;right:40px;bottom:20px">{contact_dark()}</div>
</div>"""
    def role(c,t,dt,sc,bl,cur=False):
        return f'<div style="margin-bottom:20px"><div style="display:flex;justify-content:space-between;align-items:flex-start"><div><div class="sg" style="font-size:17px;font-weight:700">{c}</div><div style="font-size:11.5px;font-weight:500;color:{LINK2};margin-top:1px">{t}</div></div><span class="tag" style="background:{"#0B8450" if cur else "#E4E9F0"};color:{"#fff" if cur else LINK2}">{dt}</span></div><div style="font-size:10.6px;font-style:italic;color:{LINK3};margin:6px 0 8px">{sc}</div>{bl}</div>'
    early=''.join(f'<div style="flex:1"><div class="sg" style="font-size:15px;font-weight:700">{c}</div><div style="font-size:11px;font-weight:500;color:{LINK2}">{t}</div><div style="margin:5px 0"><span class="tag" style="background:#E4E9F0;color:{LINK2}">{dt.replace(" to "," – ")}</span></div><div style="font-size:10.4px;color:{LINK3}">{d}</div></div>' for c,t,dt,d in EARLY)
    p2=f"""
<div class="page" style="background:{LBG}">
 <div style="padding:30px 46px 0;height:calc(1123px - 70px)">
  <div class="sg" style="font-size:26px;font-weight:700;margin-bottom:14px">Experience <span class="ser" style="color:{LACC};font-size:30px">details</span></div>
  {role('American Express','Sr. Associate, Product Designer','Jul 2024 – Present',AMEX_SCOPE,bullets(AMEX,10.8,5,LACC,LINK2),True)}
  {role('Saveo HealthTech Pvt. Ltd.','Product Designer','Feb 2022 – Feb 2024',SAVEO_SCOPE,bullets(SAVEO,10.8,5,LACC,LINK2))}
  <div style="display:flex;gap:24px;margin-bottom:20px;align-items:flex-start">{early}</div>
  <div><div class="sg" style="font-size:17px;font-weight:700;margin-bottom:8px">AI and built products</div>{bullets([f'<b style="color:{LINK}">{h}:</b> {t}' for h,t in AI_ITEMS],10.8,5,LACC,LINK2)}</div>
  <div style="font-size:9px;color:{LINK3};font-style:italic;margin-top:8px">{NOTE}</div>
 </div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:70px;background:{BG};color:{INK};padding:0 40px;display:flex;align-items:center"><div style="flex:1">{contact_dark(28)}</div></div>
</div>"""
    return f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{p1}{p2}</body></html>'
def one():
    amex=AMEX[:6]+[AMEX[7]]
    def role(c,t,dt,sc,bl):
        return f'<div style="display:flex;justify-content:space-between;align-items:center"><div><span class="sg" style="font-size:13.5px;font-weight:700">{c}</span> <span style="font-size:10.5px;font-weight:500;color:{LINK2}">· {t}</span></div><span class="tag" style="background:{LCARD2};color:{LINK2};font-size:8.5px">{dt}</span></div><div style="font-size:9.9px;font-style:italic;color:{LINK3};margin:2px 0 6px;line-height:1.35">{sc}</div>{bl}'
    left=f"""<div class="kick" style="color:{LACC};margin-bottom:8px">Experience</div>
{role('American Express','Sr. Associate, Product Designer','Jul 2024 – Present',AMEX_SCOPE,bullets(amex,10.1,4.2,LACC,LINK2))}
<div style="height:9px"></div>
{role('Saveo HealthTech Pvt. Ltd.','Product Designer','Feb 2022 – Feb 2024',SAVEO_SCOPE,bullets(SAVEO,10.1,4.2,LACC,LINK2))}
<div style="margin-top:11px;font-size:10px;color:{LINK2};line-height:1.45">"""+''.join(f'<div style="display:flex;justify-content:space-between;gap:8px;margin-bottom:2px"><div><b style="color:{LINK}">{c}</b> · {t}. {d}</div><div style="white-space:nowrap;color:{LINK3}">{dt.replace(" to "," – ")}</div></div>' for c,t,dt,d in EARLY)+f"""</div>
<div style="font-size:8.6px;color:{LINK3};font-style:italic;margin-top:6px">{NOTE}</div>"""
    right=f"""<div class="kick" style="color:{LACC};margin-bottom:8px">Core skills</div>
{''.join(f'<div style="margin-bottom:9px"><div class="sg" style="font-size:10.5px;font-weight:700;margin-bottom:3px">{h}</div><div>{"".join(f"<span class=chip style=\"background:{LCARD2};color:{LINK2};font-size:8.8px;padding:2.5px 7px;margin:0 3px 4px 0\">{x}</span>" for x in t)}</div></div>' for h,t in SK)}
<div class="kick" style="color:{LACC};margin:8px 0 5px">AI and built products</div>
{''.join(f'<div style="margin-bottom:3px;font-size:9.4px;color:{LINK2};line-height:1.4"><b style="color:{LINK}">{h}:</b> {t}</div>' for h,t in AI_ITEMS)}
<div class="kick" style="color:{LACC};margin:8px 0 4px">Education and certifications</div>
<div style="font-size:9.4px;color:{LINK2};line-height:1.4"><b style="color:{LINK}">B.Tech, Mechanical Engineering (VBIT)</b>, JNTU Hyderabad<br>{'<br>'.join(CERTS)}</div>"""
    pill=lambda ic_,t,u:f'<div style="display:flex;align-items:center;gap:6px;font-size:9.5px;color:{INK};white-space:nowrap">{circ(ic_,u,18)}<a href="{u}">{t}</a></div>'
    return f"""<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="page" style="background:{LBG}">
 <div style="position:absolute;left:0;right:0;top:0;height:298px;background:{BG};color:{INK}">
  <svg style="position:absolute;left:0;top:0" width="794" height="304" viewBox="0 0 794 304"><path d="{QC(794,0,200)}" fill="rgba(102,245,178,.16)"/></svg>
  {photo(190,right=30,top=34)}
  <div style="position:absolute;left:30px;top:30px;width:538px">
   <div class="kick" style="color:{INK3};font-size:9.5px">Product Designer · Fintech · AI-assisted · Bangalore</div>
   <div style="margin-top:6px;line-height:1"><span class="sg" style="font-size:42px;font-weight:700">Rakhesh </span><span class="ser" style="font-size:48px;color:{ACC}">Karnati</span></div>
   <div style="margin-top:10px;display:flex;gap:16px;flex-wrap:nowrap">{pill('phone',PHONE,'tel:+917036534813')}{pill('mail',EMAIL,'mailto:'+EMAIL)}{pill('globe','Portfolio',PORT)}{pill('in','LinkedIn',LI)}</div>
   <div style="margin-top:12px;font-size:10.2px;line-height:1.5;color:{INK2}">{SUMMARY} {SUMMARY2}</div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:14px;border-radius:18px;background:{CARD};padding:10px 16px">{stats(19,8.8,6,1)}</div>
 </div>
 <div style="position:absolute;left:0;right:0;top:298px;bottom:0;display:flex;padding:16px 30px 14px;gap:18px">
  <div style="width:58%">{left}</div>
  <div style="flex:1;border-left:1px solid #D9E0E8;padding-left:18px">{right}</div>
 </div>
</div></body></html>"""
open('one.html','w').write(one()); open('two.html','w').write(two())
