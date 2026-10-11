#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 invariant_sim.py | grep -F "survivor = 6"
echo PASS
