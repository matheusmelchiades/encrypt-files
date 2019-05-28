
def handle_file(filename, cryptFn, block_size=16):

    with open(filename, 'r+b') as _file:

        row_value = _file.read(block_size)

        while row_value:
            encrypted_value = cryptFn(row_value)

            if len(row_value) != len(encrypted_value):
                error_message = f'The value encrypted {len(encrypted_value)} has a different of plan vlaue {len(row_value)}'
                raise ValueError(error_message)

            _file.seek(- len(row_value), 1)
            _file.write(encrypted_value)
            row_value = _file.read(block_size)
