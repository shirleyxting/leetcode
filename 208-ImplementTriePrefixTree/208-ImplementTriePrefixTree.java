// Last updated: 8/16/2026, 9:51:19 PM
class Trie {

    class TrieNode {
        public TrieNode[] children;
        public boolean is_word;

        public TrieNode() {
            children = new TrieNode[26];
            is_word = false;
        }
    }

    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode p = root;
        for (int i = 0; i < word.length(); i ++) {
            int idx = word.charAt(i) - 'a';
            // if not exist in trie, create a new TrieNode of word.charAt(i)
            if (p.children[idx] == null) p.children[idx] = new TrieNode();
            // move p to next node
            p = p.children[idx];
        }
        // mark the last node as 'is_word'
        p.is_word = true;
    }
    
    public boolean search(String word) {
        TrieNode node = helper(word);
        return node != null && node.is_word;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = helper(prefix);
        return node != null;
    }

    private TrieNode helper(String str) {
        TrieNode p = root;
        for (int i = 0; i < str.length(); i ++) {
            int idx = str.charAt(i) - 'a';
            // if this char cannot be found, return null
            if (p.children[idx] == null) return null;
            // move to next node
            p = p.children[idx];
        }
        // return last node;
        return p;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */