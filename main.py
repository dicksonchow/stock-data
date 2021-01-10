import requests
import pandas


def invoke_aastocks_api(query_params):
    url = 'http://wdata.aastocks.com/datafeed/getultrablocktradelog.ashx?symbol={symbol}&type={' \
          'type}&lang=chi&dt=20210108&f=1'.format(**query_params)
    data = requests.get(url).json()
    print(data['tslog'])
    df_orig = pandas.DataFrame.from_dict(data['tslog'])
    # Date -> 日期, Price -> 股價, Turnover -> 金額, Volume -> 成交量
    df_new = df_orig.rename(columns={'dt': 'Date', 'p': 'Price', 't': 'Turnover', 'v': 'Volume', 'e': 'Other'})  # rename the column name
    file_name = '{}.csv'.format(query_params['symbol'])
    df_new.to_csv(file_name, encoding='utf-8', index=False)
    print(df_new.to_csv(index=False))


if __name__ == '__main__':
    # aastock types
    # ubbull -> 超大手買盤
    # bbull  -> 大手買盤
    # rbull  -> 散戶買盤
    # ubbear -> 超大手賣盤
    # bbear  -> 大手賣盤
    # rbear  -> 散戶賣盤
    aastocks_query_params = {
        'symbol': '00700',
        'type': 'ubbull'
    }
    invoke_aastocks_api(aastocks_query_params)
