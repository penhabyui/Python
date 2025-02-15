from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Andre", "Muniz") == "Muniz; Andre"
    assert make_full_name("Jose Roberto", "Cardoso") == "Cardoso; Jose Roberto"
    assert make_full_name("Alex", "Atkinson-Lloyd") == "Atkinson-Lloyd; Alex"

def test_extract_family_name():
    """Verify that the extract_family_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_family_name("Atkinson-Lloyd; Alex") == "Atkinson-Lloyd"
    assert extract_family_name("Cardoso; Jose Roberto") == "Cardoso"
    assert extract_family_name("Muniz; Andre") == "Muniz"
    assert extract_family_name("Brown; Sally") == "Brown"

def test_extract_given_name():
    """Verify that the extract_given_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_given_name("Atkinson-Lloyd; Alex") == "Alex"
    assert extract_given_name("Cardoso; Jose Roberto") == "Jose Roberto"
    assert extract_given_name("Muniz; Andre") == "Andre"
    assert extract_given_name("Brown; Sally") == "Sally"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])