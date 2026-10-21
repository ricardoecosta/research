#!/bin/bash
set -euo pipefail
cd /Users/ricardo/hustling
/usr/bin/python3 research/koerner-office/scripts/fetch_freetranscript.py "${1:-20}"
