function numIslands(grid: string[][]): number {
  if (grid.length === 0) {
    return 0;
  }

  let numIslands = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === "1") {
        numIslands += dfs(grid, i, j);
      }
    }
  }

  return numIslands;
}

const dfs = (grid: string[][], i: number, j: number) => {
  if (
    i < 0 ||
    i >= grid.length ||
    j < 0 ||
    j >= grid[i].length ||
    grid[i][j] === "0"
  ) {
    return 0;
  }

  grid[i][j] = "0";
  dfs(grid, i + 1, j);
  dfs(grid, i - 1, j);
  dfs(grid, i, j + 1);
  dfs(grid, i, j - 1);

  return 1;
};
