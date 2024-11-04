def price(num_throws):
    # method2
    res = [0] * (num_throws+1)

    for t in range(1, num_throws+1):
        curr_res = 0

        for dice in range(1, 7):
            curr_res += max(curr_res, res(t-1))/6
            res[t] = curr_res

    return round(res(num_throws), 4)

    # if __name__ == '__main__':
    #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #     num_throws = int(input().strip())

    #     result = price(num_throws)

    #     fptr.write(str(result)+'\n')

    #     fptr.close()
