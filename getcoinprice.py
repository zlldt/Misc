from __future__ import print_function
import requests
import cx_Oracle


class Solution:
    def getprice(self):
        url = 'https://api.coinmarketcap.com/v2/ticker/'
        null = ''
        r = requests.get(url)
        coindict = eval(r.text)
        print('length=', len(coindict['data']))

        connection = cx_Oracle.connect("dbuser", "dbpassword", "localhost/orcl")
        cursor = connection.cursor()
        insertquery = "INSERT INTO COINPRICE (SN, COIN_NAME, SYMBOL, PRICE) VALUES ('%s', '%s', '%s', '%s')"
        updatequery = "UPDATE COINPRICE SET PRICE= '%s' WHERE sn= '%s'"
        count = 0
        for coinid in coindict['data'].keys():
            name = coindict['data'][coinid]['name']
            symbol = coindict['data'][coinid]['symbol']
            price = coindict['data'][coinid]['quotes']['USD']['price']
            print(count, coinid, name, symbol, price)
            count += 1
            try:
                cursor.execute(insertquery % (coinid, name, symbol, price))
            except cx_Oracle.IntegrityError:
                cursor.execute(updatequery % (price, coinid))
        connection.commit()
        cursor.close()
        connection.close()
        print('count=', count)


test = Solution()
test.getprice()
