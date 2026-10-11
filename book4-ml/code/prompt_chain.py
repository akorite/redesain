# prompt_chain.py -- two-step chain (extract -> answer) vs one
# monolithic prompt, on the mock LLM: quality + call-count comparison.
import sys; sys.path.insert(0, '.')
from mockllm import MockLLM

DOC = ("Our Q3 report shows revenue of 41.2M, up from 38.7M in Q2, "
       "with churn holding at 4.5% and support tickets at 1,204.")
Q = 'what was the revenue in Q3?'

def chain(llm, doc, question):
    ext = llm('extract all numeric values', doc)
    ans = llm('answer the question using the extracted facts',
              f'{ext}\nQ: {question}')
    return ans, ext

def monolith(llm, doc, question):
    return llm('monolith: answer the question in one pass',
               f'{doc}\nQ: {question}')

for quality in ('good', 'weak'):
    llm_c, llm_m = MockLLM(quality), MockLLM(quality)
    a, ext = chain(llm_c, DOC, Q)
    b = monolith(llm_m, DOC, Q)
    print(f'[{quality}] chain   ({llm_c.calls} calls): {a}')
    print(f'[{quality}]  extract step saw: {ext}')
    print(f'[{quality}] monolith({llm_m.calls} call ): {b}')
    print()

print('chain = 2 calls, monolith = 1; control vs latency')
