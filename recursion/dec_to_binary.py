def dec_to_bin(decim):
    assert int(decim) == decim , 'integer must be'
    if decim == 0:
        return 0
    else:
        return decim%2 + 10 * dec_to_bin(int(decim/2))
print(dec_to_bin(13))