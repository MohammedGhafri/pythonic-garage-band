from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import  Band,Guitarist,Bassist,Drummer
import pytest

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def prep_data():
    
    mahmoud=Bassist("mahmoud","Bassist")
    ahmad=Guitarist("ahmad","Guitarist")
    noor=Drummer("noor","Drummer")
    return {'ahmad':ahmad, 'mahmoud':mahmoud, 'noor':noor}


def test_one(prep_data):
    ahmad=Guitarist("ahmad","Guitarist")
    expected=f"This in the main Band {prep_data['ahmad'].name} will Play a solo"
    actual=Band.play_solos(prep_data['ahmad'])
    assert expected==actual

def test_two(prep_data):
    expected=f"{prep_data['mahmoud'].name} will Play a solo"
    actual=prep_data['mahmoud'].play_solos()
    assert expected==actual


def test_three(prep_data):
    expected=f"{prep_data['noor'].name} will Play a solo"
    actual=prep_data['noor'].play_solos()    
    assert expected==actual



