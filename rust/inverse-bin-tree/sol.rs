use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(root_val) = &root {
            let mut node = root_val.borrow_mut();
            let left = node.left.take();
            let right = node.right.take();
            node.left = right;
            node.right = left;
            Self::invert_tree(node.left.clone());
            Self::invert_tree(node.right.clone());
        } 
        return root;
    }
}

