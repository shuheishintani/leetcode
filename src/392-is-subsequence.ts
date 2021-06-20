function isSubsequence(s: string, t: string): boolean {
  if (s.length === 0) {
    return true;
  }
  for (const char of t) {
    if (char === s[0]) {
      s = s.slice(1);
      if (s.length === 0) {
        return true;
      }
    }
  }
  return false;
}

function isSubsequence2(s: string, t: string): boolean {
  if (s.length === 0) {
    return true;
  }
  let index = 0;
  for (let i = 0; i < t.length; i++) {
    if (t.charAt(i) === s.charAt(index)) {
      index++;
    }
    if (index >= s.length) {
      return true;
    }
  }
  return false;
}
