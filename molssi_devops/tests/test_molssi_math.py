import molssi_devops
import pytest
import sys
import numpy as np

def test_mean():
    """
    Test that the md.mean() function returns the mean appropriately
    """
    test_list = [1, 2, 3, 4, 5]
    expected = 3
    calculated = molssi_devops.mean(test_list)
    assert expected == calculated

@pytest.mark.my_test
def test_mean_type_error():
    test_variable = 'this is a string'

    with pytest.raises(TypeError):
        molssi_devops.mean(test_variable)

@pytest.mark.parametrize("num_list, expected_mean" , [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5),
    (list(range(1, 1000000)), 1000000/2.0)
])

def test_many(num_list, expected_mean):
    # assert mean(num_list) == expected_mean
    assert np.isclose(molssi_devops.mean(num_list), expected_mean, 1e-6)
