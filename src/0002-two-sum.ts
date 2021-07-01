function twoSum1(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  throw new Error("No two sum solution");
}

function twoSum2(nums: number[], target: number): number[] {
  const map = new Map();
  nums.forEach((num, i) => {
    map.set(num, i);
  });

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.get(complement) && map.get(complement) !== i) {
      return [i, map.get(complement)];
    }
  }

  throw new Error("No two sum solution");
}
