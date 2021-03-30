n = int(input())
num = list(map(int,input().split()))
m = int(input())
search = list(map(int,input().split()))
#재귀함수 이용
def binary_search(array,target,start,end):
  if start>end:
    return None
  mid = (start+end)//2
  if array[mid] == target:
    return mid
  elif array[mid]>target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)
#반복문 사용
def binary_search1(array,target,start,end):
  while start<=end:
    mid = (start+end)//2
    if array[mid] == target:
      return mid
    elif array[mid]>target:
      end = mid-1
    else:
      start = mid + 1
  return None  

for i in range(len(search)):
  result = binary_search(num,search[i],0,n-1)
  if result == None:
    print("N0")
  else:
    print("Yes")
for i in search:
  result1 = binary_search(num,i,0,n-1)
  if result1 != None:
    print('yes',end='')
  else:
    print('No',end='')


#계수정렬이용한 방법
k = int(input())
array = [0]*100001
#가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
  array[int(i)] = 1
#M(손님이 확인 요청한 부품개수)입력받기
m = int(input())
#손님이 확인 요청한 전체 부품번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))
for i in x:
  if array[i] == 1:
    print('Yes')
  else:
    print('no')

#집합자료형 set() 이용

z = int(input())

#가게에 있는 전체 부품 번호를 입력받아서 집합(set)자료형에 기록
array = set(map(int,input().split()))
m = int(input())
x = list(map(int,input().split()))
for i in x:
  if i in array:
    print('Yes',end='')
  else:
    print('No',end='')

























