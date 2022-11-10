from src.algoritmo import creapassword
import src.algoritmo as algoritmo
from pytest_mock import MockerFixture

def testbruteforce(mocker: MockerFixture) -> None:
    # arrange
    mock_random_return = 6
    mocker.patch.object(algoritmo, "randint", return_value=mock_random_return)
    spy = mocker.spy(algoritmo, "randint")

    # assert
    assert creapassword(5) == "jjjjj"
    assert spy.call_count == 5
    assert spy.spy_return == mock_random_return
    # assert creapassword(6) == "hjkgdf"
    # assert creapassword(3) == "afh"
    # assert creapassword(0) == 0
