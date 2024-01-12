import write_your_name as name_point

def test_hi_my_name_is():
    assert len(name_point.hi_my_name_is())  > 1 
    name = name_point.hi_my_name_is()
    print(name)


test_hi_my_name_is()    


