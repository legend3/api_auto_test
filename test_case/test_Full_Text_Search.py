import requests
import allure
import pytest


@allure.feature('full-text')
@allure.story('unclear')
@allure.severity('B')
# def test_unclear_search(env_config, Login):
def test_unclear_search(env_config,Login):
    """全文检索-模糊查询"""
    # headers =  {# get方式
    #     "JSESSIONID": Login['JSESSIONID'])
    # }
    url = env_config['host']['url'] + env_config['unclear_search_url']['unurl']
    unclear_searchparams = {'text': env_config['unclear_search_data']['text']}

    # r = requests.post(url, params=unclear_searchparams, headers=headers)  # get方式
    r = requests.post(url, params=unclear_searchparams, cookies=Login)  # post方式,JSESSIONID='xxxxx'
    # print(r.url)
    result1 = r.json()
    print(Login)
    assert str(result1['success']) == 'True'


def test_List_Data(env_config, Login):
    url = env_config['host']['url'] + env_config['list_Data']['ld']
    ld_params = {'page': env_config['ld_data']['page'], 'limit': env_config['ld_data']['limit'], 'params': env_config['ld_data']['params']}

    # r = requests.post(url, params=unclear_searchparams, headers=headers)  # get方式
    r = requests.post(url, params=ld_params, cookies=Login)  # post方式,JSESSIONID='xxxxx'
    # print(r.url)
    result2 = r.json()
    print(Login)
    assert str(result2['success']) == 'True'
