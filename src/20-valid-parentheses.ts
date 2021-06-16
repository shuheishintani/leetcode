function isValid1(s: string): boolean {
  const a = s.split("");
  const stack: string[] = [];
  let valid = true;

  for (const char of a) {
    if (isOpen(char)) {
      stack.push(char);
      continue;
    }
    const peak = stack.pop();
    if (!peak) {
      valid = false;
      break;
    }
    if (isPair(peak, char)) {
      continue;
    } else {
      valid = false;
      break;
    }
  }

  if (stack.length !== 0) {
    valid = false;
  }
  return valid;
}

const isOpen = (char: string): boolean => {
  if (char === "(" || char === "{" || char === "[") {
    return true;
  }
  return false;
};

const isPair = (open: string, close: string): boolean => {
  if (open === "(" && close === ")") {
    return true;
  }
  if (open === "{" && close === "}") {
    return true;
  }
  if (open === "[" && close === "]") {
    return true;
  }
  return false;
};

function isValid2(s: string): boolean {
  const hash: { [key: string]: string } = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  const stack: string[] = [];

  for (const char of s) {
    if (char in hash) stack.push(char);
    else {
      const top = stack.pop();
      if (top === undefined || hash[top] !== char) {
        return false;
      }
    }
  }

  return !stack.length;
}
