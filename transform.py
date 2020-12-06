import numpy as np
import open3d as o3d


def EulerAngle_from_RotationMatrix(M):
     
    if M[2][0] == -1:
        alpha = 0
        beta = np.pi / 2
        gamma = np.arctan2(M[0][1],M[1][1])
        
    elif M[2][0] == 1:
        alpha = 0
        beta = - np.pi / 2
        gamma = - np.arctan2(M[0][1],M[1][1])           
        
    else:
        beta = np.arctan2(-M[2][0],((M[0][0]**2 + M[1][0]**2)**(0.5))) #in radians
        alpha = np.arctan2(M[1][0]/np.cos(beta),M[0][0]/np.cos(beta))
        gamma = np.arctan2(M[2][1]/np.cos(beta),M[2][2]/np.cos(beta))
       
    return [alpha,beta,gamma]

def RotationMatrix_from_EulerAngles(alpha,beta,gama):
     
    [sa,sb,sc] = np.sin([alpha,beta,gama])
    [ca,cb,cc] = np.cos([alpha,beta,gama])
    
    M = np.array([
    [ca*cb, ca*sb*sc-sa*cc, ca*sb*cc+sa*sc],
    [sa*cb, sa*sb*sc+ca*cc, sa*sb*cc-ca*sc],
    [-sb  , cb*sc         , cb*cc         ]])
    
    return M

def PCD_Transform(pcd,M):
	"""
	

	Parameters
	----------
	pcd : o3d.pointcloud()
		point cloud
	M :  matrix
		transformation matrix 
		in zyx euler angles

	Returns
	-------
	None.

	"""
	pcd_array = np.asarray(pcd.points)
	pcd_Atransformed = np.dot(np.array(M),np.array(pcd_array).T).T
	pcd_NEW = o3d.geometry.PointCloud()
	pcd_NEW.points = o3d.utility.Vector3dVector(pcd_Atransformed)
	return pcd_NEW