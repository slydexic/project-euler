def problem10():
    """Find the sum of all the primes below two million."""
return sum(takewhile(lambda x: x<2e6, get_primes()))