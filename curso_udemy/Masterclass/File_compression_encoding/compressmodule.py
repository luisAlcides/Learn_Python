import zlib
import base64


def compress(inputfile, outputfile, format='utf-8'):
    data = open(inputfile, 'r').read()
    data_bytes = bytes(data, format)

    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
    decoded_data = compressed_data.decode(format)
    compressed_file = open(outputfile, 'w')
    compressed_file.write(decoded_data)


def decompress(inputfile, outputfile, format='utf-8'):
    file_content = open(inputfile, 'r').read()
    encoded_data = file_content.encode(format)
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode(format)
    file = open(outputfile, 'w')
    file.write(decoded_data)
    file.close()


decompress('ot.txt', 'dc1.txt')
