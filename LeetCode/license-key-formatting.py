def license_key_formatting(key):
    key = key.replace('-','')
    n = len(key)
    full = n // 4
    rem = n % 4
    formatted_key = []
    for i in range(rem, n):
        formated_key.append(key[i:i+4])
    if rem > 0:
        formatted_key = key[:rem] + formatted_key
    return '-'.join(formatted_key)
