# mockllm.py -- a scripted stand-in for an API LLM, so every listing
# in this chapter runs offline. The behaviours it mimics are real:
# it follows format instructions, degrades on compound prompts, and
# can be made to fail on demand. Swap this for a client call and the
# harnesses work unchanged.
import re

class MockLLM:
    def __init__(self, quality='good', latency=0.05):
        self.calls = 0
        self.quality = quality
        self.latency = latency

    def __call__(self, system, user):
        self.calls += 1
        # --- 'extract': pull numbers/entities out of a blob ---
        if system.startswith('extract'):
            nums = re.findall(r'[-+]?\d+\.?\d*', user)
            return 'EXTRACTED: ' + ','.join(nums)
        # --- 'answer': answer a question from extracted facts ---
        if system.startswith('answer'):
            m = re.findall(r'[-+]?\d+\.?\d*', user)
            return f'ANSWER: based on {m[-1] if m else "?"}'
        # --- monolith: one shot at the whole task ---
        if system.startswith('monolith'):
            if self.quality == 'good':
                nums = re.findall(r'[-+]?\d+\.?\d*', user)
                return f'ANSWER: the value is {float(nums[0])*2 if nums else "?"}'
            return 'ANSWER: I am unsure, the text contains many numbers'
        # --- react brain: choose tool by where we are in the trace ---
        if 'TOOLS:' in system:
            if 'result was 37.5' in user or 'have the total' in user:
                return 'Thought: have the total\nFinal: 37.50'
            if 'result was' in user:
                return 'Thought: have price 12.50; compute 3*12.50\nAction: calc(3*12.50)'
            if 'cost of 3 items' in user or 'total' in user:
                return 'Thought: need the unit price first\nAction: search(unit price)'
            return 'Thought: unsure\nFinal: cannot determine'
        return 'OK'
