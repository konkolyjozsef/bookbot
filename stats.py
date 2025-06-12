def get_num_words(text):
    words = text.split()
    return len(words)


def get_text_string(text):
    char_count = {}
    small_text = text.lower()
    for char in small_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_text(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=lambda d: d["num"])
    return char_list


    