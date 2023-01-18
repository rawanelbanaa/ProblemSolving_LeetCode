## This is my first solution I write but when submet given a **Time Limit Exceeded**

```
Res= []
n = len(nums)
for i in range(1,n+1):
    if i in nums:
        continue
    else:
        Res.append(i)

return Res

```

and This another sucssful solution 

```
return set(range(1, len(nums)+1)).difference(set(nums))

```
