function addDigits(num: number): number {
  if (num < 10) {
    return num;
  }
  const added = num
    .toString()
    .split("")
    .map((str) => parseInt(str))
    .reduce((a, b) => a + b);

  return addDigits(added);
}

function addDigits2(num: number) {
  while (num >= 10) {
    let t = num;
    num = 0;
    while (t > 0) {
      num += t % 10;
      t = Math.floor(t / 10);
    }
  }
  return num;
}

function addDigits3(num: number) {
  if (num < 10) return num;
  return num % 9 === 0 ? 9 : num % 9;
}

console.log(addDigits3(38));
