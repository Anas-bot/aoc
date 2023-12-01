with open("input.txt", "r") as f:
    lines = f.readlines()

digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]


def part_one_two(lines_):
    sum = 0
    for line in lines_:
        nums = []
        for index, ch in enumerate(line):
            if ch.isdigit():
                nums.append(ch)

            for idx, word in enumerate(digits):
                if line[index:].startswith(word):
                    nums.append(str(idx + 1))
        sum += int(nums[0] + nums[-1])

    return sum
