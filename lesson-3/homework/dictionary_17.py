nested_dict = {
    'person': {
        'name': 'Alice',
        'details': {
            'age': 30,
            'city': 'Riga'
        }
    }
}

value = nested_dict['person']['details']['city']
print(value) 
