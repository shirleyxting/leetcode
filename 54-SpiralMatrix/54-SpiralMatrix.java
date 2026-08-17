// Last updated: 8/16/2026, 9:53:09 PM
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        int m = matrix.length, n = matrix[0].length;

        int iMin = 0, iMax = m-1, jMin = 0, jMax = n-1;

        while(iMin <= iMax && jMin <= jMax) {
            // move right
            for(int j = jMin; iMin <= iMax && j <= jMax; j ++) res.add(matrix[iMin][j]);
            iMin ++;
            
            // move down
            for(int i = iMin; jMin <= jMax && i <= iMax; i ++) res.add(matrix[i][jMax]);
            jMax --;

            // move left
            // int j = jMax; iMin <= iMax && jMin <= jMax && j >= jMin 
            // -> simplify to: iMin <= iMax && j >= jMin 
            for(int j = jMax; iMin <= iMax && j >= jMin; j --) res.add(matrix[iMax][j]);
            iMax --;
            
            // move up
            // int i = iMax; iMin <= iMax && jMin <= jMax && i >= iMin
            // -> simplify: jMin <= jMax && i >= iMin
            for(int i = iMax; jMin <= jMax && i >= iMin; i --) res.add(matrix[i][jMin]);
            jMin ++;
        
        }

        return res;
    }
}