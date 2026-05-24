from db_config import create_connection

# ---------- Default Nifty50 Companies ----------
DEFAULT_COMPANIES = [
    ("Reliance Industries",                 "RELIANCE.NS"),
    ("HDFC Bank",                           "HDFCBANK.NS"),
    ("Tata Consultancy Services",           "TCS.NS"),
    ("Bharti Airtel",                       "BHARTIARTL.NS"),
    ("ICICI Bank",                          "ICICIBANK.NS"),
    ("State Bank of India",                 "SBIN.NS"),
    ("Infosys",                             "INFY.NS"),
    ("Hindustan Unilever",                  "HINDUNILVR.NS"),
    ("Life Insurance Corporation of India", "LICI.NS"),
    ("Bajaj Finance",                       "BAJFINANCE.NS"),
    ("ITC",                                 "ITC.NS"),
    ("Larsen & Toubro",                     "LT.NS"),
    ("Maruti Suzuki India",                 "MARUTI.NS"),
    ("HCL Technologies",                    "HCLTECH.NS"),
    ("Sun Pharmaceutical",                  "SUNPHARMA.NS"),
    ("Kotak Mahindra Bank",                 "KOTAKBANK.NS"),
    ("Mahindra & Mahindra",                 "M&M.NS"),
    ("UltraTech Cement",                    "ULTRACEMCO.NS"),
    ("Axis Bank",                           "AXISBANK.NS"),
    ("NTPC Limited",                        "NTPC.NS"),
    ("Titan Company",                       "TITAN.NS"),
    ("Bajaj Finserv",                       "BAJAJFINSV.NS"),
    ("Hindustan Aeronautics",               "HAL.NS"),
    ("Oil & Natural Gas",                   "ONGC.NS"),
    ("Adani Ports & SEZ",                   "ADANIPORTS.NS"),
    ("Bharat Electronics",                  "BEL.NS"),
    ("Wipro",                               "WIPRO.NS"),
    ("JSW Steel",                           "JSWSTEEL.NS"),
    ("Tata Motors",                         "TATAMOTORS.NS"),
    ("Asian Paints",                        "ASIANPAINT.NS"),
    ("Coal India",                          "COALINDIA.NS"),
    ("Nestlé India",                        "NESTLEIND.NS"),
    ("Grasim Industries",                   "GRASIM.NS"),
    ("Hindalco Industries",                 "HINDALCO.NS"),
    ("Tata Steel",                          "TATASTEEL.NS"),
    ("Ambuja Cement",                       "AMBUJACEM.NS"),
]

# This Nifty50 list was compiled by Copilot on 21 April 2026.
# It contains the top 50 companies by market capitalization on the NSE as of that date.
#
#  Here is the full, clean, complete list of all 50 Nifty 50 companies ordered by market capitalization, using:
#  Yahoo Finance market‑cap data where available
#  NSE India market‑cap data for the remaining companies
#  Clear marking of inferred (non‑Yahoo) entries
#  This gives you a fully ranked list, largest → smallest, in CSV format.
NIFTY50 = [
    ("Reliance Industries", "RELIANCE.NS"),
    ("HDFC Bank", "HDFCBANK.NS"),
    ("ICICI Bank", "ICICIBANK.NS"),
    ("Infosys", "INFY.NS"),
    ("Tata Consultancy Services", "TCS.NS"),
    ("State Bank of India", "SBIN.NS"),
    ("Bharti Airtel", "BHARTIARTL.NS"),
    ("Larsen & Toubro", "LT.NS"),
    ("ITC", "ITC.NS"),
    ("Hindustan Unilever", "HINDUNILVR.NS"),
    ("Bajaj Finance", "BAJFINANCE.NS"),
    ("Kotak Mahindra Bank", "KOTAKBANK.NS"),
    ("Adani Enterprises", "ADANIENT.NS"),
    ("Adani Ports", "ADANIPORTS.NS"),
    ("NTPC", "NTPC.NS"),
    ("Power Grid", "POWERGRID.NS"),
    ("Tata Motors", "TATAMOTORS.NS"),
    ("Maruti Suzuki", "MARUTI.NS"),
    ("UltraTech Cement", "ULTRACEMCO.NS"),
    ("JSW Steel", "JSWSTEEL.NS"),
    ("Tata Steel", "TATASTEEL.NS"),
    ("Mahindra & Mahindra", "M&M.NS"),
    ("Sun Pharma", "SUNPHARMA.NS"),
    ("HCL Technologies", "HCLTECH.NS"),
    ("Wipro", "WIPRO.NS"),
    ("Axis Bank", "AXISBANK.NS"),
    ("IndusInd Bank", "INDUSINDBK.NS"),
    ("Bajaj Finserv", "BAJAJFINSV.NS"),
    ("Bajaj Auto", "BAJAJ-AUTO.NS"),
    ("Nestle India", "NESTLEIND.NS"),
    ("Cipla", "CIPLA.NS"),
    ("Dr Reddy's Laboratories", "DRREDDY.NS"),
    ("Coal India", "COALINDIA.NS"),
    ("Hindalco Industries", "HINDALCO.NS"),
    ("Grasim Industries", "GRASIM.NS"),
    ("Titan Company", "TITAN.NS"),
    ("Tata Consumer Products", "TATACONSUM.NS"),
    ("Eicher Motors", "EICHERMOT.NS"),
    ("Hero MotoCorp", "HEROMOTOCO.NS"),
    ("Apollo Hospitals", "APOLLOHOSP.NS"),
    ("UPL", "UPL.NS"),
    ("Divi's Laboratories", "DIVISLAB.NS"),
    ("SBI Life Insurance", "SBILIFE.NS"),
    ("HDFC Life Insurance", "HDFCLIFE.NS"),
    ("Tech Mahindra", "TECHM.NS"),
    ("Britannia Industries", "BRITANNIA.NS"),
    ("JSW Energy", "JSWENERGY.NS"),
    ("Tata Power", "TATAPOWER.NS"),
    ("Bharat Electronics", "BEL.NS")
]

# All index symbols and names below come directly from Yahoo Finance’s World Indices page. 
# This list was compiled by Copilot on 21 April 2026.
MAJOR_GLOBAL_INDICES = [
    ("S&P 500", "^GSPC"),
    ("Dow Jones Industrial Average", "^DJI"),
    ("NASDAQ Composite", "^IXIC"),
    ("NYSE Composite", "^NYA"),
    ("NYSE American Composite", "^XAX"),
    ("Cboe UK 100", "^BUK100P"),
    ("Russell 2000", "^RUT"),
    ("CBOE Volatility Index (VIX)", "^VIX"),
    ("FTSE 100", "^FTSE"),
    ("DAX", "^GDAXI"),
    ("CAC 40", "^FCHI"),
    ("EURO STOXX 50", "^STOXX50E"),
    ("Euronext 100", "^N100"),
    ("BEL 20", "^BFX"),
    ("MOEX Russia Index", "MOEX.ME"),
    ("Hang Seng Index", "^HSI"),
    ("STI Index (Singapore)", "^STI"),
    ("S&P/ASX 200", "^AXJO"),
    ("All Ordinaries", "^AORD"),
    ("S&P BSE Sensex", "^BSESN"),
    ("IDX Composite (Jakarta)", "^JKSE"),
    ("FTSE Bursa Malaysia KLCI", "^KLSE"),
    ("S&P/NZX 50", "^NZ50"),
    ("KOSPI Composite", "^KS11"),
    ("Taiwan Weighted Index", "^TWII"),
    ("S&P/TSX Composite", "^GSPTSE"),
    ("IBOVESPA (Brazil)", "^BVSP")
]

# Major Global Currencies
# This list was compiled by Copilot on 21 April 2026, based on the most commonly traded currency pairs in the forex market, as 
# well as some important cross pairs and emerging market majors. The ticker symbols are in Yahoo Finance format.
MAJOR_GLOBAL_CURRENCIES = [
    ("EUR/USD", "EURUSD=X"),
    ("USD/JPY", "JPY=X"),
    ("GBP/USD", "GBPUSD=X"),
    ("USD/CHF", "CHF=X"),
    ("USD/CAD", "CAD=X"),
    ("AUD/USD", "AUDUSD=X"),
    ("NZD/USD", "NZDUSD=X"),

    # Important cross pairs
    ("EUR/GBP", "EURGBP=X"),
    ("EUR/JPY", "EURJPY=X"),
    ("GBP/JPY", "GBPJPY=X"),
    ("AUD/JPY", "AUDJPY=X"),
    ("CHF/JPY", "CHFJPY=X"),
    ("EUR/CHF", "EURCHF=X"),

    # Emerging market majors
    ("USD/CNY", "CNY=X"),
    ("USD/INR", "INR=X"),
    ("USD/BRL", "BRL=X"),
    ("USD/ZAR", "ZAR=X"),
    ("USD/KRW", "KRW=X"),
    ("USD/MXN", "MXN=X"),
    ("USD/TRY", "TRY=X")
]

# -----------------------------------
# Tickers and portfolio weights
# -----------------------------------

# Microsoft (MSFT)                                              15%
# NVIDIA (NVDA)                                                 20%
# Taiwan Semiconductor (TSM)                                    10%
# AMD                                                           10%
# Rheinmetall (RHM.DE)                                          10%
# Siemens Energy (ENR.DE)                                       10%
# Palantir (PLTR)                                               10% 
# Rocket Lab (RKLB)                                              5%
# Cash: Xtrackers II Eurozone Government Bond 1-3 UCITS ETF 1C  10%
portfolio = {
    "MSFT":     0.15,
    "NVDA":     0.20,
    "TSM":      0.10,
    "AMD":      0.10,
    "RHM.DE":   0.10,
    "ENR.DE":   0.10,
    "PLTR":     0.10,
    "RKLB":     0.05,
    "DBXP.DE":  0.10
}
# Benchmarks: Invesco QQQ Trust (QQQ) and Invesco EQQQ Nasdaq-100 UCITS (EQQQ.DE)
benchmark1 = "QQQ" # Benchmark: Invesco QQQ Trust
benchmark2 = "EQQQ.DE" # Benchmark: Invesco EQQQ Nasdaq-100 UCITS

PORTFOLIO_TICKERS = [
        ("Microsoft Corporation", "MSFT"),
        ("NVIDIA Corporation", "NVDA"),
        ("Taiwan Semiconductor Manufacturing Company", "TSM"),
        ("Advanced Micro Devices, Inc.", "AMD"),
        ("Rheinmetall AG", "RHM.DE"),
        ("Siemens Energy AG", "ENR.DE"),
        ("Palantir Technologies Inc.", "PLTR"),
        ("Rocket Lab USA Inc.", "RKLB"),
        ("Xtrackers II Eurozone Government Bond 1-3 UCITS ETF 1C", "DBXP.DE")
]

def insert_companies(COMPANIES: list[tuple[str, str]]):
    """
    Auto-insert default companies safely (idempotent).
    Mirrors the original MongoDB upsert behaviour exactly.
    """
    conn = create_connection()
    inserted_count = 0

    with conn.cursor() as cur:
        for name, ticker in COMPANIES:
            cur.execute(
                """
                INSERT INTO companies (company_name, ticker_symbol)
                VALUES (%s, %s)
                ON CONFLICT (ticker_symbol)
                DO UPDATE SET company_name = EXCLUDED.company_name
                RETURNING (xmax = 0) AS is_new;
                """,
                (name, ticker),
            )
            row = cur.fetchone()
            if row and row[0]:          # xmax = 0 means it was a fresh INSERT
                inserted_count += 1

    conn.commit()
    conn.close()
    print(f"✔ Company list synced! (Newly inserted: {inserted_count})")


if __name__ == "__main__":
    print("Inserting DEFAULT_COMPANIES ...")
    insert_companies(DEFAULT_COMPANIES)
    print("Inserting NIFTY50 ...")
    insert_companies(NIFTY50)
    print("Inserting MAJOR_GLOBAL_INDICES ...")
    insert_companies(MAJOR_GLOBAL_INDICES)
    print("Inserting MAJOR_GLOBAL_CURRENCIES ...")
    insert_companies(MAJOR_GLOBAL_CURRENCIES)
    print("Inserting PORTFOLIO_TICKERS ...")
    insert_companies(PORTFOLIO_TICKERS)