<순차탐색>

-리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 한씩 차례대로 확인하는 방법
-보통 정렬 되지 않은 리스트에서 데이터를 찾아야 할때 사용
#순차탐색 소스코드
def sequential_search(n,target,array):
  #각 원소를 하나씩 확인하며
  for i in range(n):
    #현재의 원소가 찾고자 하는 원소와 동일한 경우
    if array[i]==target:
      return i+1#현재의 위치 반환
      



<이진탐색>
-배열 내부의 데이터가 정렬되어있어야만 사용할수 있는 알고리즘
-범위 시작점, 끝점, 중간점의 위치를 나타내는 변수 3개 사용
찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는다.
#재귀함수로 구현한 이진탐색 소스코드
def bianry_search(array,target,start,end):
  if start>end:
    return None
   mid = (start+end)//2
   #찾은 경우 인덱스 반환
   if array[mid] == target:
    return mid
   #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
   elif array[mid]>target:
    return binary_search(array,target,start,mid-1)
   else:
    return binary_search(array,target,mid+1,end)
 

#반복문으로 구현한 이진탐색 소스코드
def binary_search(array,target,start,end):
  while start<=end:
    mid = (start+end)//2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
      end = mid-q
    else:
      start = mid+1
  return None
  
  
  
 <이진 탐색트리>
 -부모노드보다 왼쪽 자식노드가 작다
 -부모노드보다 으른쪽 자식노드가 크가























