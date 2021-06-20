export class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function isValidBST(root: TreeNode | null): boolean {
  return validate(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER);
}

const validate = (root: TreeNode | null, min: number, max: number): boolean => {
  if (!root) {
    return true;
  } else if (root.val >= max || root.val <= min) {
    return false;
  } else {
    return (
      validate(root.left, min, root.val) && validate(root.right, root.val, max)
    );
  }
};

const node = new TreeNode(2);
node.left = new TreeNode(1);
node.right = new TreeNode(3);

console.log(isValidBST(node));
