import molssi_devops
import pytest
import sys

def test_title_case():
    """"
    Test that the title_case function returns the appropriate sentence
    """

    test_sentence = "a SENTENCE tO CheCK."
    expected = "A Sentence To Check."
    calculated = molssi_devops.util.title_case(test_sentence)
    assert expected == calculated

def test_type_error():
    test_case = ['this', 'is', 'not', 'a', 'string']

    with pytest.raises(TypeError):
        molssi_devops.title_case(test_case)
