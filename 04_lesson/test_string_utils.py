import pytest
from string_utils import StringUtils


@pytest.fixture(scope="module")
def utils():
    return StringUtils()


@pytest.mark.positive
def test_capitalize_positive(utils):
    assert utils.capitalize("home") == 'Home'
    assert utils.capitalize("cat") == 'Cat'
    assert utils.capitalize("dog") == 'Dog'


@pytest.mark.positive
def test_capitalize_empty(utils):
    assert utils.capitalize('') == ''


@pytest.mark.negative
def test_capitalize_none(utils):
    with pytest.raises(TypeError):
        utils.capitalize(None)


@pytest.mark.positive
def test_trim_positive(utils):
    assert utils.trim(" home ") == 'home'
    assert utils.trim(" cat ") == 'cat'
    assert utils.trim(" dog ") == 'dog'


@pytest.mark.positive
def test_trim_empty(utils):
    assert utils.trim("") == ''


@pytest.mark.negative
def test_trim_none(utils):
    with pytest.raises(TypeError):
        utils.capitalize(None)

@pytest.mark.positive
def test_contain_valid(utils):
    assert utils.contains("Skypro", 'S')
    assert not utils.contains ("Skypro", "W")


@pytest.mark.negative
def test_contain_none(utils):
    with pytest.raises(TypeError):
        utils.contains(None, 'S')


@pytest.mark.positive
def test_delete_symbol_positive(utils):
    assert utils.delete_symbol("home", 'h') == 'ome'
    assert utils.delete_symbol("cat", 't') == 'ca'
    assert utils.delete_symbol("dog", 'o') == 'dg'

@pytest.mark.positive
    def test_delete_symbol_empty(utils):
        assert utils.delete_symbol("", 'Q') == ''


@pytest.mark.negative
def test_delete_symbol_none(utils):
    with pytest.raises(TypeError):
        utils.delete_symbol(None, 'S')
