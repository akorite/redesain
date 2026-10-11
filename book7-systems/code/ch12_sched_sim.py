# ch12_sched_sim.py -- FIFO/SJF/STCF/MLFQ turnaround + response sim.
jobs=[("A",0,100),("B",10,30),("C",20,10),("D",30,60)]
def run(pol):
    t=0; done={}; first={}; rem={n:e for n,a,e in jobs}
    arrived=set(); 
    timeline=[]
    while len(done)<len(jobs):
        ready=[(a,e,n) for n,a,e in jobs if a<=t and n not in done and n not in arrived or (a<=t and n not in done)]
        ready=[(a,e,n) for n,a,e in jobs if a<=t and n not in done]
        if not ready:
            t=min(a for n,a,e in jobs if a>t and n not in done); continue
        if pol=="fifo": key=lambda r:r[0]
        elif pol=="sjf": key=lambda r:r[1]
        else: key=lambda r:rem[r[2]]          # stcf: shortest remaining
        a,e,n=min(ready,key=key)
        if n not in first: first[n]=t
        timeline.append(n)
        if pol=="stcf":
            rem[n]-=1; t+=1
            if rem[n]==0: done[n]=t
        else:
            t=a+e if t<a else t+e; done[n]=t; rem[n]=0
    tat=sum(done[n]-a for n,a,e in jobs)/len(jobs)
    resp=sum(first[n]-a for n,a,e in jobs)/len(jobs)
    return tat,resp,"".join(dict.fromkeys(timeline))
for pol in ["fifo","sjf","stcf"]:
    tat,resp,tl=run(pol)
    print(f"{pol:5s} turnaround={tat:5.1f}  response={resp:5.1f}  order={tl}")
