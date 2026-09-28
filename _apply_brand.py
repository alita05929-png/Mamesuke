# -*- coding: utf-8 -*-
"""Place Mamesuke art into existing slots and update site copy."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(r"E:\pack\bsc\7")
ASSETS = Path(r"C:\Users\Alita\.cursor\projects\e-pack-bsc-7\assets")
NEW = "0x6d54f0aea4777de067cb9b2b85912d237e847777"
FOUR = f"https://four.meme/token/{NEW}"
PANCAKE = f"https://pancakeswap.finance/swap?outputCurrency={NEW}"
SCAN = f"https://bscscan.com/token/{NEW}"
DEX = f"https://dexscreener.com/bsc/{NEW}"

GROUPS = {
    "mame-hero.png": ["**/broccoli-cyberpunk-city-hq-02-placeholder.jpg"],
    "mame-eco.png": ["**/Ecosystem-cover-02.jpg"],
    "mame-build.png": ["**/F3B-Build-01.jpg"],
    "mame-cyber.png": ["**/F3B_Cyberpunk-A03*.jpg"],
    "mame-moon.png": ["**/F3B_Moon_01.jpg"],
    "mame-farmer.png": ["**/F3B_Farmer_03.jpg"],
    "mame-gm.png": ["**/F3B_GM_D01.jpg"],
    "mame-poker.png": ["**/F3B_Poker_01.jpg"],
    "mame-skate.png": ["**/F3B-skateboard-01.jpg"],
    "mame-coins.png": ["**/F3B_Build_C01.jpg"],
    "mame-learn.png": ["**/F3B_Learn01.jpg"],
    "mame-car.png": ["**/F3B-Car-01.jpg"],
    "mame-jetski.png": ["**/F3B_Jetski_02.jpg"],
    "mame-paint.png": ["**/F3B_Build_B01.jpg"],
    "mame-rocket.png": ["**/F3B-rocket-01.jpg"],
    "mame-chef.png": ["**/F3B-Chef-01.jpg"],
    "mame-plant.png": ["**/F3B_Build_D01.jpg"],
    "mame-beach.png": ["**/F3B-Beach-01.jpg"],
    "mame-square.png": ["**/Broccoli-x-Binance-Square-01*.jpg"],
    "mame-winner.png": ["**/bsc-chain-winner-01*.jpg"],
    "mame-phone.png": ["**/iphone-binance-wallet-03*.jpg"],
    "mame-book.png": ["**/giggle-book*.jpg"],
    "mame-ep1.png": ["**/Broccoli-MB-00C*.jpg"],
    "mame-ep2.png": ["**/F3B_Giggle_EP02_00A*.jpg"],
    "mame-ep3.png": ["**/F3B_Story_EP003_00A04*.jpg"],
    "mame-ep4.png": ["**/F3B_Story_EP004_00B*.jpg"],
    "mame-ep5.png": ["**/F3B_Story_EP005_00A*.jpg"],
    "mame-ep6.png": ["**/F3B_Story_EP006_00A*.jpg"],
    "mame-ep7.png": ["**/F3B_Story_EP007_00_A*.jpg"],
}


def cover(src, size):
    im = Image.open(src).convert("RGB")
    fitted = ImageOps.fit(im, size, Image.Resampling.LANCZOS, centering=(0.5, 0.45))
    return fitted


def write_like(src, dest: Path):
    old = Image.open(dest)
    im = cover(src, old.size)
    if dest.suffix.lower() == ".png":
        im.save(dest, "PNG")
    else:
        im.save(dest, "JPEG", quality=88, optimize=True)


def circled(size):
    im = ImageOps.fit(
        Image.open(ROOT / "logo4.png").convert("RGBA"),
        (size, size),
        Image.Resampling.LANCZOS,
        centering=(0.5, 0.42),
    )
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    im.putalpha(mask)
    return im


def place_images():
    n = 0
    for asset, patterns in GROUPS.items():
        src = ASSETS / asset
        if not src.exists():
            raise SystemExit(f"missing {src}")
        dests = []
        for pat in patterns:
            dests.extend(ROOT.glob(pat))
        if not dests:
            raise SystemExit(f"no dest for {asset}")
        for dest in dests:
            write_like(src, dest)
            n += 1
            print(f"img {dest.relative_to(ROOT)}")

    logo = Image.open(ROOT / "logo4.png").convert("RGBA")
    for dest in ROOT.glob("**/broccoli-favicon*.png"):
        old = Image.open(dest)
        ImageOps.fit(logo, old.size, Image.Resampling.LANCZOS, centering=(0.5, 0.42)).save(dest, "PNG")
        n += 1
        print(f"img {dest.relative_to(ROOT)}")

    for dest in ROOT.glob("**/cropped-Broccoli_logoCircle_500px*.png"):
        old = Image.open(dest)
        circled(old.size[0]).save(dest, "PNG")
        n += 1
        print(f"img {dest.relative_to(ROOT)}")

    header = Image.new("RGBA", (93, 43), (0, 0, 0, 0))
    face = circled(43)
    header.paste(face, ((93 - 43) // 2, 0), face)
    header_path = ROOT / "wp-content/themes/Divi/images/logo.png"
    header.save(header_path, "PNG")
    n += 1
    print("img header logo")

    word = Image.new("RGBA", (400, 41), (0, 0, 0, 0))
    font = ImageFont.truetype(r"C:\Windows\Fonts\YuGothB.ttc", 28)
    draw = ImageDraw.Draw(word)
    text = "まめすけ"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (400 - tw) // 2 - bbox[0]
    y = (41 - th) // 2 - bbox[1]
    draw.text((x, y), text, font=font, fill=(245, 197, 66, 255))
    word_path = ROOT / "wp-content/uploads/2025/02/logo-1-e1744717578807.png"
    word.save(word_path, "PNG")
    n += 1
    print("img wordmark")
    print("images", n)


PHRASES = [
    (
        "Name and ticker: 人民交易所. The people’s exchange — a community-owned token on BNB Chain.",
        "Name and ticker: まめすけ. A little Shiba on BNB Chain — a community token in a green scarf.",
    ),
    (
        "The ticker and name “人民交易所” are on BNB Chain through the FOUR.MEME platform. The project is fully community-managed and owned.",
        "The ticker and name “まめすけ” are on BNB Chain through the FOUR.MEME platform. The project is fully community-managed and owned.",
    ),
    (
        "This is the people’s exchange: one name, one ticker, and a market built to bring people together.",
        "まめすけ is one name and one ticker: a diligent little Shiba bringing the community together.",
    ),
    (
        "We work with partners across Binance and BNB Chain. 人民交易所 is the figurehead of this movement — education, outreach, onboarding, and tools that make the ecosystem better for everyone.",
        "We work with partners across Binance and BNB Chain. まめすけ is the mascot of this movement — education, outreach, onboarding, and tools that make the ecosystem warmer for everyone.",
    ),
    (
        "Binance and BNB Chain are home for this market, and the community is building 人民交易所 in that chapter.",
        "Binance and BNB Chain are home, and the community is growing まめすけ in that chapter.",
    ),
    (
        "人民交易所 has communities around the world and a presence on Binance Square. Follow along for news and updates.",
        "まめすけ has friends around the world and a presence on Binance Square. Follow along for news and updates.",
    ),
    (
        "人民交易所 is deployed on BNB Chain through the Four.meme platform. The goal is a community token people can gather around — a shared exchange, not only hype.",
        "まめすけ is deployed on BNB Chain through the Four.meme platform. The goal is a community token people can gather around — a shared little shrine, not only hype.",
    ),
    (
        "We are building something open and lasting, powered by the gold mark, education, and a global community. Whether you are new to crypto or already trading, there is a place for you here.",
        "We are building something open and lasting, powered by a golden shrine, a green scarf, and a global community. Whether you are new to crypto or already trading, there is a place for you here.",
    ),
    (
        "Join the movement and build the people’s exchange with us — one name and one ticker: 人民交易所.",
        "Join the movement and grow まめすけ with us — one name and one ticker: まめすけ.",
    ),
    (
        "THE PEOPLE’S EXCHANGE ON BNB CHAIN",
        "まめすけ ON BNB CHAIN",
    ),
    (
        "人民交易所 is the community token. The mark is the gold diamond. The name is 人民交易所. The ticker is 人民交易所. It launched on FOUR.MEME for people who want a shared exchange on BNB Chain.",
        "まめすけ is the community token. The mark is the little Shiba in a green scarf. The name is まめすけ. The ticker is まめすけ. It launched on FOUR.MEME for people who want a warm shared token on BNB Chain.",
    ),
    (
        "learn the people’s exchange at the academy!",
        "learn まめすけ at the academy!",
    ),
    (
        "At the harvest festival, one trader takes more than their share. 人民交易所 is a reminder that a market stays full when people give as well as take.",
        "At the harvest festival, one trader takes more than their share. まめすけ is a reminder that a basket stays full when friends give as well as take.",
    ),
    (
        "Builders write the market together. Shared rules and fair choices create something that belongs to everyone: 人民交易所.",
        "Builders write the story together. Shared rules and fair choices create something that belongs to everyone: まめすけ.",
    ),
    (
        "Join 人民交易所, a playful pup, on a magical adventure!",
        "Join まめすけ, a playful Shiba pup, on a magical adventure!",
    ),
    (
        "Binance is SAFU. People’s exchange. Intern got promoted.",
        "Binance is SAFU. まめすけ. A little Shiba on BNB.",
    ),
    (
        "人民交易所 | People's Exchange",
        "まめすけ",
    ),
    ("href=\"https://人民交易所\"", f'href="{FOUR}"'),
    ("https://coinmarketcap.com/currencies/broccoli/", DEX),
    ("https://www.coingecko.com/en/coins/broccoli", DEX),
    ("https://www.dextools.io/app/en/token/firstbroccoli?t=1742653472062", DEX),
    ("https://www.cyberscope.io/audits/8-broccoli", SCAN),
    ("https://binance.com/en/futures/BROCCOLIF3BUSDT", FOUR),
    ("https://www.mexc.com/exchange/BROCCOLIF3B_USDT", PANCAKE),
    ("https://www.lbank.com/en-US/trade/broccoli4_usdt/", PANCAKE),
    ("https://bingx.com/en/spot/BROCCOLIF3BUSDT/", PANCAKE),
    ("https://poloniex.com/trade/BROCCOLIF3B_USDT/?type=spot", PANCAKE),
    ("https://ascendex.com/en/cashtrade-spottrading/usdt/broccoli4", PANCAKE),
    ("https://binance.com/en/square/profile/broccoli", "https://binance.com/en/square"),
    ("https://t.me/broccoli", "https://t.me"),
    ("0xdb25c09d96c165b62f6e6f9d9b17174738d897ba", NEW),
    ("0x12B4356C65340Fb02cdff01293F95FEBb1512F3b", NEW),
    ("0x12b4356c65340fb02cdff01293f95febb1512f3b", NEW),
    ("人民交易所", "まめすけ"),
    ("People's Exchange", "まめすけ"),
    ("people’s exchange", "まめすけ"),
    ("People’s exchange", "まめすけ"),
]


def update_html():
    for path in ROOT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        orig = text
        for old, new in PHRASES:
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print("html", path.relative_to(ROOT))


if __name__ == "__main__":
    place_images()
    update_html()
