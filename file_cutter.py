import os
import sys

def bytes_to_mb(bytes):
    return bytes / (1024 * 1024)

file_path = '/Users/ramses/desktop/WikiAi/wiki_articles.txt'

def file_cutter(file_path):
    with open (file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    wiki_byte_siz  = sys.getsizeof(lines)
    file_size = os.path.getsize(file_path)

    count = 1
    file_ = 'wiki' + str(count) + '.txt'
    new_lines = []
    while len(lines) != len(new_lines):
        for line in lines:
            with open(file_, 'a') as files:
                size = bytes_to_mb(os.path.getsize(file_))
                if size <= 23:
                    files.write(line + '\n')
                    new_lines.append(line)
                    print (size)
                else:
                    count += 1
                    file_ = 'wiki' + str(count) + '.txt'
                    with open(file_, 'a') as files:
                        files.write(line + '\n')
                        new_lines.append(line)
