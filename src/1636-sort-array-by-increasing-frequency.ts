function frequencySort1(nums: number[]) {
  const hashMap: { [key: number]: number } = {};
  for (const num of nums) {
    if (num in hashMap) {
      hashMap[num] += 1;
    } else {
      hashMap[num] = 1;
    }
  }

  const matrix: number[][] = [];

  for (const key in hashMap) {
    if (hashMap.hasOwnProperty(key)) {
      if (!matrix[hashMap[key]]) {
        matrix[hashMap[key]] = [parseInt(key)];
      } else {
        matrix[hashMap[key]].push(parseInt(key));
      }
    }
  }

  const result: number[] = [];

  matrix.forEach((nums, freq) => {
    nums
      .sort((a, b) => b - a)
      .forEach((num) => {
        for (let i = 1; i <= freq; i++) {
          result.push(num);
        }
      });
  });

  return result;
}

function frequencySort2(nums: number[]) {
  const map = new Map();
  for (let n of nums) {
    map.set(n, (map.get(n) || 0) + 1);
  }
  return nums.sort((a, b) => {
    if (map.get(a) === map.get(b)) {
      return b - a;
    } else {
      return map.get(a) - map.get(b);
    }
  });
}
