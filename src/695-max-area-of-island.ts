function maxAreaOfIsland(grid: number[][]) {
  if (grid.length === 0) {
    return 0;
  }

  let maxArea = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        const area = dfs(grid, i, j);
        if (maxArea < area) {
          maxArea = area;
        }
      }
    }
  }
  return maxArea;
}

export const dfs = (grid: number[][], i: number, j: number): number => {
  if (
    i < 0 ||
    i >= grid.length ||
    j < 0 ||
    j >= grid[i].length ||
    grid[i][j] === 0
  ) {
    return 0;
  }

  grid[i][j] = 0;

  const w = dfs(grid, i, j + 1);
  const e = dfs(grid, i, j - 1);
  const n = dfs(grid, i + 1, j);
  const s = dfs(grid, i - 1, j);

  return w + e + n + s + 1;
};

console.log(
  maxAreaOfIsland([
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
  ])
);
