function romanToInt1(s: string, carryOver: number = 0): number {
  if (s.length === 0) {
    return carryOver;
  }

  const rev = s.split("");
  const peak = rev.shift();

  if (peak === "M") {
    carryOver += 1000;
  }
  if (peak === "D") {
    carryOver += 500;
  }
  if (peak === "L") {
    carryOver += 50;
  }
  if (peak === "V") {
    carryOver += 5;
  }

  if (peak === "C") {
    const next = rev[0];
    if (next === "M") {
      rev.shift();
      carryOver += 900;
    } else if (next === "D") {
      rev.shift();
      carryOver += 400;
    } else {
      carryOver += 100;
    }
  }

  if (peak === "X") {
    const next = rev[0];
    if (next === "C") {
      rev.shift();
      carryOver += 90;
    } else if (next === "L") {
      rev.shift();
      carryOver += 40;
    } else {
      carryOver += 10;
    }
  }

  if (peak === "I") {
    const next = rev[0];
    if (next === "X") {
      rev.shift();
      carryOver += 9;
    } else if (next === "V") {
      rev.shift();
      carryOver += 4;
    } else {
      carryOver += 1;
    }
  }

  return romanToInt1(rev.join(""), carryOver);
}

const trad: { [index: string]: number } = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

function romanToInt2(s: string): number {
  let newS = s;

  newS = newS.replace("IV", "IIII");
  newS = newS.replace("IX", "VIIII");
  newS = newS.replace("XL", "XXXX");
  newS = newS.replace("XC", "LXXXX");
  newS = newS.replace("CD", "CCCC");
  newS = newS.replace("CM", "DCCCC");

  let result = 0;

  for (const char of newS) {
    result += trad[char];
  }

  return result;
}

const romanToInt3 = (s: string): number => {
  let arr = s.split("");
  let res = 0;
  for (let i = 0; i < arr.length; i++) {
    if (trad[arr[i]] < trad[arr[i + 1]]) {
      res -= trad[arr[i]];
      continue;
    }
    res += trad[arr[i]];
  }
  return res;
};

const trad2 = new Map([
  ["I", 1],
  ["V", 5],
  ["X", 10],
  ["L", 50],
  ["C", 100],
  ["D", 500],
  ["M", 1000],
]);

const romanToInt4 = (s: string): number => {
  let arr = s.split("");
  let res = 0;
  for (let i = 0; i < arr.length; i++) {
    if (trad2.get(arr[i])! < trad2.get(arr[i + 1])!) {
      res -= trad2.get(arr[i])!;
      continue;
    }
    res += trad2.get(arr[i])!;
  }
  return res;
};
