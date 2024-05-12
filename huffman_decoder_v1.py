from huffman_coding_v1 import encoded_text
from huffman_coding_v1 import huffman_codes 
def huffman_decoder(encoded_texting, huffman_mapping):
    decoded_text = ""
    current_code = ""
    
    # Invert the huffman_mapping to map codes to characters
    inverted_mapping = {code: char for char, code in huffman_mapping.items()}
    
    for bit in encoded_texting:
        current_code += bit
        if current_code in inverted_mapping:
            decoded_text += inverted_mapping[current_code]
            current_code = ""
    
    return decoded_text

# Example usage:
# encoded_text is the Huffman encoded binary string
# huffman_mapping is the mapping of characters to their Huffman codes
# Replace these with your actual encoded text and mapping
encoded_texting = encoded_text
huffman_mapping = huffman_codes

decoded_text = huffman_decoder(encoded_text, huffman_mapping)
print("Decoded Text:", decoded_text)
