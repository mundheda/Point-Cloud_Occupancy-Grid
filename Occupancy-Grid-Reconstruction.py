from Part1 import *
import matplotlib.pyplot as plt

def toWorldPCD(Lidar_to_World_i,pcd_i):
    pcd_world = o3d.geometry.PointCloud()
    pcd_transformed = np.dot(np.array(Lidar_to_World_i),np.array(pcd_i).T).T
    pcd_transformed = np.delete(pcd_transformed,3,1)
    #Doing the tranformation of Lidar frame points to world frame points
    #pcd_del = np.delete(pcd_transform,3,1) #Deleting the column for ones
    #print(np.shape(pcd_transformed))
    pcd_world.points = o3d.utility.Vector3dVector(pcd_transformed) #Con verting Numpy matrix to PCD
    
    return pcd_world

def k_name(i):
    if(i < 10):
        k = '0' + str(i) 
    else:
        k = str(i)
    return k

def pcdtoccgrid(pcd,th,img_name,i):
    #Reading points from PCD
        points = np.asarray(pcd.points) 
        points = np.around(points) 
        points = points.astype(int)
    #Finding min and max points 
        min_x = np.min(points[:,0]) 
        min_y = np.min(points[:,1]) 
        max_x = np.max(points[:,0]) 
        max_y = np.max(points[:,1])
    #Finding Range 
        size_x = max_x-min_x+1 
        size_y = max_y-min_y+1 
    #Removing same points from the pcd points array
        points_u = np.unique(points,axis=0) 
        points_u[:,0] = points_u[:,0] - min_x 
        points_u[:,1] = points_u[:,1] - min_y
    #Grid of size of range(x)* range(y) 
        occ_grid = np.zeros((size_y,size_x)) 
        for j in range(len(points_u)):
            occ_grid[points_u[j][1]][points_u[j][0]]+=1 
        occ_grid = (occ_grid>th) 
    #Saving occupancy grid map
        plt.imsave(img_name,occ_grid, cmap = plt.get_cmap('gray')) 

pcd_one = o3d.geometry.PointCloud()
pcd_combined = o3d.geometry.PointCloud()
for i in range(77):
    pcd_one = toWorldPCD(PoseMat[i],pcd[i])
    alph = math.radians(-90)
    beta = math.radians(0)
    gama = math.radians(-90)

    M = transform.RotationMatrix_from_EulerAngles(alph,beta,gama)
    pcd_one =  transform.PCD_Transform(pcd_one,M)

    img_name = './Results/Individual_binary/binary_'+ k_name(i) +'.png'
    threshold  = 1 #Threshold for number of values of z for given (x,y)
    pcdtoccgrid(pcd_one,threshold,img_name,i)
    pcd_combined += pcd_one

    if(i == 5 or i == 10 or i == 15 or i == 76):
    	img_name = './Results/Combined/combined_0_to_'+ k_name(i) +'.png'
    	pcdtoccgrid(pcd_combined,threshold,img_name,i)
