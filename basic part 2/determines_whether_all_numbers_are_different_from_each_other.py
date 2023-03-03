def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
    
print(test_distinct([1,2,3,2]))
print(test_distinct([3,6,9,8,5,1,4,7]))