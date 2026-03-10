def solve_n_queens(n: int) -> list[list[int]]:
    """
    求解n皇后问题，返回所有合法解
    参数n：棋盘的行数/列数
    返回值：列表的列表，每个子列表代表一个解，索引为行，值为列（0开始）
    """
    solutions = []  # 存储所有合法解
    used_cols = set()  # 记录已使用的列
    used_diag1 = set()  # 记录已使用的对角线（行-列 固定）
    used_diag2 = set()  # 记录已使用的对角线（行+列 固定）

    def backtrack(row: int, current_solution: list[int]):
        """回溯函数，逐行放置皇后"""
        # 终止条件：所有行都放好皇后，保存解
        if row == n:
            solutions.append(current_solution.copy())
            return
        
        # 遍历当前行的每一列，尝试放置皇后
        for col in range(n):
            # 检查列和两个对角线是否已被占用
            if col not in used_cols and (row - col) not in used_diag1 and (row + col) not in used_diag2:
                # 标记占用
                used_cols.add(col)
                used_diag1.add(row - col)
                used_diag2.add(row + col)
                current_solution.append(col)
                
                # 递归处理下一行
                backtrack(row + 1, current_solution)
                
                # 回溯：撤销标记
                current_solution.pop()
                used_cols.remove(col)
                used_diag1.remove(row - col)
                used_diag2.remove(row + col)

    # 从第0行开始回溯
    backtrack(0, [])
    return solutions
