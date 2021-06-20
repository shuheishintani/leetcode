function permute(nums: number[]): number[][] {
  if (nums.length === 1) {
    return [nums];
  }

  let output: number[][] = [];

  for (const num of nums) {
    const sub = nums.filter((n) => n !== num);
    const subPermute = permute(sub);
    subPermute.forEach((s) => {
      output.push([num, ...s]);
    });
  }

  return output;
}

const permute2 = function (nums: number[]) {
  const result: number[][] = [];
  const temp: number[] = [];
  findPermutations(temp, nums, result);
  return result;
};

const findPermutations = (
  temp: number[],
  nums: number[],
  result: number[][]
) => {
  if (!nums.length) {
    result.push(temp.concat());
    return;
  }

  for (var i = 0; i < nums.length; i++) {
    const newNum = nums[i];
    temp.push(newNum);
    nums.splice(i, 1);
    findPermutations(temp, nums, result);
    temp.pop();
    nums.splice(i, 0, newNum);
  }

  console.log(result);
};

permute2([1, 2, 3]);
