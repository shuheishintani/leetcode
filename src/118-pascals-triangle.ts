function generate(numRows: number): number[][] {
  if (numRows === 1) return [[1]];
  if (numRows === 2) return [[1], [1, 1]];

  const res: number[][] = [[1], [1, 1]];

  for (let i = 2; i < numRows; i++) {
    const aux = [];
    for (let j = 1; j < i; j++) {
      aux.push(res[i - 1][j - 1] + res[i - 1][j]);
    }
    res.push([1, ...aux, 1]);
  }

  return res;
}
