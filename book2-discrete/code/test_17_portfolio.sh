#!/bin/bash
set -e
cd "$(dirname "$0")"
out=$(python3 portfolio_check.py)
echo "$out" | grep -F "good_proof.tex: OK" >/dev/null
echo "$out" | grep -F "missing:" >/dev/null
echo PASS
