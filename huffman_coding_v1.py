import heapq
from collections import defaultdict

# Import w_optimal from egd_for_stat_proj_v1.py
from egd_for_stat_proj_v1 import w_optimal

# Read the text from the file
file_path = 'C:\\Users\\inoxb\\Downloads\\input.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Define the Huffman coding function
def huffman_coding(text, weights):
    # Create a dictionary to store the frequency of each character
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    # Build the Huffman tree
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Create a dictionary to store the Huffman codes
    huffman_codes = {}
    for char, code in heap[0][1:]:
        huffman_codes[char] = code

    # Encode the text using Huffman codes
    encoded_text = ''.join(huffman_codes[char] for char in text)

    return encoded_text, huffman_codes

# Apply Huffman coding with the weights from w_optimal
encoded_text, huffman_codes = huffman_coding(text, w_optimal)

# Print the encoded text
print("Encoded text:")
print(encoded_text)

# Print the mapping of ASCII characters to binary strings
print("\nCharacter - Binary String Mapping:")
for char, code in huffman_codes.items():
    print(f"'{char}' - {code}")
