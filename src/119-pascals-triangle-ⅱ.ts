function getRow(rowIndex: number): number[] {
  const res: number[][] = [[1], [1, 1]];

  for (let i = 2; i <= rowIndex; i++) {
    const aux = [];
    for (let j = 1; j < i; j++) {
      aux.push(res[i - 1][j] + res[i - 1][j - 1]);
    }
    res.push([1, ...aux, 1]);
  }

  return res[rowIndex];
}
