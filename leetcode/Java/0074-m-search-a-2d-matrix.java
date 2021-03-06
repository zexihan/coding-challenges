/* 
 * Binary search
 */
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0) {
            return false;
        }

        if (matrix[0] == null || matrix[0].length == 0) {
            return false;
        }

        int n = matrix.length;
        int m = matrix[0].length;
        int start = 0, end = n * m - 1;

        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            int row = mid / m;
            int col = mid % m;
            if (matrix[row][col] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (matrix[start / m][start % m] == target) {
            return true;
        }

        if (matrix[end / m][end % m] == target) {
            return true;
        }

        return false;
    }
}