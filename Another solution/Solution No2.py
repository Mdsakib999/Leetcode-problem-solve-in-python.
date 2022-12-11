class Solution:
   def solve(self, words):
      words.sort()
      prefix = []
      flag = 0
      for i in range(len(words[0])):
         prefix.append(words[0][i])
         for j in words:
            if j[i] != prefix[-1]:
               prefix.pop()
               flag = 1
               break
         if flag == 1:
            break
      return ''.join(prefix)
value = Solution()
words = list(map(str,input('Write the elements sequence: ').split()))
print(value.solve(words))