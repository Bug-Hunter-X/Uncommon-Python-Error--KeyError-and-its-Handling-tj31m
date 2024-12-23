def function_with_uncommon_error(data):
    try:
        if "missing_key" not in data:
            print("Key 'missing_key' is not present in the dictionary. Returning default value.")
            return 0  # Or another default value as appropriate
        result = 1 / data['missing_key']
        return result
    except ZeroDivisionError:
        print("ZeroDivisionError occurred. Handle it gracefully!")
        return None
    except TypeError:
        print("TypeError occurred. Handle it gracefully!")
        return None
data = {"key1": 10}
result = function_with_uncommon_error(data)
print(result) #Will return 0 since missing_key is not in the dictionary