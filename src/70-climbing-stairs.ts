function climbStairs1(n: number): number {
  if (n === 1) {
    return 1;
  }
  if (n === 2) {
    return 2;
  }
  return climbStairs1(n - 1) + climbStairs1(n - 2);
}

function climbStairs2(n: number): number {
  const memo = [];
  memo[1] = 1;
  memo[2] = 2;

  if (n === 1) {
    return 1;
  }
  if (n === 2) {
    return 2;
  }

  for (let i = 3; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2];
  }
  return memo[n];
}

function climbStairs3(n: number): number {
  if (n === 1) {
    return 1;
  }
  let first = 1;
  let second = 2;

  for (let i = 3; i <= n; i++) {
    const third = first + second;
    first = second;
    second = third;
  }
  return second;
}
