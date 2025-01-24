def slidigz_window(arr, k):
    result = []
    window_start = 0
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            result.append(window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return result