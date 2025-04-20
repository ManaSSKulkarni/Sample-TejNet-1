
def add(a, b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    if a < b:
        return a + b


def example(arg1, arg2):
    """_summary_

    Args:
        arg1 (_type_): _description_
        arg2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    if (arg1 > arg2):
        print('Arg1 is greater')
    else:
        print('Arg2 is greater')
    return {'result': arg1+arg2, 'status': 'success'}
