def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    string = '{}{}{}'.format(one, delimiter, two)    
    return string.upper()

result = get_summ('Learn','Python')
print(result)