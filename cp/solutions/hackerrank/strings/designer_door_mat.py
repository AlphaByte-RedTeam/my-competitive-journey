# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
pattern = '.|.'

if M % 3 == 0:
    # TOP
    for i in range(1, N, 2):
        print((pattern * i).center(M, '-'))

    # MIDDLE
    print('WELCOME'.center(M, '-'))

    # BOTTOM
    for i in reversed(range(1, N, 2)):
        print((pattern * i).center(M, '-'))
