class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let max = 0;
        let l = 0;
        let r = heights.length -1;

        while (l < r) {
            const currAmount = (r-l) * Math.min(heights[l], heights[r]);
            max = Math.max(max, currAmount);

            if (heights[l] >= heights[r]) {
                r--;
            }
            else if (heights[l] < heights[r]) {
                l++;
            }
        }

        return max;
    }
}
