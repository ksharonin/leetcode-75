import java.util.*;

class Solution {
    public int[] runningSum(int[] nums) {
        // Create same size array - indexes start 0!
        int limit = nums.length;
        int[] result = new int[limit];
       
        // Net sum store
        int sum = 0;
    
        // Populate w loop, DO NOT over index
        for (int i= 0; i < limit; i++) {
            sum = sum + nums[i]; // update sum
            result[i] = sum; // update result array
        }
    
        return result;
    }
}

// runtime: 0 ms, memory: 43.5 MB
