from pathlib import Path
from xml.etree import ElementTree as ET
import html, textwrap
DIR=Path(__file__).resolve().parents[1]/'assets'/'diagramme';DIR.mkdir(parents=True,exist_ok=True)
# node tuple (name,type,text,x,y,width,height) ; edge tuple (start,end,label, via optional points)
D={
'loesung-nachbauen':(
[('s','start','Anfrage eingegangen',35,120,85,85),('a','task','Anfrage erfassen',200,126,155,68),('b','task','Kundendaten prüfen',430,126,175,68),('e','end','Anfrage erfasst',695,120,85,85)],
[('s','a',''),('a','b',''),('b','e','')],(830,330)),
'aufgabe-fehler':(
[('s','end','Bestellung eingegangen',40,230,90,90),('a','start','Druckmotiv prüfen',235,230,90,90),('g','task','Motiv geeignet?',435,230,160,73),('ja','task','Druckauftrag anlegen',680,110,172,72),('nein','task','Ablehnung versenden',680,330,172,72),('ej','end','Auftrag angelegt',955,105,95,95),('en','end','Bestellung abgelehnt',955,325,95,95)],
[('s','a',''),('a','g',''),('g','ja',''),('g','nein',''),('ja','ej',''),('nein','en','')],(1120,510)),
'loesung-fehler':(
[('s','start','Bestellung eingegangen',40,230,90,90),('a','task','Druckmotiv prüfen',230,240,165,72),('g','xor','Motiv geeignet?',495,233,90,90),('ja','task','Druckauftrag anlegen',685,100,170,72),('nein','task','Ablehnung versenden',685,350,170,72),('ej','end','Auftrag angelegt',973,93,90,90),('en','end','Bestellung abgelehnt',973,345,90,90)],
[('s','a',''),('a','g',''),('g','ja','Ja'),('g','nein','Nein'),('ja','ej',''),('nein','en','')],(1140,515)),
'loesung-eigen':(
[('s','start','Bestellung eingegangen',25,265,90,90),('a','task','Bestelldaten prüfen',190,275,150,70),('g1','xor','Vollständig?',410,265,90,90),('a2','task','Motiv prüfen',605,275,140,70),('g2','xor','Geeignet?',825,265,90,90),('accept','task','Druckauftrag anlegen',1015,115,160,70),('reject1','task','Ablehnung versenden',610,455,160,70),('reject2','task','Ablehnung versenden',1015,455,160,70),('end1','end','Druckauftrag angelegt',1240,107,90,90),('end2','end','Bestellung abgelehnt',840,447,90,90),('end3','end','Bestellung abgelehnt',1240,447,90,90)],
[('s','a',''),('a','g1',''),('g1','a2','Ja'),('g1','reject1','Nein'),('reject1','end2',''),('a2','g2',''),('g2','accept','Ja'),('g2','reject2','Nein'),('accept','end1',''),('reject2','end3','')],(1380,640))
}

def svg(name,nodes,edges,wh):
 W,H=wh; parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="BPMN-Diagramm {html.escape(name)}">','<defs><marker id="ar" markerWidth="10" markerHeight="8" refX="8" refY="4" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,4 L0,8 Z" fill="#344567"/></marker></defs>',f'<rect width="{W}" height="{H}" fill="#f7f9ff" rx="18"/>']
 pos={i:(typ,x,y,w,h) for i,typ,txt,x,y,w,h in nodes}
 for s,t,label in edges:
  _,x1,y1,w1,h1=pos[s];_,x2,y2,w2,h2=pos[t];
  if x2>x1+w1-10:
   p1=(x1+w1,y1+h1/2);p2=(x2,y2+h2/2)
   mid=(p1[0]+p2[0])/2
   d=f'M{p1[0]} {p1[1]} H{mid} V{p2[1]} H{p2[0]-3}'
  elif y2>y1:
   p1=(x1+w1/2,y1+h1);p2=(x2+w2/2,y2);d=f'M{p1[0]} {p1[1]} V{(p1[1]+p2[1])/2} H{p2[0]} V{p2[1]-3}'
  else:
   p1=(x1+w1/2,y1);p2=(x2+w2/2,y2+h2);d=f'M{p1[0]} {p1[1]} V{(p1[1]+p2[1])/2} H{p2[0]} V{p2[1]+3}'
  parts.append(f'<path d="{d}" fill="none" stroke="#344567" stroke-width="3" marker-end="url(#ar)" stroke-linejoin="round"/>')
  if label:
   lx=(p1[0]+p2[0])/2;ly=(p1[1]+p2[1])/2-8
   parts.append(f'<rect x="{lx-27}" y="{ly-17}" width="54" height="25" rx="9" fill="#ffffff" stroke="#cdd7ed"/><text x="{lx}" y="{ly}" text-anchor="middle" font-size="15" font-weight="700" fill="#344567">{html.escape(label)}</text>')
 for i,typ,txt,x,y,w,h in nodes:
  cx=x+w/2;cy=y+h/2
  if typ in ['start','end']:
   parts.append(f'<circle cx="{cx}" cy="{cy}" r="{min(w,h)/2-8}" stroke="#192845" stroke-width="{6 if typ=="end" else 2.5}" fill="#fff"/>')
  elif typ=='task':
   parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" stroke="#192845" stroke-width="2.5"/>')
  else:
   parts.append(f'<path d="M{cx} {y+3} L{x+w-3} {cy} L{cx} {y+h-3} L{x+3} {cy}Z" fill="#fff" stroke="#192845" stroke-width="2.5"/>')
   parts.append(f'<path d="M{cx-12} {cy-12} L{cx+12} {cy+12} M{cx+12} {cy-12} L{cx-12} {cy+12}" stroke="#192845" stroke-width="3.5"/>')
  if typ not in ['start','end','xor']:
   bits=textwrap.wrap(txt,width=21,break_long_words=False)
   for n,line in enumerate(bits):parts.append(f'<text x="{cx}" y="{cy+(n-(len(bits)-1)/2)*18+5}" text-anchor="middle" font-size="15" font-family="Arial, sans-serif" fill="#15243f">{html.escape(line)}</text>')
  else:
   below=y+h+22 if typ!='xor' else y+h+20
   bits=textwrap.wrap(txt,width=21,break_long_words=False)
   for n,line in enumerate(bits):parts.append(f'<text x="{cx}" y="{below+n*17}" text-anchor="middle" font-size="14" font-family="Arial, sans-serif" fill="#2c3d5c">{html.escape(line)}</text>')
 parts.append('</svg>');return '\n'.join(parts)

def drawio(name,nodes,edges,wh):
 mx=ET.Element('mxfile',host='app.diagrams.net',modified='2026-11-24T08:00:00.000Z',agent='BPMN-Labor',version='24.7.17',type='device')
 diagram=ET.SubElement(mx,'diagram',id=name,name='BPMN')
 model=ET.SubElement(diagram,'mxGraphModel',dx='1300',dy='700',grid='1',gridSize='10',guides='1',tooltips='1',connect='1',arrows='1',fold='1',page='1',pageScale='1',pageWidth=str(wh[0]),pageHeight=str(wh[1]),math='0',shadow='0')
 root=ET.SubElement(model,'root');ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
 for i,typ,txt,x,y,w,h in nodes:
  sty= {'start':'ellipse;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#ffffff;strokeColor=#192845;', 'end':'ellipse;whiteSpace=wrap;html=1;strokeWidth=6;fillColor=#ffffff;strokeColor=#192845;', 'task':'rounded=1;arcSize=15;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#ffffff;strokeColor=#192845;', 'xor':'rhombus;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#ffffff;strokeColor=#192845;'}[typ]
  label=txt if typ=='task' else ('X' if typ=='xor' else '')
  cell=ET.SubElement(root,'mxCell',id=i,value=label,style=sty,vertex='1',parent='1');ET.SubElement(cell,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
  if typ!='task':
   labelcell=ET.SubElement(root,'mxCell',id='label-'+i,value=txt,style='text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;strokeColor=none;fillColor=none;',vertex='1',parent='1');ET.SubElement(labelcell,'mxGeometry',x=str(x-25),y=str(y+h+5),width=str(w+50),height='40',attrib={'as':'geometry'})
 for n,(s,t,label) in enumerate(edges):
  c=ET.SubElement(root,'mxCell',id='edge-'+str(n),value=label,style='edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;strokeColor=#344567;fontColor=#1f3556;labelBackgroundColor=#ffffff;',edge='1',parent='1',source=s,target=t)
  ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
 return ET.tostring(mx,encoding='unicode',xml_declaration=True)

for name,(n,e,wh) in D.items():
 (DIR/(name+'.svg')).write_text(svg(name,n,e,wh),encoding='utf-8')
 (DIR/(name+'.drawio')).write_text(drawio(name,n,e,wh),encoding='utf-8')
# Aufgabe nachbauen: zum Nachbauen dieselbe Grafik wie Muster, aber in der Aufgabenstellung erkennbar.
for ext in ('svg','drawio'):
 (DIR/('aufgabe-nachbauen.'+ext)).write_text((DIR/('loesung-nachbauen.'+ext)).read_text(encoding='utf-8'),encoding='utf-8')
try:
 import cairosvg
 for p in DIR.glob('*.svg'):
  cairosvg.svg2png(url=str(p),write_to=str(p.with_suffix('.png')),output_width=1100)
except Exception as e: print('PNG optional:',e)
print('Diagrams',len(list(DIR.iterdir())))
