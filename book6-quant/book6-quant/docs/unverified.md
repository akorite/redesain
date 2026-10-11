# Unverified claims
| Claim | Where | Why unverified |
|---|---|---|
| Kraken public OHLC endpoint live + free of auth | ch01 (kraken_daily.py, Notes, FR) | Verified 2026-10-11; availability from any venue in Indonesia is unverified — re-check at use |
| Parkinson/GARCH microstructure bias on synthetic h,l | ch01 §1.3 | Synthetic ranges are wider than true GBM microstructure → Parkinson biased high pre-switch (0.389 vs 0.300); flagged in text |

## Publisher links that return 403 to curl (checked 2026-10-11)
These resolve in a browser but refuse automated fetches -- logged, not removed:
- ch09 Gelman & Loken "garden of forking paths": statmodeling.stat.columbia.edu (403 to curl)
- ch10 Cartea et al., Algorithmic and High-Frequency Trading: cambridge.org/9781107091146 (403 to curl; the /core/books/... path 404'd and was replaced)
- ch10 Almgren & Chriss optimal execution: math.nyu.edu/~chriss/optimal.htm (403 to curl)
- ch13 MacLean, Thorp & Ziemba Kelly volume: worldscientific.com/worldscibooks/10.1142/7598 (403 to curl)
- ch14 McNeil/Frey/Embrechts QRM: press.princeton.edu .../9780691166278/... (403 to curl)
- ch15 Gardner "Three Data Revolutions": tandfonline.com/doi/full/10.1080/00031305.2023.2284320 (403 to curl)
- ch14 Hull RMFI: wiley product page 404'd; citation converted to ISBN-only per review.
