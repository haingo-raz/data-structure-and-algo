#https://leetcode.com/problems/3sum/description/
# Inspired by https://leetcode.com/problems/3sum/solutions/725950/python-5-easy-steps-beats-97-4-annotated/
# Two-pointer solution https://leetcode.com/problems/3sum/solutions/5055810/video-two-pointer-solution/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        # 1. Separate into negatives, positives, and zeros
        neg, pos, zero = [], [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zero.append(num)

        # 2. Convert to sets for fast lookup
        neg_set, pos_set = set(neg), set(pos)

        # 3. (neg, 0, pos) triplets
        if zero:
            for num in pos_set:
                if -num in neg_set:
                    res.add((-num, 0, num))

        # 4. (0, 0, 0) triplet
        if len(zero) >= 3:
            res.add((0, 0, 0))

        # 5. (neg1, neg2, pos)
        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                target = -(neg[i] + neg[j])
                if target in pos_set:
                    res.add(tuple(sorted([neg[i], neg[j], target])))

        # 6. (pos1, pos2, neg)
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                target = -(pos[i] + pos[j])
                if target in neg_set:
                    res.add(tuple(sorted([pos[i], pos[j], target])))

        return [list(triplet) for triplet in res]