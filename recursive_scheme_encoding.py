import math

def expected_hits(n):
    # Calculate the expected number of hits needed to collect all ASCII characters
    return n * sum(1 / k for k in range(1, n + 1))

def scaling_factor(probability):
    # Calculate the scaling factor to achieve the desired probability threshold
    return -math.log(1 - probability)

n = 128  # Total number of ASCII characters
probability = 0.99  # Desired probability threshold

expected_hits_99 = expected_hits(n) * scaling_factor(probability)
expected_hits_99 = math.ceil(expected_hits_99)  # Round up to the nearest integer
print(expected_hits_99)
