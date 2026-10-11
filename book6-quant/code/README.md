# Quant book code
Env: macOS, /usr/bin/python3. Pinned: numpy 2.0.2, pandas 2.3.3,
statsmodels 0.14.6, scipy 1.13.1, matplotlib 3.9.4 (all via `pip install --user`).
Data: `data/btc_daily.csv` is a pinned Kraken OHLC snapshot
(fetched 2026-10-11) so all printed outputs reproduce offline;
delete it to refetch live.
Tests: `bash test_01.sh`, `bash test_02.sh` — each greps the exact
numbers quoted in the chapters.
