from ex7_helper import*
from typing import List, Any

def mult(x: float, y: int) -> float:
    if y == 0:
        return 0.0
    if x == 0:
        return 0.0
    if y == 1:
        return x
    else:
        return add(x, mult(x, subtract_1(y)))


def is_even(n: int) -> bool:
    if n == 0:
        return True
    if n == 1:
        return False
    else:
        return is_even(subtract_1(subtract_1(n)))


def log_mult(x: float, y: int) -> float:
    if x == 0:
        return 0
    if y == 0:
        return 0
    if y == 1:
        return x
    if not is_odd(y):
        return add(log_mult(x, divide_by_2(y)), log_mult(x, divide_by_2(y)))
    else:
        return add(x, add(log_mult(x, divide_by_2(y)), log_mult(x, divide_by_2(y))))


def helper_is_power(i: int, b: int, x: int) -> bool:
    if x < i:
        return False
    elif x > i:
        return helper_is_power(i * b, b, x)
    elif x == i:
        return True
    return False


#ناقصها تناي واحد والا الوظيفة تسكرتتت كله فل
def is_power(b: int, x: int) -> bool:
    if x == 0 and b == 0:
        return True
    if x == 0 and b != 0:
        return False
    if b < 0:
        return False
    if x < 0:
        return False
    if x == 1:
        return True
    if b == x:
        return True
    if b == 1 and x != 1:
        return False
    return helper_is_power(b, b, x)


def reverse(s: str) -> str:
    if len(s) == 0 or len(s) == 1:
        return s
    return append_to_end(reverse(s[1:]), s[0])



def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    if n > 0:
        play_hanoi(Hanoi, n-1, src, temp, dst)
        Hanoi.move(src, dst)
        play_hanoi(Hanoi, n - 1, temp, dst, src)
        return None
    if n == 0:
        return None
    if n < 0:
        return None


def helper_num_of_ones(n: int, i: int, counter: int) -> int:
    d = i * 10
    c = i * (n // d)
    counter += (c + min(max(n % d - i + 1, 0), i))
    if i >= n:
        return counter
    return helper_num_of_ones(n, i * 10, counter)

def number_of_ones(n: int) -> int:
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n < 10:
        return 1
    if n == 10:
        return 2
    else:
        return helper_num_of_ones(n, 1, 0)


def helper_compare_2d_lists(l1: List[Any], l2: List[Any], length_1: int, length_2: int, i: int) -> bool:
    if length_1 != length_2:
        return False
    if i >= length_2 or i >= length_1:
        return True
    if l1[i] != l2[i]:
        return False
    return helper_compare_2d_lists(l1, l2, length_1, length_2, i + 1)



def compare_2d_lists(l1: List[List[Any]], l2: List[List[Any]]) -> bool:

    if len(l1) != len(l2):
        return False
    if not l2:
        return True
    return helper_compare_2d_lists(l1[0], l2[0], len(l1[0]), len(l2[0]), 0) and \
           compare_2d_lists(l1[1:], l2[1:])


def deep(lst: List[List[Any]]) -> List[List[Any]]:
    if not isinstance(lst, list):
        return lst
    else:
        if len(lst) != 0:
            return [deep(lst[0])] + deep(lst[1:])
        return []

def magic_list(n: int) -> List[List[Any]]:
    if n == 0:
        return []
    if n == 1:
        return [[]]
    else:
        pre = magic_list(n - 1)
        return deep(pre) + [deep(pre)]
