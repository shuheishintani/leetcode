function reverse1(x: number): number {
  if (x === 0) {
    return 0;
  }
  let negative = false;
  const numArray = x
    .toString()
    .split("")
    .map((str) => parseInt(str, 10));
  if (x < 0) {
    negative = true;
    numArray.shift();
  }
  const reversedNum = numArray.reduce((a, b, i) => a + b * Math.pow(10, i));
  const output = negative ? -reversedNum : reversedNum;
  return output >= -(2 ** 31) && output <= 2 ** 31 - 1 ? output : 0;
}

function reverse2(x: number): number {
  let output = parseInt(x.toString().split("").reverse().join(""));
  return output >= -(2 ** 31) && output <= 2 ** 31 - 1
    ? output * Math.sign(x)
    : 0;
}

function reverse3(x: number): number {
  const MAX_INTEGER = 2 ** 31 - 1;
  const MIN_INTEGER = -(2 ** 31);

  let rev = 0;
  while (x !== 0) {
    const pop = x % 10;
    x = Math.trunc(x / 10);
    if (rev > MAX_INTEGER / 10 || (rev === MAX_INTEGER / 10 && pop > 7)) {
      return 0;
    }
    if (rev < MIN_INTEGER / 10 || (rev === MIN_INTEGER / 10 && pop < -8)) {
      return 0;
    }
    rev = rev * 10 + pop;
  }
  return rev;
}
