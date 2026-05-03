import os
import sys

# Prepend our parent directory to the system's path so we can load
# the "modules" in this project:
_parent_dp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Stocks_predictor'))
_src_dp = _parent_dp
sys.path.insert(0, _src_dp)