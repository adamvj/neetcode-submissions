class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1
        while start <= end:
            mid_list = (start+end)//2
            mid_list_vals = matrix[mid_list]
            start2=0
            end2 = len(mid_list_vals)-1
            while start2<=end2:
                #print("Made to second while")
                mid = (start2+end2)//2
                mid_val = mid_list_vals[mid]
                if target == mid_val:
                    return True
                elif target > mid_val:
                    start2 = mid+1
                else:
                    end2 = mid-1
            #print("Current mid: ", mid) 
            if target > mid_val:
                #print("Made to target>mid")
                start = mid_list+1
            else:
                end = mid_list-1
                #print("Dropped to previous list")
        return False