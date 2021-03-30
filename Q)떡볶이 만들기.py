n,m  = map(int,input().split())
x = list(map(int,input().split()))
end = max(x)
start = 0
while start<=end:
  mid = (start+end)//2
  total = 0
  for i in range(len(x)):
    if x[i]>=mid:
      total+=(x[i] - mid)
  
  if total<m:
    end = mid-1
  else:
    result = mid
    start = mid+1
print(mid)


