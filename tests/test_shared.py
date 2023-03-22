import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)




def test_space_compress():
    
    # Test Case

    test = "Test     This     Function"

    # Call Function

    test_result =  sh.space_compress(test)

    proper_output = "Test This Function"

    # Test if True

    assert test_result == proper_output, f"Expected {proper_output}, but got {test_result}"



@pytest.mark.xfail
def test_fail():

    assert (1,2,3) == (3,2,1)



@pytest.mark.skip(reason='Skipping Test On Purpose')
def test_skip():
    print('Skipping Test')




@pytest.mark.skipif(sys.platform == 'linux', reason = 'Skipping Test..... This test does not run on linux')
def test_skipif():
    print('My platform is ', sys.platform)


import mock
sys = mock.MagicMock()
sys.configure_mock(platform='win32')


@pytest.mark.xfail
@pytest.mark.skipif(sys.platform == 'linux', reason = 'Skipping Test.... this test does not run on linux')
def test_fail_skipif():
    print('My Platform is: ' , sys.platform)
    assert sys.platform == 'linux'
