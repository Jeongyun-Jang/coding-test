# sol 1773
#The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

# Example 1:

# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        cnt = 0
        for i in range(len(items)):
          if ruleKey == 'type' and ruleValue == items[i][0]:
              cnt += 1
          elif ruleKey == 'color' and ruleValue == items[i][1]:
              cnt += 1
          elif ruleKey == 'name' and ruleValue == items[i][2]:
              cnt += 1

        return cnt
        