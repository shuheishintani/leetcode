function removeDuplicates(s: string): string {
  const stack: string[] = [];

  for (const char of s) {
    if (stack[stack.length - 1] === char) {
      stack.pop();
      continue;
    }
    stack.push(char);
  }

  return stack.join("");
}

removeDuplicates("abbaca");
