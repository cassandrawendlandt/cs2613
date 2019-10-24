
import humansize 



def approximate_size(size, a_kilobyte_is_1024_bytes=False):

    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True, use multiples of 1024
                                if False (default), use multiples of 1000

    Returns: string

    '''

    return humansize.approximate_size (size, a_kilobyte_is_1024_bytes)


if __name__ == '__main__':
    print(approximate_size(1000000000000, True))
    print(approximate_size(1000000000000))

