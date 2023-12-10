def read_lines_from_file(file_path, delimiter=None):
    with open(file_path, 'r') as file:
        if delimiter:
            return [line.strip().split(delimiter) for line in file if line.strip()]
        else:
            return [line.strip() for line in file if line.strip()]
