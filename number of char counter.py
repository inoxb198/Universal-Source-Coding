import numpy as np

def count_ascii_characters(page_content):
    # Initialize a list to store the counts of ASCII characters
    ascii_counts = [0] * 128  # Initialize with zeros for ASCII characters 0 to 127

    # Iterate over each character in the page content
    for char in page_content:
        # Check if the character is an ASCII character
        ascii_val = ord(char)
        if ascii_val < 128:
            # Increment the count for the ASCII character
            ascii_counts[ascii_val] += 1

    return ascii_counts

def create_ascii_frequency_matrix(book_file):
    ascii_frequency_matrix = []

    # Open the book file and read its contents page by page
    with open('C:\\Users\\inoxb\\Downloads\\input.txt', 'r', encoding='utf-8') as file:
        for page_content in file:
            # Count the ASCII characters in the page
            page_ascii_counts = count_ascii_characters(page_content)

            # Append the ASCII frequency counts of the page to the matrix
            ascii_frequency_matrix.append(page_ascii_counts)

    # Convert the list of lists to a numpy array (matrix)
    ascii_frequency_matrix = np.array(ascii_frequency_matrix)

    return ascii_frequency_matrix

# Example usage: Replace 'book.txt' with the path to your book file
book_file_path = 'C:\\Users\\inoxb\\Downloads\\input.txt'
ascii_frequency_matrix = create_ascii_frequency_matrix(book_file_path)

# Print the ASCII frequency matrix
print("ASCII Frequency Matrix:")
print(ascii_frequency_matrix)
