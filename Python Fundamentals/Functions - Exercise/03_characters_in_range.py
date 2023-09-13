def get_chars(start, end):
    result = ""
    for char in range(ord(start) + 1, ord(end)):
        result += f"{chr(char)} "
    return result


start_ch = input()
end_ch = input()
print(get_chars(start_ch, end_ch))
