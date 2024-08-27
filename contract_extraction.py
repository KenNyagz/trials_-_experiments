import ccxt
import requests
'''Attempts to extract token addresses of exchanges listed on centralised exchanges via ccxt'''

# Replace with your Etherscan API key
ETHERSCAN_API_KEY = 'YourEtherscanAPIKey'

# Step 1: Initialize and fetch token data from multiple exchanges using CCXT

def fetch_tokens_from_exchanges():
    # Initialize exchanges
    exchanges = {
        'binance': ccxt.binance(),
        'kucoin': ccxt.kucoin(),
        # Add more exchanges as needed
    }

    # Dictionary to store token data
    tokens = {}

    # Fetch market data for each exchange
    for exchange_name, exchange in exchanges.items():
        markets = exchange.load_markets()
        for market in markets.values():
            base_token = market['base']  # The token symbol (e.g., BTC, ETH)
            if base_token not in tokens:
                tokens[base_token] = []

            # Check if the market data includes a contract address
            contract_address = market.get('info', {}).get('contractAddress', None)

            # Store symbol, exchange information, and contract address if available
            tokens[base_token].append({
                'symbol': market['symbol'],
                'exchange': exchange_name,
                'quote': market['quote'],
                'contract_address': contract_address  # Contract address from the exchange
            })

    return tokens

# Step 2: Retrieve official contract address from Etherscan API

def get_contract_address_from_etherscan(token_symbol):
    url = f'https://api.etherscan.io/api?module=token&action=tokeninfo&contractaddress={token_symbol}&apikey={ETHERSCAN_API_KEY}'

    response = requests.get(url)
    data = response.json()

    if data['status'] == '1' and 'result' in data:
        return data['result'][0]['contractAddress']
    else:
        return None

# Step 3: Compare contract addresses from exchange and Etherscan

def compare_contract_addresses(tokens):
    for token, details in tokens.items():
        print(f"\nChecking Token: {token}")
        for detail in details:
            exchange_contract_address = detail['contract_address']
            if not exchange_contract_address:
                print(f" - Exchange: {detail['exchange']} | Symbol: {detail['symbol']} | Contract Address: Not Provided by Exchange")
                continue

            etherscan_contract_address = get_contract_address_from_etherscan(token)
            if etherscan_contract_address:
                if exchange_contract_address.lower() == etherscan_contract_address.lower():
                    print(f" - Exchange: {detail['exchange']} | Symbol: {detail['symbol']} | Match: YES")
                else:
                    print(f" - Exchange: {detail['exchange']} | Symbol: {detail['symbol']} | Match: NO")
                    print(f"   Exchange Address: {exchange_contract_address} | Etherscan Address: {etherscan_contract_address}")
            else:
                print(f" - Exchange: {detail['exchange']} | Symbol: {detail['symbol']} | Etherscan Contract Address: Not Found")

# Step 4: Combine all steps to run the full validation

def main():
    # Step 1: Fetch tokens from exchanges
    tokens = fetch_tokens_from_exchanges()

    # Step 2 & 3: Compare contract addresses
    compare_contract_addresses(tokens)

# Run the script
if __name__ == "__main__":
    main()

