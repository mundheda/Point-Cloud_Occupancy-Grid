# Point-Cloud_Occupancy-Grid

Point clouds are a collection of points that represent a 3D shape or feature.Each point has its own set of X, Y and Z coordinates and in some cases additional attributes.

Point clouds are most often created by methods used in photogrammetry or remote sensing.Photogrammetry uses photographs to survey and measure an area or object.
A combination of photographs taken at many angles can be used to create point clouds.

## LIDAR Point Clouds

Basically, LiDAR is a remote sensing process which collects measurements used to create 3D models and maps of objects and environments. Using ultraviolet, visible, or near-infrared light, LiDAR gauges spatial relationships and shapes by measuring the time it takes for signals to bounce off objects and return to the scanner.

Although now most sources treat the word "LiDAR" as an acronym, the term originated as a combination of "light" and "radar". When LiDAR was first proposed in the 1960s, lasers and detection mechanisms were bulky and slow to operate — all that is changing rapidly.

![README/kitti.png](README/kitti.png)

LiDAR systems send out pulses of light just outside the visible spectrum and register how long it takes each pulse to return. The direction and distance of whatever the pulse hits are recorded as a point of data. Different LiDAR units have different methods, but generally they sweep in a circle like a RADAR dish, while simultaneously moving the laser up and down.

![README/Lidar_1.png](README/Lidar_1.png)

## Occupancy Grid Construction

### What are Occupancy Grid Maps?
Occupancy grid maps are discrete fine grain grid maps. These maps can be either 2-D or 3-D. Each cell in the occupancy grid map contains information on the physical objects present in the corresponding space. Since these maps shed light on what parts of the environment are occupied, and what is not, they are really useful for path planning and navigation.

Examples of a simple 2-D grid map and a complicated 3-D map. Notice how the 3-D map is discretized and not an example of a point cloud:

[https://lh4.googleusercontent.com/NxQOmkaI0iA1cWQo4ymdeprJyhMEKdyYlUyoNQa2AIxu5OY1YZ-LXoX-KeBoS-T-R7AO0zlBI0Byd_g24exM35H1vZj3mqv9-AUVfyr9J1D9CO1WSyiMXJ1Myu9cDLl3ihQqDQgF](https://lh4.googleusercontent.com/NxQOmkaI0iA1cWQo4ymdeprJyhMEKdyYlUyoNQa2AIxu5OY1YZ-LXoX-KeBoS-T-R7AO0zlBI0Byd_g24exM35H1vZj3mqv9-AUVfyr9J1D9CO1WSyiMXJ1Myu9cDLl3ihQqDQgF)

[https://lh3.googleusercontent.com/j47FR-uFXfsP3LWv5XQRyVLM6yk7EQiaKMGPEJCESA3UasHryl9a8ECjSsGgnGwfGJDUSmpH9IQpH8xn31_Xw_oohQZr15NUSSab3xR9TdGf5xK8Uc3TYIv9lHmbajspFZJOWIbl](https://lh3.googleusercontent.com/j47FR-uFXfsP3LWv5XQRyVLM6yk7EQiaKMGPEJCESA3UasHryl9a8ECjSsGgnGwfGJDUSmpH9IQpH8xn31_Xw_oohQZr15NUSSab3xR9TdGf5xK8Uc3TYIv9lHmbajspFZJOWIbl)
