def phoneNumberMnemonics(phoneNumber):
    # helper data structure
    DIGIT_LETTERS = {
        "0": ["0"],
        "1": ["1"],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def backtrack(index, path):
        if len(path) == len(phoneNumber):
            res.append("".join(path))
            return
        for char in DIGIT_LETTERS[phoneNumber[index]]:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()

    res = []
    if phoneNumber:
        backtrack(0, [])
    return res


print(phoneNumberMnemonics(str(1905)))
