function moveZeroes(nums: number[]): void {
  let countZero = 0;
  const numlen = nums.length;
  for (let i = 0; i < numlen; i++) {
    if (nums[0] === 0) {
      nums.shift();
      countZero++;
    } else {
      const peak = nums.shift();
      if (peak) {
        nums.push(peak);
      }
    }
  }
  const zeroArray: number[] = new Array(countZero).fill(0);
  nums.push(...zeroArray);
}

function moveZeroes2(nums: number[]): void {
  let index = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      nums[index++] = nums[i];
    }
  }
  for (let i = index; i < nums.length; i++) {
    nums[i] = 0;
  }
}

console.log(moveZeroes([0, 1, 0, 3, 12]));
