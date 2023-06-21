import ccxt
import time

coin = "DOGE/USDT"


ex1 = ccxt.mexc({
    'apiKey': 'qwertyuiodfvbnmdfgh',
    'secret': 'cfvbnmsdfghjrftghjkwertyuvbnlkjhgffghjk'})


exchange_kucoin = ccxt.kucoin({
    'apiKey': '63ac1bh95b574b01*6db',
    'secret': 'e87e4dff-a*4e5',
    'password': '-------'})


def main():
    price_ex_1 = ex1.fetch_ticker(coin)['last']
    price_ex_kuco = exchange_kucoin.fetch_ticker(coin)['last']


    arbitrage = price_ex_1 - price_ex_kuco
    
    if arbitrage > 0:
        print('arbitrage *detected*')
        print(f'arbitrage:{arbitrage}')
        amount = 130


        print(ex1.id, ex1.create_limit_buy_order('DOGE/USDT', amount, price_ex_1))

        print(exchange_kucoin.id, exchange_kucoin.create_limit_sell_order('DOGE/USDT', amount, price_ex_kuco))

       
                                                  # ⬇⬆

        # print(exchange_kucoin.id, exchange_kucoin.create_limit_buy_order('DOGE/USDT', amount, price_ex_kuco))

        # print(ex1.id, ex1.create_limit_sell_order('DOGE/USDT', amount, price_ex_1))









    else:
        print(f'mexc: {price_ex_1} ----- kucoin: {price_ex_kuco} Arbitrage: {arbitrage}')


    time.sleep(10)


    

while True:
    main()
    
    
