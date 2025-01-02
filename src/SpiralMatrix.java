import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix{
    public List<Integer> spiralOrder(int[][] matrix) {
        // Calculate the total number of rows and columns
        int rows = matrix.length;
        int cols = matrix[0].length;

        // Set up pointers to traverse the matrix
        int row = 0;
        int col = -1;

        // Set the initial direction to 1 for moving left to right
        int direction = 1;

        // Create an array to store the elements in spiral order
        List<Integer> result = new ArrayList<>();

        // Traverse the matrix in a spiral order
        while (rows > 0 && cols > 0) {
            for (int i = 0; i < cols; i++) {
                col += direction;
                result.add(matrix[row][col]);
            }
            rows--;

            for (int i = 0; i < rows; i++) {
                row += direction;
                result.add(matrix[row][col]);
            }
            cols--;
            direction *= -1;
        }

        return result;
    }
}