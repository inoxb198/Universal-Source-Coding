import heapq

class Node:
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.weight < other.weight

def build_huffman_tree(weights):
    # Create a priority queue (min heap) of nodes
    pq = [Node(symbol, weight) for symbol, weight in weights.items()]
    heapq.heapify(pq)

    # Build the Huffman tree
    while len(pq) > 1:
        # Remove the two nodes with the lowest weights
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)

        # Create a new parent node with the combined weight
        parent = Node(None, left.weight + right.weight)
        parent.left = left
        parent.right = right

        # Add the parent node back to the priority queue
        heapq.heappush(pq, parent)

    # Return the root of the Huffman tree
    return pq[0]

def generate_huffman_codes(root, code="", codes={}):
    # Traverse the Huffman tree recursively
    if root is not None:
        # If leaf node, assign code
        if root.symbol is not None:
            codes[root.symbol] = code
        # Traverse left and right children
        generate_huffman_codes(root.left, code + "0", codes)
        generate_huffman_codes(root.right, code + "1", codes)
    return codes

def huffman_encode(text, codes):
    # Encode the input text using the generated Huffman codes
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

# Example usage
text = "abracadabra"
unique_chars = set(text)
weights_vector = {char: text.count(char) for char in unique_chars}

# Build Huffman tree
root = build_huffman_tree(weights_vector)

# Generate Huffman codes
codes = generate_huffman_codes(root)

# Encode input text
encoded_text = huffman_encode(text, codes)

print("Huffman Codes:", codes)
print("Encoded Text:", encoded_text)

