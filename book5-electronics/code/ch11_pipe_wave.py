# parse the pipe_tb $monitor rows -> pgfplots .dat
import re
rows=[]
for line in open("ch11_pipe.out"):
    m=re.match(r"t=\s*(\d+) clk=(\w) d=(\w) \| q_nb=(\w) q_block=(\w)",line)
    if m:
        t,c,d,qn,qb=m.groups()
        cv=lambda v:{'x':0,'0':0,'1':1}[v]
        rows.append((int(t),cv(c),cv(d),cv(qn),cv(qb)))
with open("../figures/ch11/ch11_pipe.dat","w") as f:
    f.write("t clk d qnb qb\n")
    for r in rows: f.write("%d %d %d %d %d\n"%r)
print(len(rows),"rows")
