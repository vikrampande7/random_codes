def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    n = len(samples)
    freq = {}
    pmf = []
    for s in samples:
        freq[s] = freq.get(s, 0) + 1
    for k, v in freq.items():
        pmf.append((k, v/n))
    return pmf