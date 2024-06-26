To implement the following algorithm effectively, it's crucial to understand its key components and the sequential flow of operations. Here's a formal description of the algorithm:

1.Input Data Processing:
   - As a user continuously inputs data into a file, the module `number of char counter.py` processes each chunk of data.
   - Upon receiving a chunk of data, the `number of char counter.py` module runs the `egd for stat proj v1.py` file. This process computes the optimal weights based on the received data.

2. Huffman Encoding:
   - Using the obtained optimal weights, the module `huffman encoder.py` encodes the data and generates a dictionary mapping each character to its corresponding binary string.

3. Dictionary Concatenation:
   - When a user writes another piece of text, the same process is repeated to obtain optimal weights and create a corresponding dictionary.
   - If the ordering of weights remains the same, indicating no significant changes in the character frequencies, the new dictionary is concatenated with the previous one.
   - If the ordering of weights changes, suggesting a shift in character frequencies, the differences in the encoding scheme are noted and incorporated into the dictionary.

4. Continuous Operation:
   - This process continues iteratively as the user inputs more data. At each step, the algorithm adapts to changes in the data and updates the encoding scheme accordingly.

5. Decoding:
   - During decoding:
     - For the first step, the data is decoded directly using the original dictionary.
     - For subsequent steps, changes in the dictionary made during encoding are noted, and decoding is performed accordingly to account for these changes.

This algorithm allows for adaptive encoding and decoding, where the encoding scheme adjusts dynamically based on the observed data patterns. By continuously updating the encoding dictionary, the algorithm efficiently adapts to changes in the input data distribution while maintaining the ability to decode previous and current data streams accurately.

First we try and formalize how large should be a chunk of data.Suppose a monkey is randomly hitting keys on a typewriter with all the 128 ascii characters.The expected number of hits required to hit all the characters is 128H_{128} where H_{128} denotes the 128th harmonic number this fact comes from the Expectation of coupon collecting problem

We now formally show how the dictionary keeps on getting updated so at every step we dont have to save the dictionary and the process can be described as follows:

1. **Initialization**:
   - Given an initial encoding scheme \( E_1 \), weight vector \( W_1 \), and dictionary \( D_1 \), encode the first chunk of text using \( E_1 \) and maintain \( D_1 \).

2. **Updating Encoding Scheme**:
   - Upon adding a new chunk of text with weight vector \( W_2 \), construct a new dictionary \( D_2 \) corresponding to the new text.
   - Check the monotonicity of \( W_2 \) and \( W_1 + W_2 \):
     - If the monotonicity of \( W_2 \) matches \( W_1 + W_2 \), continue using \( E_1 \).
     - If the monotonicity of \( W_2 \) differs from \( W_1 + W_2 \):
       - Determine the smallest number of permutations required for \( W_2 \) to achieve the same monotonicity as \( W_1 + W_2 \).
       - Update \( D_1 \) accordingly by applying the permutations, ensuring that the changes preserve existing encodings as much as possible.
       - Use the modified dictionary \( D_1 \) to encode the new chunk of text with \( E_1 \).

3. **Recursion and Separate Computation**:
   - Repeat the above process recursively for subsequent chunks of text.
   - If the set of indexes of non-zero weights of \( W_2 \) is a subset or equal set of indexes of non-zero weights of \( W_1 \):
     - Check if the monotonicity of \( W_1 + W_2 \) and \( W_2 \) is preserved.
     - If preserved, continue with \( E_1 \); otherwise, update \( D_1 \) and \( E_1 \) as described above.
   - If none of the indexes of non-zero weights of \( W_2 \) is a subset or equal set of indexes of non-zero weights of \( W_1 \):
     - Compute the dictionary \( D_2 \) separately.
   - If the indexes of non-zero weights of \( W_2 \) have a non-zero intersection with the indexes of non-zero weights of \( W_1 \):
     - Again, compute the dictionary \( D_2 \) separately.

This formal description outlines the procedure for adaptively updating the encoding scheme and dictionary based on changes in the weight vectors of chunks of text. It accounts for scenarios where the monotonicity changes and where the sets of non-zero weights intersect or are disjoint between weight vectors.

Now we can recursively keep on storing the dictionary by noting the changes being made so we dont have to collectively store a complete dictionary everytime we add a new chunk of data which will make the decoding a simple recursive process 


1. **Initial Encoding Tree**: 
   - Adaptive Huffman encoding starts with an initial encoding tree that represents a fixed initial dictionary mapping characters to binary codes. This initial tree is commonly constructed using a predefined method like ASCII or fixed-length codes.

2. **Tree Update on New Symbol Arrival**: 
   - As new symbols are encountered in the input stream, the encoding tree is updated dynamically. If the new symbol is encountered for the first time, it is added to the encoding tree with a new code. If the symbol has been seen before, the encoding tree is adjusted to maintain the Huffman coding property, typically by swapping nodes to maintain the optimal encoding.

3. **Tree Traversal for Encoding**: 
   - To encode a symbol, the encoding tree is traversed from the root to the leaf node corresponding to the symbol. The binary code associated with that leaf node is then output as the encoded representation of the symbol.

4. **Dynamic Nature of the Encoding Tree**: 
   - The encoding tree evolves continuously as new symbols are encountered. This dynamic nature of the tree allows it to adapt to changes in the frequency distribution of symbols in the input stream.

5. **Implicit Dictionary Preservation**: 
   - Since the encoding tree represents a mapping from symbols to binary codes, the dictionary is implicitly preserved as the tree evolves. Each node in the tree corresponds to a symbol, and the path from the root to a leaf node represents the binary code for that symbol. Therefore, at any given point, the encoding tree encapsulates the current dictionary mapping.

6. **Chunk-Based Encoding**: 
   - While adaptive Huffman encoding does not explicitly preserve the dictionary at every chunk, it continuously updates the encoding tree based on the symbols encountered in the input stream. Therefore, the encoding scheme adapts to the characteristics of the input data dynamically, ensuring efficient compression.

