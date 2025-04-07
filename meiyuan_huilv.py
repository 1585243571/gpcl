import requests

# 替换为你的 API Key
API_KEY = 'eb87ab46559ea72ee0376f8c'
def get_usd_to_cny_exchange_rate(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Error fetching exchange rate data")
    
    data = response.json()
    if "conversion_rates" not in data:
        raise Exception("Invalid API response")
#    print(data)
    usd_to_cny_rate = data["conversion_rates"]["CNY"]
    return usd_to_cny_rate

if __name__ == "__main__":
    try:
        rate = get_usd_to_cny_exchange_rate(API_KEY)
        print(f"Current USD to CNY exchange rate: {rate}")
    except Exception as e:
        print(f"Failed to fetch exchange rate: {e}")

