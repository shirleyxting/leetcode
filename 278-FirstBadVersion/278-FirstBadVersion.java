// Last updated: 8/16/2026, 9:50:48 PM
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        // brute force O(n), better one should be binary search
        // and its ooxxx, so binary search
        int left = 1, right = n;

        while(left + 1 < right) {
            int mid = left + (right - left) / 2;
            if ( isBadVersion(mid) ) {
                right = mid;
            } else {
                left = mid;
            }
        }
        if(isBadVersion(left)) return left;
        if(isBadVersion(right)) return right;

        return -1;
    }
}