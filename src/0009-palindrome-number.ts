function isPalindrome1(x: number): boolean {
  const strX = x.toString();
  return strX === strX.split("").reverse().join("");
}

function isPalindrome2(x: number): boolean {
  if (x < 0) return false;

  let y = x;
  let rev = 0;

  while (y !== 0) {
    const rem = y % 10;
    rev = rev * 10 + rem;
    y = Math.trunc(y / 10);
  }

  return rev === x;
}
