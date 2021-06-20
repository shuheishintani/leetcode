function intersection(nums1: number[], nums2: number[]): number[] {
  const set1 = new Set(nums1);
  const set2 = new Set(nums2);

  let output: number[] = [];

  set2.forEach((num) => {
    if (set1.has(num)) {
      output.push(num);
    }
  });

  return output;
}
