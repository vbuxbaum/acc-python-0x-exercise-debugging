def lines_with_word_occurrences(file_path: str, word: str):
    str_lines = read_file_lines(file_path)
    result = []
    for index, line in enumerate(str_lines, start=1):
        if word.casefold() in line.casefold():
            result.append(index)
        else:
            str_lines.remove(line)
    return result


def read_file_lines(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    return file_content.split()


def main():
    file_path = "data/word_finder.txt"
    search_word = "python"
    occurrences = lines_with_word_occurrences(file_path, search_word)
    print(
        f'A palavra "{search_word}" ocorre nas seguintes linhas do arquivo:',
        occurrences,
    )


if __name__ == "__main__":
    main()
