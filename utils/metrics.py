
import numpy as np, pandas as pd

def sharpe(returns, rf=0.0):
    if len(returns)==0: return 0.0
    r = np.array(returns) - rf/252
    denom = np.std(r, ddof=1) if len(r)>1 else 1e-9
    return np.sqrt(252) * np.mean(r) / denom

def sortino(returns):
    if len(returns)==0: return 0.0
    r = np.array(returns)
    downside = r[r<0]
    denom = np.std(downside, ddof=1) if len(downside)>1 else 1e-9
    return np.sqrt(252) * np.mean(r) / denom

def max_drawdown(equity):
    if len(equity)==0: return 0.0
    eq = np.array(equity)
    run_max = np.maximum.accumulate(eq)
    dd = (eq - run_max) / run_max
    return float(dd.min())
