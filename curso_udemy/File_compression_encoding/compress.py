import base64
import zlib



format = 'utf-8'

data = open('demo.txt', 'r').read()
data_bytes = bytes(data, format)

compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
decoded_data = compressed_data.decode(format)
compressed_file = open('compressed.txt', 'w')
compressed_file.write(decoded_data)

decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
