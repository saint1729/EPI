import sys


def find_max_sub_array_sum_naive(l):
    n = len(l)

    if n == 0:
        return 0

    s = max(l)
    for i in range(1, n + 1):
        for j in range(0, i):
            s = max(s, sum(l[j: i]))
    return s


def find_max_sub_array_sum_naive_2(l):
    n = len(l)
    if n == 0:
        return 0
    s = [0]
    for i in range(n):
        s.append(s[i] + l[i])
    ans = max(l)
    for i in range(1, n + 1):
        for j in range(0, i):
            ans = max(ans, s[i] - s[j])
    return ans


def find_max_sub_array_sum_dnc(l):
    n = len(l)
    if n == 0:
        return 0
    m = max(l)
    if m < 0:
        return m
    return find_max_sub_array_sum_dnc_util(l, 0, n - 1)


def find_max_sub_array_sum_dnc_util(l, start, end):
    if start == end:
        return max(0, l[start])
    elif (start + 1) == end:
        return max(l[start], l[end], sum(l[start: (end + 1)]))
    else:
        mid = start + (end - start) // 2
        left_max_sum = find_max_sub_array_sum_dnc_util(l, start, mid)
        right_max_sum = find_max_sub_array_sum_dnc_util(l, mid + 1, end)
        s = compute_max_through(l, start, mid, end)
        return max(left_max_sum, right_max_sum, s)


def find_max_sub_array_sum_dnc_eff(l):
    n = len(l)
    if n == 0:
        return 0
    m = max(l)
    if m < 0:
        return m
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[i] + l[i])
    return find_max_sub_array_sum_dnc_eff_util(l, 0, n - 1, prefix_sum)


def find_max_sub_array_sum_dnc_eff_util(l, start, end, prefix_sum):
    if start == end:
        return max(0, l[start])
    elif (start + 1) == end:
        return max(l[start], l[end], sum(l[start: (end + 1)]))
    else:
        mid = start + (end - start) // 2
        left_max_sum = find_max_sub_array_sum_dnc_eff_util(l, start, mid, prefix_sum)
        right_max_sum = find_max_sub_array_sum_dnc_eff_util(l, mid + 1, end, prefix_sum)
        s = compute_max_through_prefix(start, mid, end, prefix_sum)
        return max(left_max_sum, right_max_sum, s)


def compute_max_through(l, start, mid, end):
    s, left_ans, right_ans = 0, 0, 0
    for i in range(mid, start - 1, - 1):
        s += l[i]
        left_ans = max(left_ans, s)
    s = 0
    for i in range(mid + 1, end + 1):
        s += l[i]
        right_ans = max(right_ans, s)
    return left_ans + right_ans


def compute_max_through_prefix(start, mid, end, prefix_sum):
    left_ans, right_ans = 0, 0
    for i in range(mid, start - 1, - 1):
        left_ans = max(left_ans, prefix_sum[mid + 1] - prefix_sum[i])
    for i in range(mid + 1, end + 1):
        right_ans = max(right_ans, prefix_sum[i + 1] - prefix_sum[mid + 1])
    return left_ans + right_ans


def find_maximum_subarray_dp(l):
    n = len(l)
    if n == 0:
        return 0
    m = max(l)
    if m < 0:
        return m
    min_sum = max_sum = running_sum = 0
    for i in range(n):
        running_sum += l[i]
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum


if __name__ == '__main__':
    tests = [[904, 40, 523, 12, -335, -385, -124, 481, -31], [], [1],
             [1, 2, 3, 4, 5], [-1, 2, 3, 4, 5], [1, 2, 3, 4, -5],
             [-1, 2, 3, 4, -5], [-1, 2, -3, 4, -5], [-1, -2, -3, 4, -5],
             [-1, -2, -3, -4, -5], [-1, 3, -2, 4, -5], [1, 2, -3, -5, 10, 20, -9],
             [1, 9, -3, 5, -10, 20, -9], [2, -4, 9, 5, 10, 20, -9],
             [-2, 4, 9, -5, 10, -20, 9]]
    answers1 = []
    for x in tests:
        answers1.append(find_max_sub_array_sum_naive(x))
    print(answers1)

    # tests = [[-1, 3, -2, 4, -5]]
    answers2 = []
    for x in tests:
        answers2.append(find_max_sub_array_sum_naive_2(x))
    print(answers2)

    answers3 = []
    for x in tests:
        answers3.append(find_max_sub_array_sum_dnc(x))
    print(answers3)

    answers4 = []
    for x in tests:
        answers4.append(find_max_sub_array_sum_dnc_eff(x))
    print(answers4)

    answers5 = []
    for x in tests:
        answers5.append(find_maximum_subarray_dp(x))
    print(answers5)


    # print(find_max_sub_array_sum_naive([904, 40, 523, 12, -335, -385, -124, 481, -31]))
