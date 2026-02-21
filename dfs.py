def DFS(x):
  visited=set()
  stack=[x]
  while stack:
    now=stack.pop()
    if not now in visited:
      visited.add(now)
      for ele in g[now]:
        stack.append(ele)
