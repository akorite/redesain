#!/usr/bin/env bash
# ch02 regression: every printed output must reproduce.
set -e
cd "$(dirname "$0")"
python3 simulate_ts.py | grep -q "random walk : mean=+7.883 sd=9.361"
python3 simulate_ts.py | grep -q "OU theta.12 : mean=+4.011 sd=0.729"
python3 adf_demo.py | grep -q "random walk  ADF= -0.349  p=0.9182"
python3 adf_demo.py | grep -q "coint sprd z ADF= -5.371"
python3 adf_demo.py | grep -q "seed 11: ADF=-3.979 p=0.002 stationary"
python3 ljung_box.py | grep -q "LB(10)=1385.33"
python3 ljung_box.py | grep -q "LB(10)=   5.05"
python3 ou_halflife.py | grep -q "hl= 15.6"
python3 ou_halflife.py | grep -q "hl=  2.4"
python3 btc_stationarity.py | grep -q "ADF= -1.822 p=0.3697"
python3 btc_stationarity.py | grep -q "ADF=-18.535 p=0.0000"
echo "ALL ch02 CHECKS PASS"
