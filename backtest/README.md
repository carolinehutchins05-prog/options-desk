# Backtest of the Options Desk screen against the S&P 500

`run_backtest.py` reads daily prices (a pickle of a yfinance download of the current S&P 500 plus SPY, adjusted, from 2015-06-01) and writes `results.json`.
The rules and the known biases are documented at the top of the script. Option prices are modeled with Black Scholes because no free source has historical chains.
Write-up: https://carolinehutchins05-prog.github.io/options-desk/research/backtest.html
