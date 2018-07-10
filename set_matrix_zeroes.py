#-*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/set-matrix-zeroes/description/

给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_dict = {}
        for row_n, row in enumerate(matrix):
            for col_n, col in enumerate(row):
                if col == 0:
                    row_dict.setdefault(row_n, [])
                    row_dict[row_n].append(col_n)
                    
        col_flag = {}
        for row in row_dict:
            matrix[row][:] = [0]*len(matrix[0])
            for col in row_dict[row]:
                if col in col_flag:
                    continue
                for i in matrix:
                    i[col] = 0
                

    
s = Solution()
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s.setZeroes(matrix)
for i in matrix:
    print i 
        
    
        
        
        
        
        
        