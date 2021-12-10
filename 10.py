from aocd import lines  # type: ignore
import utils
from typing import List, cast

doing_part_a = False
actually_submit = True
sample = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
part_b_score_map = {")": 1, "]": 2, "}": 3, ">": 4}
closing_to_opening = {")": "(", "}": "{", "]": "[", ">": "<"}
opening_to_closing = {v: k for k, v in closing_to_opening.items()}
closing = closing_to_opening.keys()
opening = closing_to_opening.values()

if not actually_submit:
    typed_lines = sample.split("\n")
else:
    typed_lines = cast(List[str], lines)


def a() -> int:
    score = 0
    for line in typed_lines:
        chars = list(line)
        stack = []
        for char in chars:
            if char in opening:
                stack.append(char)
            else:
                if closing_to_opening[char] != stack.pop():
                    score += score_map[char]
    return score


def b() -> int:
    scores = []
    for line in typed_lines:
        chars = list(line)
        stack: List[str] = []
        valid_line = True
        for char in chars:
            if char in opening:
                stack.append(char)
            else:
                if closing_to_opening[char] != stack.pop():
                    valid_line = False
                    break
        if not valid_line:
            continue
        curr_score = 0
        for opening_char in stack[::-1]:
            curr_score *= 5
            curr_score += part_b_score_map[opening_to_closing[opening_char]]
        scores.append(curr_score)
    return sorted(scores)[len(scores) // 2]


utils.submit(a() if doing_part_a else b(), actually_submit)
