if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # Solution not accepted because the hash() functions algorithm different in Pypy3 and Python 3.
    # Both runtime are not accepted.

    # Update: use Python 2 runtim
    t = tuple(integer_list)
    print(hash(t))
