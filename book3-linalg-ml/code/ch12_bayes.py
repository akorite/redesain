# medical test: prevalence 0.1%, sensitivity 99%, specificity 95%
prev, sens, spec = 0.001, 0.99, 0.95
num = sens * prev
den = num + (1 - spec) * (1 - prev)
print("P(sick|+)= %.4f/%.4f = %.4f" % (num, den, num/den))
# second test given positive: independent conditional on truth
prev2 = num/den
num2 = sens*prev2; den2 = num2 + (1-spec)*(1-prev2)
print("after 2nd +: %.4f" % (num2/den2))
# what specificity would push first test past 50%?
for s in [0.95,0.98,0.99,0.999]:
    d = sens*prev + (1-s)*(1-prev)
    print(f"spec={s}: P(sick|+) = {sens*prev/d:.4f}")
