import requests
import allure
import pytest


@allure.feature('full-text')
@allure.story('unclear')
@allure.severity('B')
def test_unclear_search(env_config, jsessionid):
    """全文模糊查询"""
    cookie = jsessionid
    # headers =  {# get方式
    #     "JSESSIONID": Login['JSESSIONID'])
    # }
    url = env_config['host']['url'] + env_config['unclear_search_url']['unurl']
    unclear_searchparams = {'text': env_config['unclear_search_data']['text']}

    # r = requests.post(url, params=unclear_searchparams, headers=headers)  # get方式
    r = requests.post(url, params=unclear_searchparams, cookies=jsessionid)  # post方式,JSESSIONID='xxxxx'
    result_unclear_search = r.json()
    assert str(result_unclear_search['success']) == 'True'


@allure.feature('full-text')
@allure.story('list_data')
@allure.severity('B')
def test_list_data(env_config,jsessionid):
    """全文列表"""
    cookie = jsessionid
    url = env_config['host']['url'] + env_config['list_Data']['ld']
    ld_params = {'page': env_config['ld_data']['page'], 'limit': env_config['ld_data']['limit'], 'params': env_config['ld_data']['params']}

    # r = requests.post(url, params=unclear_searchparams, headers=headers)  # get方式
    r = requests.post(url, params=ld_params, cookies=jsessionid)  # post方式,JSESSIONID='xxxxx'
    result_list_data = r.json()
    assert str(result_list_data['success']) == 'True'


# @allure.feature('full-Text')
# @allure.story('login')
# @allure.severity('A')
# @pytest.fixture(scope='session')
# def login(env_config):
#     """登录"""
#     url = env_config['host']['url'] + env_config['Login_url']['lurl']
#     loginparams = {'username': env_config['Login_data']['username'], 'password': env_config['Login_data']['password'],
#                    'vcode': env_config['Login_data']['vcode']}
#
#     # session = requests.sessions()
#     r = requests.post(url, params=loginparams)
#     # print(r.url)
#     cookie = r.cookies.get_dict()
#     result_login = r.json()
#     assert str(result_login['success']) == 'True'
#     return dict(JSESSIONID=cookie['JSESSIONID'])


@pytest.fixture(scope='session', name='jsessionid')
def full_text(env_config):
    """Connect to server before testing, util after."""
    # Setup : start login
    url = env_config['host']['url'] + env_config['Login_url']['lurl']
    loginparams = {'username': env_config['Login_data']['username'], 'password': env_config['Login_data']['password'],
                   'vcode': env_config['Login_data']['vcode']}

    # session = requests.sessions()
    r = requests.post(url, params=loginparams)
    # print(r.url)
    cookie = r.cookies.get_dict()
    result_login = r.json()
    jsessionid = dict(JSESSIONID=cookie['JSESSIONID'])
    assert str(result_login['success']) == 'True'
    print("\nsetup")
    yield jsessionid  # 此处开始执行测试用例且传递setup之前的数据到test

    # Teardown : over
    print("\nteardown")
