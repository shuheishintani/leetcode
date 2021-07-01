function uniquePaths1(m: number, n: number): number {
  let a = Math.min(m, n) - 1;
  let b = m + n - 2;

  if (a === 0) {
    return 1;
  }

  let tmp = a;
  let tmpA = 1;
  let tmpB = 1;

  for (let i = 0; i < tmp; i++) {
    tmpA *= a;
    tmpB *= b;
    a--;
    b--;
  }

  return tmpB / tmpA;
}

function uniquePaths2(m: number, n: number): number {
  let dp = new Array(m + 1).fill(1).map(() => new Array(n + 1).fill(0));
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (i == 1 && j == 1) dp[i][j] = 1;
      else dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }
  return dp[m][n];
}

console.log(uniquePaths2(7, 3));
