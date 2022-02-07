#This will test the function
import pytest

@pytest.mark.parametrize("input, expected", [
    (([2,3],[3,1], 4), -1),
    (([2,3],[2,1], 2), 2),
    (([2,3],[3,3], 4), 1),
    (([-2,1],[-1,2], -3), 0),
    (([-2,-2],[-4,-4],-6), -6),
    (([1,-1],[2,-2],3), -3),
    (([0,0],[1,2],2), 4),
    (([1,1],[2,2],0), 0),
    ])

def test_points547(input, expected):
    from points547 import points
    answer=points(input)
    assert answer==expected
