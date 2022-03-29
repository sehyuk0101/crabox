def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)
t = ((1, "hi"), (2, "hello"), (3, "bye"))
print(get_data(t))
print(t[0])
print(t[1])
print(t[2])