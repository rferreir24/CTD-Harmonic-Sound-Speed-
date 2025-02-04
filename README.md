# CTD-Harmonic-Sound-Speed

CTD (Conductivity, Temperature, and Depth) data is used to generate sound velocity profiles of the water column, ensuring accurate bathymetric measurements for multibeam sonar and other sonar systems.

**Why is this required?** 

 The Speed of Sound in water is required to derive the range (depth) the sound travels. 

 The calculations performed in **harmonic.py** assumes the sound propagates straight down to the water (Normal vertical incidence). i.e. The effects of refraction are neglected.

Due to variability in sounds speeds at different depths, the harmonic mean sound speed is considered. However, we cannot possibly calculate every millimetre of water, instead we approximate the profile by dividing the layers of water with a constant velocity. 

Hence, we divide the profile into layers and calculate the depth, and the time it takes for the sound to propagate in each layer.

The Harmonic Mean Sound Speed is calculated as follows: 

$$ V = \left( \sum_{i=0}^{i=n} \Delta d_i  \right) \div \left( \sum_{i=0}^{i=n} t_i \right)$$
 
The data used was collected by the University of New Brunswick's Ocean Mapping Group at the Port of Saint John, New Brunswick. 

The following graphs illustrate the differences between the true sound speed profile and the harmonic mean sound speed profile
<img width="890" alt="image" src="https://github.com/user-attachments/assets/72b8a903-d3ce-4916-bbcb-6346196a71fe" />


 
