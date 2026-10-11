# make        -> builds main.pdf (pdflatex x3 + makeindex)
# make figures-> regenerates Python figures into figures/
# make test   -> runs every code example in code/
MAIN=main
all:
	pdflatex -interaction=nonstopmode $(MAIN).tex
	pdflatex -interaction=nonstopmode $(MAIN).tex
	makeindex $(MAIN)
	pdflatex -interaction=nonstopmode $(MAIN).tex
	@echo "--- Overfull boxes > 3pt:"; grep -E "Overfull .hbox \(([3-9]|[1-9][0-9]+)\." $(MAIN).log || echo none
	@echo "--- Undefined refs/cites:"; grep -iE "undefined" $(MAIN).log || echo none
figures:
	@for f in figures/*.py; do [ -e "$$f" ] && python3 "$$f"; done; true
test:
	@for f in code/test_*.sh; do [ -e "$$f" ] && sh "$$f"; done; echo "tests done"
clean:
	rm -f *.aux *.log *.toc *.idx *.ind *.ilg *.out *.lof *.lot
