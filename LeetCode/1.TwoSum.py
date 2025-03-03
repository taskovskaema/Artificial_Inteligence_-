
class Solution:
 def twoSum(self, nums:list[int], target:int)->list[int]:

  for i in range(len(nums)):
   x=target-nums[i]
   if x in nums[i+0:]:
    return [i,nums.index(x,i+1)]
  return[]

if __name__ == '__main__':

 lista1=input("vnesi lista: ->")
 # lista=lista1.split(',')
 lista=[int(x) for x in lista1.split(',')]

 target=int(input())

 print(Solution().twoSum(lista,target))
