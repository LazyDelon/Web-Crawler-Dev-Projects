import os
import get_data as gd

path = 'C:\\DFS\\'

# 查詢是否已有資料夾，無資料夾則新增一個
folder = path 
if not os.path.isdir(folder):
    os.makedirs(folder)

gd.get_data(path)
gd.combine_all_data(path)
gd.get_merge(path)
gd.csv_db(path)