import pytest
import requests
import json

def test_product():
    url = 'http://commdity-develop.kapeixi.cn/product/PPI1001001'
    headers = {"content-type": "application/json"}
    para = {'skuIdList': [773, 778, 788]}


    r = requests.post(url, json=para, headers=headers)
    print(json.dumps(r.json(),indent=2,ensure_ascii=False))

if __name__ == '__main__':
    pytest.main(["-vs","test_api.py"])