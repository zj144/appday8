import os
import sys

import pytest
sys.path.append(os.getcwd())

from Base.ts import GetDate


class TestSum:
    @pytest.mark.parametrize("a,b,c",GetDate().read_sum_ya_data('va.yaml'))
    def test_sum(self, a, b, c):
        print(f"{a}+{b}={c}")
        assert a + b == c


if __name__ == '__main__':
    pytest.main(['08test_lx.py'])