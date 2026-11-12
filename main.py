import os,json,urllib.request as Q
V=(0,100,320,330,500,900,0)
ND=(-33,-31,-18,-14,14,18,31,33);KD=(-17,-16,-15,-1,1,15,16,17)
BD=(-17,-15,15,17);RD=(-16,-1,1,16)
CM={0:13,7:14,4:12,112:7,119:11,116:3}
Z=120000;I=10**6
class TO(Exception):pass
def A(s,y):
 for t in(s-15*y,s-17*y):
  if not t&136 and B[t]==6+y:return 1
 for os,tg,sl in((ND,4,0),(KD,64,0),(BD,40,1),(RD,48,1)):
  for o in os:
   t=s+o
   while not t&136:
    p=B[t]
    if p!=6:
     if 1<<abs(p-6)&tg and(p-6)*y>0:return 1
     break
    if not sl:break
    t+=o
 return 0
def W(t):return A(KK[t],-S if t==(S<0)else S)
def G():
 ms=[];ap=ms.append;w=S>0
 def ad(s,t):
  if t>>4 in(0,7):
   for pr in(5,4,3,2):ap(s|t<<7|pr<<14)
  else:ap(s|t<<7)
 for s in PL:
  p=B[s]
  if(p>6)!=w:continue
  a=abs(p-6);r=s>>4
  if a==1:
   d=16*S;t=s+d
   if B[t]==6:
    ad(s,t)
    if(r==1 if w else r==6)and B[s+2*d]==6:ap(s|(s+2*d)<<7)
   for df in(-1,1):
    t=s+d+df
    if not t&136 and((B[t]-6 and(B[t]>6)!=w)or t==EP):ad(s,t)
  else:
   for o in(ND if a==2 else BD if a==3 else RD if a==4 else KD):
    t=s+o
    while not t&136:
     q=B[t]
     if q==6:ap(s|t<<7)
     else:
      if(q>6)!=w:ap(s|t<<7)
      break
     if a in(2,6):break
     t+=o
 k=4 if w else 116
 if B[k]==6+6*S and not A(k,-S):
  for bt,sg in((1,1),(2,-1))if w else((4,1),(8,-1)):
   if C&bt and B[k+sg]==6 and B[k+2*sg]==6 and not A(k+sg,-S)and not A(k+2*sg,-S)and(sg>0 or B[k+3*sg]==6):ap(k|(k+2*sg)<<7)
 return ms
def M(m):
 global S,C,EP
 sv=(B[:],S,C,EP,KK[:],PL.copy())
 f=m&127;t=m>>7&127;pr=m>>14&7;p=B[f]
 ie=1 if abs(p-6)==1 and t==EP and B[t]==6 and f&7!=t&7 else 0
 B[f]=6;PL.discard(f)
 if ie:B[t-16*S]=6;PL.discard(t-16*S)
 B[t]=6+pr*S if pr else p;PL.add(t)
 if abs(p-6)==6:
  KK[S<0]=t
  if abs(t-f)==2:u=f+3 if t>f else f-4;v=f+1 if t>f else f-1;rk=B[u];B[v]=rk;B[u]=6;PL.discard(u);PL.add(v)
 C&=CM.get(f,15)&CM.get(t,15)
 EP=f+16*S if abs(p-6)==1 and t-f==32*S else -1;S=-S
 return sv
def X(sv):
 global B,S,C,EP,PL
 B,S,C,EP,KK[:],PL=sv
def Y():
 s=0
 for i in PL:
  p=B[i]
  a=abs(p-6);f=i&7;r=i>>4
  if p<6:r=7-r
  c=min(f,7-f)+min(r,7-r)
  s+=(100+6*r,300+10*c,330,500,900,0)[a-1]*(1-(p<6)*2)
 return s
def O(ms):
 return sorted(ms,key=lambda m:-((V[abs(B[m>>7&127]-6)]<<5)-V[abs(B[m&127]-6)])*(B[m>>7&127]!=6))
def P(a,b,ply):
 global N
 N+=1
 if N>Z:raise TO
 ic=W(S<0)
 if ply>9 or(ply>5 and not ic):return S*Y()
 if not ic:
  st=S*Y()
  if st>=b:return b
  if st>a:a=st
 else:a=-I
 for m in G():
  if not ic and B[m>>7&127]==6 and not m>>14:continue
  sv=M(m)
  if W(S>0):X(sv);continue
  sc=-P(-b,-a,ply+1);X(sv)
  if sc>a:a=sc
  if a>=b:return b
 return a if a>-I else-I//10+ply
def D(d,a,b,ply):
 global N,BM
 if d<=0:return P(a,b,ply)
 N+=1
 if N>Z:raise TO
 ic=W(S<0);best=-I
 for m in O(G()):
  sv=M(m)
  if W(S>0):X(sv);continue
  sc=-D(d-1+(ic and ply<40),-b,-a,ply+1);X(sv)
  if sc>best:best=sc;bm=m
  if sc>a:a=sc
  if a>=b:break
 if best==-I:return-I//10+ply if ic else 0
 if ply==0:BM=bm
 return best
def F():
 global N,BM
 N=0;ms=[]
 for m in O(G()):sv=M(m);ms.append(m)if not W(S>0)else 0;X(sv)
 BM=ms[0]
 try:
  d=1
  while 1:D(d,-I,I,0);d+=1
 except TO:pass
 return BM
def L(x):
 global B,S,C,EP,PL,KK
 B=[6]*128;PL=set();KK=[0,0]
 w=x.split();sq=112
 for ch in w[0]:
  if ch=='/':sq-=24
  elif ch.isdigit():sq+=int(ch)
  else:
   p='pnbrqk'.find(ch.lower())+1
   if ch.islower():p=-p
   B[sq]=6+p;PL.add(sq)
   if abs(p)==6:KK[p<0]=sq
   sq+=1
 S=1-(w[1]=='b')*2;C=('K'in w[2])|('Q'in w[2])<<1|('k'in w[2])<<2|('q'in w[2])<<3;EP=-1
def J(p,d):return json.loads(Q.urlopen(Q.Request(E+p,json.dumps(d).encode(),{'Content-Type':'application/json'})).read())
if __name__=='__main__':
 E=os.environ['MAKEFUN_ENV_URL']
 while 1:
  g=J('/game',{})
  if g.get('status')=='done':break
  while g['status']=='your_move':
   L(g['start_fen']);[M((int(u[1])-1)*16+ord(u[0])-97|((int(u[3])-1)*16+ord(u[2])-97)<<7|(('nbrq'.find(u[4])+2 if len(u)>4 else 0)<<14))for u in g['moves']];m=F();g=J('/move',{'game':g['game'],'move':chr(97+(m&7))+str(1+(m>>4&7))+chr(97+(m>>7&7))+str(1+(m>>11&7))+('nbrq'[(m>>14&7)-2]if m>>14 else '')})
