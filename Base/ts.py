import os

import pytest
import yaml

class GetDate():
    def read_sum_ya_data(self,finame):
        ss = []
        # with open('../data/'+os.sep+finame, 'r', encoding='utf-8') as f:
        with open('./data/'+os.sep+finame, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            print("data:{}".format(data))
            for i in data.values():
                print(i)
                ss.append(tuple(i.values()))
            print(ss)
        return ss


ss = GetDate()
s1 = GetDate().read_sum_ya_data('va.yaml')
print(s1)

# @pytest.mark.parametrize('a,b,c',ss. addead_sum_ya_data('va.yaml'))
# def sum(a,b,c):
#     assert a+b == c

# if __name__ == '__main__':
#     pytest.main(['ts'])

