func hasDuplicate(nums []int) bool {
    seen := make(map[int]struct{})
    for _, num := range nums {
        _, exists := seen[num]
        if exists {
            return true
        }
        seen[num] = struct{}{}
    }
    return false
}
