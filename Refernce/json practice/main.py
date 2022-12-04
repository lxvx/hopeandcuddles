import json

def test_names():
    name = input('enter name:  ')


    names = []
    
    names.append(name)

    filename = 'test_names.json'
    
    with open(filename, 'w') as the_file:
        json.dump(name, the_file)

test_names()