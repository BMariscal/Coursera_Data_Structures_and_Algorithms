# python3

def max_pairwise_product(numbers):
    # O(n) space and O(n) time
    maxi_num = max(numbers)
    new_list = []

    for i in numbers:
        if i != maxi_num:
            new_list.append(i)

    return max(new_list) * maxi_num


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
