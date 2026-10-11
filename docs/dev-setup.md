# Dev environment recipe (macOS)
# TinyTeX + packages lifeos.sty needs
curl -sL https://yihui.org/tinytex/install-bin-unix.sh | sh
$HOME/Library/TinyTeX/bin/universal-darwin/tlmgr install collection-latexextra collection-pictures collection-fontsrecommended makeindex psnfss
export PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"
# pdfinfo + verilog/spice for electronics + systems testbenches
brew install poppler icarus-verilog ngspice
python3 -m pip install --user numpy matplotlib
# Build a book: cd bookN-<slug> && make ; test a chapter: cd bookN-<slug>/code && bash test_chNN.sh
