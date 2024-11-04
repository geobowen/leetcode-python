def price(num_throws):
    # method1
    if num_throws == 1:
        return 3.5
    else:
        expected_payoff = 0
        for i in range(1, 7):
            expected_payoff += max(i, price(num_throws-1))/6
        return round(expected_payoff, 4)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     num_throws = int(input().strip())

#     result = price(num_throws)

#     fptr.write(str(result)+'\n')

#     fptr.close()
