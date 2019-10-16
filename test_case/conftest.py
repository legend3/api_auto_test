# encoding: utf-8
import pytest
import allure
import yaml
import os
import requests
'''
@author: legend
@file: conftest.py
@time: 2019/6/6 11:10
@desc:
'''
@pytest.fixture(scope="session",autouse=True)
def env_config():
    """
    读取yml配置文件
    """
    curPath = os.path.abspath(os.path.dirname(__file__))
    # print(curPath)
    curlist = curPath.split('\\')  # 以\\拆分当前路径
    rootPath = '\\'.join(curlist[0:4])  # 拆分路径分片+\\
    config_path = rootPath + '\\config\\env_config.yml'  # 获取配置文件的路径
    with open(config_path) as f:
        env_config = yaml.safe_load(f)  # 读取配置文件
    return env_config


# @allure.feature('QZ')  # 标注主要功能模块
# @allure.story('login')  # 标注Features功能模块下的分支功能
# @allure.severity('A')  # 标注测试用例的重要级别为'A'
# # @pytest.mark.parametrize('username,password,vcode',test_data)
# @pytest.fixture()
# def login(env_config):
#     """
#     用例描述：登录
#     """
#     # 从yml配置文件获取url
#     url = env_config['host']['url'] + env_config['Login_url']['lurl']
#     loginparams = {'username': env_config['Login_data']['username'], 'password': env_config['Login_data']['password'], 'vcode': env_config['Login_data']['vcode']}
#
#     # session = requests.sessions()
#     r = requests.post(url, params=loginparams)
#     # print(r.url)
#     cookie = r.cookies.get_dict()
#     result_login = r.json()
#     assert str(result_login['success']) == 'True'
#     return dict(JSESSIONID=cookie['JSESSIONID'])
