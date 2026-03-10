import pytest
from src.queen_solver import solve_n_queens

# 测试n=1的情况（只有1个解）
def test_n_queens_1():
    assert solve_n_queens(1) == [[0]]

# 测试n=2的情况（无解）
def test_n_queens_2():
    assert solve_n_queens(2) == []

# 测试n=4的情况（2个解）
def test_n_queens_4():
    solutions = solve_n_queens(4)
    assert len(solutions) == 2
    assert [1, 3, 0, 2] in solutions
    assert [2, 0, 3, 1] in solutions

# 测试n=8的情况（92个解）
def test_n_queens_8():
    assert len(solve_n_queens(8)) == 92