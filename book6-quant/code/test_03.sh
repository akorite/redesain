#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 lob.py | grep -q "after sell 5@99.5: \[(100.0, 4, 's'), (99.5, 1, 's')\]"
python3 walk_book.py | grep -q "filled 9 at avg 101.1111"
python3 walk_book.py | grep -q "slippage = +0.8611/unit = +0.859%"
python3 microprice.py | grep -q "microprice=100.0455"
python3 mm_game.py | grep -q "informed share 0.9: mean MM PnL    +39.17"
python3 mm_game.py | grep -q "per informed trade -0.019"
python3 trades_to_candles.py | grep -q "t=1791739020 n=132 o=83812.8 h=83846.6 l=83812.7 c=83843.4"
python3 trades_to_candles.py | grep -q "t=1791739020 o=83812.8 h=83846.6 l=83812.7 c=83843.4"
echo "ALL ch03 CHECKS PASS"
