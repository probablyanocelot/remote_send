import base64
import exifread


def bytes_to_string(file_read):
    with open(file_read, mode='rb') as file:
        file_bytes = base64.b64encode(file.read())
        converted_string = file_bytes.decode()

        # print('\n\n PRINTING CONVERTED STRING \n\n')
        # print(converted_string)

        return converted_string


def get_meta_data(file_read):
    """ For use with images taken by camera """
    with open(file_read, 'rb') as file:
        tags = exifread.process_file(file, )  # stop_tag="DateTimeOriginal"
        # dateTaken = tags  # ["DateTimeOriginal"]
        return tags  # dateTaken


def string_to_bytes(string, file_write):
    with open(file_write, mode='wb') as file:
        print('\n\n WRITING BYTES \n\n')
        file.write(base64.b64decode(string, ))


if __name__ == '__main__':
    file_read = 'egg.bmp'
    file_write = '1test.bmp'
    file_string = bytes_to_string(file_read)
    string_to_bytes(file_string, file_write)
