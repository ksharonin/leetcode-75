class Solution {
    public int pivotIndex(int[] nums) {
        // calculate the pivot index of this array
        // left and right sums of pivot must == each other
        int sum = 0, leftSum = 0;
        // double loop to contribute to left and calc right sum
        for (int x: nums) sum += x;
          for (int i = 0; i < nums.length; i++) {
              if (leftSum == sum - nums[i] - leftSum) 
                  return i;
              leftSum += nums[i];
          }
        return -1;
    }
}
