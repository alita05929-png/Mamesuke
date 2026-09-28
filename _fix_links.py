# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(r"E:\pack\bsc\7")
NEW = "0x6d54f0aea4777de067cb9b2b85912d237e847777"
FOUR = f"https://four.meme/token/{NEW}"
PANCAKE = f"https://pancakeswap.finance/swap?outputCurrency={NEW}"
SCAN = f"https://bscscan.com/token/{NEW}"
DEX = f"https://dexscreener.com/bsc/{NEW}"
SQUARE = "https://www.binance.com/en/square"

TRADE = ("futures", "exchange", "trade", "/spot/", "cashtrade", "markets/")
SWAP = ("swap", "houdini", "chainspot", "1inch", "kiloex")
CHART = (
    "price",
    "coingecko",
    "coinmarketcap",
    "coinbase.com/price",
    "coinpaprika",
    "coinpedia",
    "comparemarketcap",
    "cryptorank",
    "tradingview",
    "lunarcrush",
    "dappradar",
    "dropstab",
    "dextools",
)


def dest_for(url: str) -> str:
    low = url.lower()
    if "square/profile" in low:
        return SQUARE
    if "cyberscope" in low or "/audits/" in low:
        return SCAN
    if any(k in low for k in SWAP):
        return PANCAKE
    if any(k in low for k in TRADE):
        return FOUR
    if any(k in low for k in CHART):
        return DEX
    return DEX


def unescape(url: str) -> str:
    return url.replace("\\/", "/")


pattern = re.compile(r"https?:(?:\\?/)+(?:(?!firstbroccoli)[^\"'\s])*?broccoli[^\"'\s]*", re.I)

for path in ROOT.rglob("*.html"):
    text = path.read_text(encoding="utf-8")
    found = pattern.findall(text)
    if not found:
        continue
    new_text = text
    for raw in sorted(set(found), key=len, reverse=True):
        plain = unescape(raw)
        if "firstbroccoli" in plain.lower():
            continue
        new = dest_for(plain)
        if "\\/" in raw:
            new = new.replace("/", "\\/")
        new_text = new_text.replace(raw, new)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        print(path.name, len(set(found)))
