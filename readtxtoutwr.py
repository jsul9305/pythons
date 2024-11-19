def extract_lines_with_phrase(input_file_path, output_file_path):
    word_to_find = " "
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                cnt = 0
                words = line.split()
                for word in words:
                    outfile.write(f"{word}\n")
                    cnt += 1
                outfile.write(f"{cnt}\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file_path = input("Enter the path to the input text file: ")
    output_file_path = input("Enter the path to the output text file: ")

    extract_lines_with_phrase(input_file_path, output_file_path)