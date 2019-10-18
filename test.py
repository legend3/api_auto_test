import os
import yaml
import requests
import os
from configparser import ConfigParser

data = {
  "username": "webadmin",
  "password": "webadmin123456",
  "vcode": "wannengyanzhengma"
}


def Login():
    """
    用例描述：登录
    """

    # session = requests.sessions()
    r = requests.post('http://192.168.0.156/audit-core/login/checkLogin.do', params=data)
    print(r.url)
    cookie = r.cookies.get_dict()
    print(type(cookie))
    # print(cookie)
    print(type(cookie['JSESSIONID']))
    result = r.json()
    # print(result)
    # assert str(result['success']) == 'True'
    print(dict(JSESSIONID=cookie['JSESSIONID']))
    return cookie


# Login()
curPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
# print(curPath)
c = ConfigParser.read(curPath, encoding='UTF-8')
print(c)

