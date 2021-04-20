class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                path_count = 0
                if i > 0:
                    path_count += paths[i-1][j]
                if j > 0:
                    path_count += paths[i][j-1]

                # This means it's an edge (case). Literally.
                if path_count == 0:
                    path_count = 1

                paths[i][j] = path_count

        return paths[-1][-1]


tests = [
    (
        (3, 7,),
        28,
    ),
    (
        (3, 3,),
        6,
    ),
    (
        (7, 3,),
        28,
    ),
    (
        (3, 2,),
        3,
    ),

]
