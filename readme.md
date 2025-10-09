### Opsett

Teknologi

#### scoop
Pakkeinstallering på windows:

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

#### uv, git og python


``` scoop install git python uv ```

### Opprett isolert miljø med uv

` uv venv .venv ` 

Activate with: ` .venv\Scripts\activate `

### Installer grunnpakker (via uv)
` uv pip install pandas matplotlib yfinance `


## VSCode
 
Sørg for at VSCode bruker det rette miljøet: 
` Ctrl + Shift + P → Python: Select Interpreter → trading_lab\.venv `

Vi trenger følgende extensions:
- Python (Microsoft)
- Pylance
- Jupyter (for notebooks)


## Git

### Github

git remote add origin git@github.com:espenhoh/sigmabott.git


## Kjør prosjekt

` uv run src/test_env.py `


## Studie

Dag 1: [candlestick-charting-what-is-it](https://www.investopedia.com/trading/candlestick-charting-what-is-it/)