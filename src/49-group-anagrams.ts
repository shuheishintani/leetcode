function groupAnagrams(strs: string[]): string[][] {
  const map = new Map();

  for (const str of strs) {
    const sorted = str.split("").sort().join("");
    if (map.get(sorted)) {
      const prev = map.get(sorted);
      map.set(sorted, [...prev, str]);
    } else {
      map.set(sorted, [str]);
    }
  }

  let output: string[][] = [];

  map.forEach((v) => {
    output.push(v);
  });

  return output;
}
