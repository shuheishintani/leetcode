function topKFrequent(nums: number[], k: number): number[] {
  const map = new Map();

  nums.forEach((num) => {
    map.set(num, (map.get(num) || 0) + 1);
  });

  const set = new Set(nums.sort((a, b) => map.get(b) - map.get(a)));
  const arr = Array.from(set);

  return arr.slice(0, k);
}
