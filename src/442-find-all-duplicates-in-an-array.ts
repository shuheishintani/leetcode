function findDuplicates1(nums: number[]) {
  const memo: number[] = [];

  for (const num of nums) {
    if (memo[num] === undefined) {
      memo[num] = 1;
    } else {
      memo[num] += 1;
    }
  }

  const output: number[] = [];

  memo.map((num, i) => {
    if (num > 1) {
      output.push(i);
    }
  });

  return output;
}

function findDuplicates2(nums: number[]) {
  const hasOne: {
    [num: number]: true;
  } = {};
  const result: number[] = [];

  for (let i = 0; i < nums.length; i++) {
    if (!hasOne[nums[i]]) {
      hasOne[nums[i]] = true;
    } else {
      result.push(nums[i]);
    }
  }
  return result;
}

findDuplicates2([1, 1, 2]);
