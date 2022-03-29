def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        print(t[0])
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    print(nums)
    print(words)
    return (min_n, max_n, unique_words)
t = ((1, "hi"), (2, "hello"), (3, "bye"))
print(get_data(t))
print(t[0])
print(t[1])
print(t[2])
"""이 함수에서 for문과 if문이 어떤 역할을 하는지 설명하기"""
"""for문: 반복해서 t 안에 있는 원소를 더함 if문: 문자가 아니라면 숫자를 더함"""