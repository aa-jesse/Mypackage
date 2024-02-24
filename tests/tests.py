from mypackage import myModule

def test_top_n():
    """
    make sure top_n works properly
    
    """

    assert myModule.top_n([5,7,3,9,2], 3) == [9,7,5], 'incorrect'
    assert myModule.top_n([5,7,43,91,12,4], 2) == [91,43], 'incorrect'
    assert myModule.top_n([1,2,3,4,5,6,7,8,9], 5) == [9,8,7,6,5], 'incorrect'