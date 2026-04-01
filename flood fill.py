# idea is to fill connected cells (like a paint bucket🎨)
# steps in doing this
# start from a pixel
# change its color
# spread to neighbors (up, down, right, left)

from collections import deque

def floodfill(image, sr, sc, color):
    old = image[sr][sc]
    if old == color:
        return image
    
    queue = deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()
        if image[r][c] == old:
            image[r][c] = color

            for dr, dc in [(1,0),(-1,0),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(image) and 0 < len(image[0]):
                    queue.append((nr, nc))
    return image                