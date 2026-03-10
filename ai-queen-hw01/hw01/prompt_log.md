# AI协作八皇后作业交互日志
## 步骤1：生成八皇后求解器
### 给AI的Prompt：
帮我实现Python版八皇后问题的回溯求解器，要求：
1. 代码保存到src/queen_solver.py中；
2. 实现函数solve_n_queens(n: int) -> list[list[int]]，返回所有合法解；
3. 每个解用列表表示，索引=行，值=列（从0开始）；
4. 代码加详细注释，适配Python 3.8。

### AI返回的核心代码：
[粘贴queen_solver.py最初的完整代码]

## 步骤2：生成单元测试
### 给AI的Prompt：
帮我为src/queen_solver.py写单元测试，要求：
1. 保存到tests/test_queen_solver.py；
2. 使用pytest框架，适配Python 3.8；
3. 测试用例：n=1（解数1）、n=2（解数0）、n=4（解数2）、n=8（解数92）。

### AI返回的测试代码：
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

## 步骤3：引入Bug并请求AI修复
### 手动引入的Bug：
将queen_solver.py中核心判断条件的 `col not in used_cols` 改为 `col in used_cols`，逻辑完全相反。

### 给AI的修复Prompt：
我修改了八皇后求解器的代码后，所有测试都失败了，帮我定位并修复Bug。
有Bug的代码片段：
def backtrack(row: int, current_solution: list[int]):
    if row == n:
        solutions.append(current_solution.copy())
        return
    for col in range(n):
        if col in used_cols and (row - col) not in used_diag1 and (row + col) not in used_diag2:
            used_cols.add(col)
            used_diag1.add(row - col)
            used_diag2.add(row + col)
            current_solution.append(col)
            backtrack(row + 1, current_solution)
            current_solution.pop()
            used_cols.remove(col)
            used_diag1.remove(row - col)
            used_diag2.remove(row + col)

### AI的修复分析：
这个Bug出现在皇后放置的核心判断逻辑中，原本应该判断“当前列未被占用（col not in used_cols）”，但被错误改为“当前列已被占用（col in used_cols）”，导致程序只会往已被占用的列放皇后，完全不符合八皇后规则，因此所有测试用例都会失败。

### AI修复后的代码片段：
将错误的判断条件改回：
if col not in used_cols and (row - col) not in used_diag1 and (row + col) not in used_diag2: