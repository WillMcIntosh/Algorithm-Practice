# On a staircase, the i-th step has some non-negative cost cost[i]
# assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need 
# to find minimum cost to reach the top of the floor, and you can either 
# start from the step with index 0, or the step with index 1.

###################################
# My attempt that didn't work
###################################

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # decide to start on 0 or 1
        
        # for different lengths...
        if len(cost) > 4:
            options_zero = [cost[0]+cost[1], cost[0]+cost[2]]
            zero         = min(options_zero)
            options_one  = [cost[1]+cost[2],cost[1]+cost[3]]
            one          = min(options_one)
        elif len(cost) == 4:
            options_zero = [cost[0]+cost[1]+cost[2], cost[0]+cost[2], cost[0] + cost[1]+cost[2]]
            zero         = min(options_zero)
            options_one  = [cost[1]+cost[2], cost[1]+cost[3]]
            one          = min(options_one)
            if one > zero:
                total = min(options_zero)
                return total
            else:
                total = min(options_one)
                return total
        elif len(cost) >= 3:
            options_zero = [cost[0]+cost[1], cost[0]+cost[2]]
            zero         = min(options_zero)
            options_one  = [cost[1]]
            one          = min(options_one)
        elif len(cost) == 2:
            zero         = cost[0]
            one          = cost[1]

        if one > zero:
            position = 0
        else:
            position = 1

        total = cost[position]  

        # now interate over list and find cost
        for i in range(0,len(cost)-1):
            
            if i != position: 
                continue
            else:
                  
                # check if we can move 2 more spots or 1 or 'none'
                if (i+1) >= len(cost)-1:
                    return total
                elif (i+2) >= len(cost): 
                    options_list = [cost[i]+ cost[i+1]]
                else:
                    options_list = [cost[i]+cost[i+2], cost[i]+ cost[i+1]]
                # return 2 if 2 moves is best, 1 if 1 is best
                if len(options_list) == 2 and options_list.index(min(options_list)) == 0:
                    action = 2
                else: 
                    action = 1
                    
                position = position + action
                total = total + cost[position]
                # return total if you'd go over
                if (position + action) >= len(cost)-1: 
                    return total


####################################
# example from discussion that does
####################################

# Minimum cost to reach step i is the min of costs to reach it 
# from [i-1] and [i-2].

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 0 or n == 1:
            return 0
        min_cost = [0]*n
        min_cost[0], min_cost[1] = cost[0], cost[1]
        for i in range(2, n):
            min_cost[i] = min(min_cost[i-1], min_cost[i-2]) + cost[i]

        return min(min_cost[n-1], min_cost[n-2])
