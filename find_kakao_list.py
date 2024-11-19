def extract_lines_with_phrase(input_file_path, output_file_path, phrase):
    """
    Extracts lines containing the specified phrase from the input file and writes them to the output file.
    
    :param input_file_path: Path to the input text file
    :param output_file_path: Path to the output text file
    :param phrase: Phrase to search for in the input text file
    """
    word_to_find = phrase
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if phrase in line:
                    words = line.split()
                    word_to_find2 = ":"
                    wordString = ''.join(words)
                    word_index = wordString.find(word_to_find)
                    word_index2 = wordString.find(word_to_find2)
                    if word_index > 0:
                        preceding_word = wordString
                        print(preceding_word)
                        outfile.write(f"{preceding_word}\n")
        print(f"Lines containing '{phrase}' and the word '{word_to_find}' have been processed.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file_path = input("Enter the path to the input text file: ")
    output_file_path = input("Enter the path to the output text file: ")
    phrase = input("Enter the find to word: ")

    extract_lines_with_phrase(input_file_path, output_file_path, phrase)