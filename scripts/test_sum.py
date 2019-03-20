import os
import sys
sys.path.append(os.getcwd())

import pytest

from read_data.read_data import ReadData


def get_data():
    datas = ReadData().read_yaml() #读取yaml文件中的数据
    arrs = []
    for data in datas.values():
        arrs.append((data[0],data[1]))
    return arrs


class TestSum():
    @pytest.mark.parametrize("a,b",get_data())
    def test_sum(self,a,b):
        a = 3
        b = 5
        sum = a+b
        print(sum)

if __name__ == '__main__':
    # print(get_data())
    # TestSum().test_sum()
    pass