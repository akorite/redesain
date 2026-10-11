# react_minimal.py -- a minimal ReAct agent in ~60 lines:
# Thought -> Action -> Observation loop with two tools
# (calculator, mock search) and a full trace dump.
# A second run injects a tool error to show the failure loop.
import re, sys, json; sys.path.insert(0, '.')
from mockllm import MockLLM

def tool_search(q):
    data = {'unit price': '12.50', 'discount': '10%'}
    return data.get(q.lower(), f'no result for {q!r}')

def tool_calc(expr):
    try:
        return str(eval(re.sub(r'[^0-9+\-*/.() ]', '', expr)))
    except Exception as e:
        return f'CALC_ERROR: {e}'

TOOLS = {'search': tool_search, 'calc': tool_calc}
SYSTEM = ('You are a ReAct agent. TOOLS: search(q), calc(expr). '
          'Reply Thought/Action or Thought/Final.')

def run(task, llm, inject_error=False, max_steps=8):
    trace, ctx, seen = [], task, set()
    for step in range(max_steps):
        out = llm(SYSTEM, ctx)
        trace.append(f'[{step}] {out}')
        if inject_error and 'search' in out:
            trace.append(f'[{step}] OBS: TOOL_ERROR timeout')
            ctx += '\nservice unavailable, retry'
            continue
        m = re.search(r'Action: (\w+)\((.*?)\)', out)
        if m:
            name, arg = m.group(1), m.group(2)
            key = (name, arg)
            if key in seen:
                trace.append(f'[{step}] OBS: loop detected, aborting')
                return trace, 'LOOP'
            seen.add(key)
            res = TOOLS[name](arg) if name in TOOLS else 'NO_TOOL'
            trace.append(f'[{step}] OBS: {res}')
            ctx += f'\nresult was {res}; cost of 3 items?'
        elif 'Final:' in out:
            return trace, out.split('Final:')[1].strip()
        else:
            ctx += '\ncontinue'
    return trace, 'MAX_STEPS'

llm = MockLLM()
tr, ans = run('cost of 3 items at unit price?', llm)
print('=== SUCCESS TRACE ===')
print('\n'.join(tr)); print('=>', ans)

tr2, ans2 = run('cost of 3 items at unit price?', llm,
                    inject_error=True)
print('\n=== FAILURE TRACE (tool error injected) ===')
print('\n'.join(tr2)); print('=>', ans2)
json.dump({'success': tr, 'failure': tr2},
            open('/tmp/react_traces.json', 'w'))
