import numpy as np


with open('1.txt') as fp:
    tree_grid = np.array(list(map(lambda line: list(map(
        int, list(line))), (fp.read().splitlines()))))


maxi_visible_height_map = np.full(tree_grid.shape, np.nan)
for row_idx in range(1, tree_grid.shape[0]-1):
    maxi_visible_height_map[row_idx, :] = np.fmin(np.max(tree_grid[:row_idx, :], axis=0),
                                                  maxi_visible_height_map[row_idx, :])
    maxi_visible_height_map[row_idx, :] = np.fmin(np.max(tree_grid[row_idx+1:, :], axis=0),
                                                  maxi_visible_height_map[row_idx, :])

for col_idx in range(1, tree_grid.shape[1]-1):
    maxi_visible_height_map[:, col_idx] = np.fmin(np.max(tree_grid[:, :col_idx], axis=1),
                                                  maxi_visible_height_map[:, col_idx])
    maxi_visible_height_map[:, col_idx] = np.fmin(np.max(tree_grid[:, col_idx+1:], axis=1),
                                                  maxi_visible_height_map[:, col_idx])

fst_part_result = tree_grid.shape[0] * tree_grid.shape[1] - \
    np.sum(tree_grid[1:-1, 1:-1] <= maxi_visible_height_map[1:-1, 1:-1])
print(f'{fst_part_result=}')


scenic_score_matrix = np.full(tree_grid.shape, 1)
for row_idx in range(1, tree_grid.shape[0]-1):
    blocked_dist_matrix = tree_grid[row_idx +
                                    1:, :] >= tree_grid[row_idx, :]
    blocked_view_dist = blocked_dist_matrix.argmax(axis=0) + 1
    unblocked_view_dist = (~blocked_dist_matrix.any(
        axis=0)) * (tree_grid.shape[0] - row_idx - 1)
    view_dist = np.maximum(blocked_view_dist, unblocked_view_dist)
    scenic_score_matrix[row_idx,
                        :] = scenic_score_matrix[row_idx, :] * view_dist

    blocked_dist_matrix = np.flip(
        tree_grid[:row_idx, :] >= tree_grid[row_idx, :], axis=0)
    blocked_view_dist = blocked_dist_matrix.argmax(axis=0) + 1
    unblocked_view_dist = (~blocked_dist_matrix.any(axis=0)) * (row_idx)
    view_dist = np.maximum(blocked_view_dist, unblocked_view_dist)
    scenic_score_matrix[row_idx,
                        :] = scenic_score_matrix[row_idx, :] * view_dist

for col_idx in range(1, tree_grid.shape[1]-1):
    blocked_dist_matrix = tree_grid[:,
                                    col_idx + 1:] >= tree_grid[:, [col_idx]]
    blocked_view_dist = blocked_dist_matrix.argmax(axis=1) + 1
    unblocked_view_dist = (~blocked_dist_matrix.any(
        axis=1)) * (tree_grid.shape[1] - col_idx - 1)
    view_dist = np.maximum(blocked_view_dist, unblocked_view_dist)
    scenic_score_matrix[:,
                        col_idx] = scenic_score_matrix[:, col_idx] * view_dist

    blocked_dist_matrix = np.flip(
        tree_grid[:, :col_idx] >= tree_grid[:, [col_idx]], axis=1)
    blocked_view_dist = blocked_dist_matrix.argmax(axis=1) + 1
    unblocked_view_dist = (~blocked_dist_matrix.any(axis=1)) * (col_idx)
    view_dist = np.maximum(blocked_view_dist, unblocked_view_dist)
    scenic_score_matrix[:,
                        col_idx] = scenic_score_matrix[:, col_idx] * view_dist

print(f'{np.max(scenic_score_matrix)=}')
