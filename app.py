from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# 虚拟币 ID 列表（最多支持 250 个）
COIN_IDS = ','.join([
    'bitcoin', 'ethereum', 'cardano', 'dogecoin', 'solana', 'polkadot',
    'tron', 'uniswap', 'chainlink', 'avalanche', 'litecoin', 'polygon',
    'stellar', 'vechain', 'cosmos', 'monero', 'tezos', 'theta', 'sandbox', 'aptos',
    'render', 'arbitrum', 'algorand', 'hedera', 'elrond', 'flow', 'filecoin',
    'near', 'icp', 'mina', 'aave', 'fantom', 'kava', 'axie-infinity', 'injective',
    'gnosis', 'loopring', 'neo', 'quant', 'chiliz', 'oasis-network', 'curve-dao-token',
    'zilliqa', '1inch', 'basic-attention-token', 'bittorrent', 'celo', 'compound',
    'dydx', 'fetch-ai', 'gala', 'helium', 'illuvium', 'iota', 'kaspa', 'kusama',
    'lido-dao', 'ocean-protocol', 'optimism', 'ravencoin', 'rocket-pool',
    'serum', 'shiba-inu', 'skale', 'spell-token', 'sushi', 'synthetix', 'terra-luna',
    'thorchain', 'twt', 'uma', 'wrapped-bitcoin', 'zcash'
])

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/api/all-prices')
def get_all_prices():
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={COIN_IDS}&vs_currencies=usd"
        headers = {
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        prices = response.json()
        return jsonify(prices)
    except Exception as e:
        return jsonify({"error": "Failed to fetch prices", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)