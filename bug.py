def function_with_uncommon_error(data):
    try:
        result = 1 / data['missing_key']  # KeyError if 'missing_key' is absent
        return result
    except KeyError:
        print("KeyError occurred. Handle it gracefully!")
        return None
    except ZeroDivisionError:
        print("ZeroDivisionError occurred. Handle it gracefully!")
        return None
    except TypeError:
        print("TypeError occurred. Handle it gracefully!")
        return None

data = {"key1": 10}
result = function_with_uncommon_error(data)