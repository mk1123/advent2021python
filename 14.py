from aocd import lines  # type: ignore
import utils
from typing import Generator, cast, List, Dict, Tuple
import itertools
from collections import Counter

doing_part_a = False
actually_submit = True
sample = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

if not actually_submit:
    typed_lines = sample.split("\n")
else:
    typed_lines = cast(List[str], lines)

template = typed_lines[0]
rules = {}
for line in typed_lines[2:]:
    split = line.split(" -> ")
    rules[split[0]] = split[1]


def pairwise(string: str) -> Generator[str, None, None]:
    for i in range(len(string) - 1):
        yield string[i : i + 2]


def a() -> int:
    num_steps = 10
    global template
    for _ in range(num_steps):
        template_list = []
        for pair in pairwise(template):
            template_list.append(pair[0])
            if pair in rules:
                template_list.append(rules[pair])
        template_list.append(template[-1])
        template = "".join(template_list)
    counter = Counter(template)
    common_elements = counter.most_common()
    return common_elements[0][1] - common_elements[-1][1]


pair_expansion_cache: Dict[Tuple[str, int], str] = {}


def get_expansion_dp(pair_str: str, num_steps: int) -> str:
    if pair_str not in rules or num_steps == 0:
        return pair_str

    if (pair_str, num_steps) in pair_expansion_cache:
        return pair_expansion_cache[(pair_str, num_steps)]

    rules_val_for_pair = rules[pair_str]
    expansion_val = get_expansion_dp(pair_str[0] + rules_val_for_pair, num_steps - 1)[
        :-1
    ] + get_expansion_dp(rules_val_for_pair + pair_str[1], num_steps - 1)
    pair_expansion_cache[pair_str, num_steps] = expansion_val
    return expansion_val


def update_counter(a: Counter, b: Counter, neg: bool = False) -> None:
    for key_b, val_b in b.items():
        if key_b:
            if key_b in a:
                if neg:
                    a[key_b] -= val_b
                else:
                    a[key_b] += val_b
            else:
                a[key_b] = val_b


def b() -> int:
    num_steps = 40
    rule_to_counter = {}
    for rule_pair in rules:
        rule_to_counter[rule_pair] = Counter(
            get_expansion_dp(rule_pair, num_steps // 2)[1:-1]
        )
    overall_counter = Counter()
    for pair_str in pairwise(template):
        first_level_expanded = get_expansion_dp(pair_str, num_steps // 2)
        for second_level_pair_str in pairwise(
            get_expansion_dp(first_level_expanded, num_steps // 2)
        ):
            update_counter(overall_counter, rule_to_counter[second_level_pair_str])
        update_counter(overall_counter, Counter(first_level_expanded))
    update_counter(overall_counter, Counter(template), neg=True)
    overall_counter[template[0]] += 1
    overall_counter[template[-1]] += 1
    print(overall_counter)
    common_elements = overall_counter.most_common()
    return common_elements[0][1] - common_elements[-1][1]


utils.submit(a() if doing_part_a else b(), actually_submit)
