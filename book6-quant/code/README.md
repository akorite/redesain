# Code
- Python 3.9+ (dev box: 3.9.6), numpy 2.0.2, pandas 2.3.3, matplotlib 3.9.4 — `python3 -m pip install --user numpy pandas matplotlib`
- Market-data pulls go in code/data/ with a note on source + access date; synthetic generators carry a seed.
- `make test` runs code/test_*.sh; the harness's look-ahead tests MUST fail by design.
