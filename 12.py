from collections import defaultdict
from aocd import lines  # type: ignore
import utils
import string
from typing import Dict, Set, cast, List

doing_part_a = False
actually_submit = True
sample = """"""

if not actually_submit:
    typed_lines = sample.split("\n")
else:
    typed_lines = cast(List[str], lines)

graph: Dict[str, List[str]] = defaultdict(list)
small: Set[str] = set()
visited: Set[str] = set()
num_paths = 0

for line in typed_lines:
    nodes = line.split("-")
    node_1, node_2 = nodes[0], nodes[1]
    if node_1.islower():
        small.add(node_1)
    if node_2.islower():
        small.add(node_2)
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)


def visit_a(node: str) -> None:
    if node == "end":
        global num_paths
        num_paths += 1
    else:
        if node in small:
            visited.add(node)
        for child in graph[node]:
            if not child in visited:
                visit_a(child)
        if node in small:
            visited.remove(node)


have_assigned_double_node = False
path: List[str] = []
all_paths = set()


def visit_b(node: str) -> None:
    global path
    if node == "end":
        all_paths.add(tuple(path))
    else:
        global have_assigned_double_node
        if (
            not have_assigned_double_node
            and node in small
            and node not in {"start", "end"}
        ):
            # current node will be the node that can be visited twice
            have_assigned_double_node = True
            path.append(node)
            for child in graph[node]:
                if not child in visited:
                    visit_b(child)
            have_assigned_double_node = False
            path.pop()
        path.append(node)
        if node in small:
            visited.add(node)
        for child in graph[node]:
            if not child in visited:
                visit_b(child)
        if node in small:
            visited.remove(node)
        path.pop()


def a() -> int:
    visit_a("start")
    return num_paths


def b() -> int:
    visit_b("start")
    return len(all_paths)


utils.submit(a() if doing_part_a else b(), actually_submit)
