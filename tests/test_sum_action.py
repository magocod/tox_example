"""
...
"""

# third-party
import pytest

# local Django
from pack.utils import sum_action


@pytest.mark.utils
def test_sum_action():
    """
    ...
    """
    result = sum_action(1, 3)
    assert result == 4
