import re
# a function to read a block of text and split each sentence to a new line
def split_text(text):
    # regex to split a string on any punctuation
    text = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)

    # remove empty strings
    text = [x for x in text if x]
    # remove leading and trailing spaces
    text = [x.strip() for x in text]

    # return text with each sentence on a new line
    return '\n'.join(text)


if __name__ == "__main__":
    file_name = './whisper/base_trans'
    file_suffix = '.txt'
    # read text from file
    with open(f'{file_name}{file_suffix}', 'r') as f:
        text = f.read()
    # split text
    text = split_text(text)
    # write text to file
    with open(f'{file_name}_2{file_suffix}', 'w') as f:
        f.write(text)