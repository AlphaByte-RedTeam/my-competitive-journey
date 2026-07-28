if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        command = input().split()
        instructions = command[0].lower()

        if instructions == "insert".lower():
            position = int(command[1])
            value = int(command[2])
            arr.insert(position, value)
        elif instructions == "print".lower():
            print(arr)
        elif instructions == "remove".lower():
            value = int(command[1])

            if value in arr:
                arr.remove(value)
        elif instructions == "append".lower():
            value = int(command[1])
            arr.append(value)
        elif instructions == "sort".lower():
            arr.sort()
        elif instructions == "pop".lower():
            arr.pop()
        elif instructions == "reverse".lower():
            arr.reverse()
        else:
            print("Instructions not recognized")
