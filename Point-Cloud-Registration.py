import utils
import numpy as np 
import open3d as o3d
import transform
import math

#Rotation Matrix
Lidar_to_camera = [[0,0,1,0],
				   [-1,0,0,0],
				   [0,-1,0,0],
				   [0,0,0,1]]

#Empty list to store data from all files
pcd = []

#Importing point cloud data from .bin files
for i in range(0,77):
	if(i < 10):
		k = '0' + str(i) 
	else:
		k = str(i)
	filename = 'dataset/01/0000' + k + '.bin'
	p = utils.readPointCloud(filename)
	p = np.delete(p,3,1)
	p= np.hstack([p, np.ones([p.shape[0], 1], dtype=np.float32)])
	p = np.dot(p,Lidar_to_camera)
	pcd.append(p)


#Reading tranformation 
GroundPose = utils.readData("dataset/01.txt")

GroundPose = GroundPose[0:77]

#Tranformation Matrix
PoseMat = []

#Making the transformation matrix
for i in range(77):
	T = GroundPose[i].reshape(3,4)
	T = np.vstack((T,np.array([0,0,0,1])))
	PoseMat.append(T)


#Create Empty Point Cloud 
pcd_world_combined = o3d.geometry.PointCloud()

# PoseMat[1]= Lidar_to_camera

for i in range(77):
	pcd_world = o3d.geometry.PointCloud()
	pcd_transformed = np.dot(np.array(PoseMat[i]),np.array(pcd[i]).T).T
	pcd_transformed = np.delete(pcd_transformed,3,1)
	pcd_world.points = o3d.utility.Vector3dVector(pcd_transformed) #Converting Numpy matrix to PCD
	pcd_world_combined += pcd_world
    

#o3d.visualization.draw_geometries([pcd_world_combined])

#Rotate pcd to align vertically
alph = math.radians(-90)
beta = math.radians(0)
gama = math.radians(-90)

M = transform.RotationMatrix_from_EulerAngles(alph,beta,gama)
transform.PCD_Transform(pcd_world_combined,M)

#visualize PCD
o3d.visualization.draw_geometries([transform.PCD_Transform(pcd_world_combined,M)])

#Save PCD
o3d.io.write_point_cloud("Results/Part1_Output.pcd", pcd_world_combined)