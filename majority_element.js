/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  // Create obj to hold counts
  // Loop through the list
  // Return highest count
  let count = {};
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in count) {
      count[nums[i]]++;
    } else {
      count[nums[i]] = 0;
    }
  }
  return Object.keys(count).reduce((a, b) => (count[a] > count[b] ? a : b));
};
