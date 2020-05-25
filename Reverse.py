def reverse(str):
  return str[::-1]
def reverse_word(s):
    s1 = s.split(' ')
    i, j = 0, len(s1)-1
    while i < j:
        s1[i], s1[j] = s1[j], s1[i]
        i += 1
        j -= 1
    return ' '.join(s1)


if __name__=="__main__":
    str = input()
    s = reverse(str)
    print(reverse_word(s))
