function minCostClimbingStairs(cost: number[]): number {
  const minCost = [0, 0];

  for (let i = 2; i <= cost.length; i++) {
    minCost[i] = Math.min(
      minCost[i - 1] + cost[i - 1],
      minCost[i - 2] + cost[i - 2]
    );
  }

  return minCost[minCost.length - 1];
}

function minCostClimbingStairs2(cost: number[]): number {
  let downOne = 0;
  let downTwo = 0;

  for (let i = 2; i <= cost.length; i++) {
    [downOne, downTwo] = [
      Math.min(downOne + cost[i - 1], downTwo + cost[i - 2]),
      downOne,
    ];
  }
  return downOne;
}
