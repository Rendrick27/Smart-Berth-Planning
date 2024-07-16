# Smart-Berth-Planning
This repository is a improvement version of the GitHub repository from "Smart-Berth-Planning" by afonsomm which is focused on optimizing berth allocation in ports. The repository contains several Jupyter notebooks that process and analyze AIS (Automatic Identification System) data for ports in France and Miami. The project includes data processing, voyage analysis, dataset creation, and model optimization for berth allocation. 

## Requirements
  - geopandas (0.13.0)
  - geodatasets (2023.3.0)
  - folium (0.14.0)
  - jupyter (1.0.0)
  - matplotlib (3.7.5)
  - scienceplots (2.1.0)
  - movingpandas (0.16.0)
  - numpy (1.25.0)
  - pandas (2.0.3)
  - pytorch (1.0.2)
  - scipy (1.11.1)
  - seaborn (0.12.2)
  - scikit-learn (1.3.0)
  - Latex
  - Python

## Dataset

To run the models, please follow these steps: 
- Download the AIS data from the links below;
- Create a folder named "data";
- Move the downloaded AIS data into the "data" folder with the following struture.
  - ./data/france_data/AIS_data
  - ./data/france_data/Ports_Brittany
  - ./data/miami_data 

### AIS Data
- <p><a href= "https://zenodo.org/records/2597641"> France</a> </p>
- <p><a href= "https://tore.tuhh.de/entities/product/79ae9d40-5a02-4e92-b1bf-32053e9a50b5"> Miami </a> </p>

## Docker

```bash
docker build -t {image_name} .

docker run -p 8888:8888 {image_name}
```

Then copy the link from the terminal to your browser to acess the jupyter notebook or you can open it by using dev container in VS Code

## Credits
### Original Repository
* <p> <a href= "https://github.com/afonsomm/Smart-Berth-Planning"> afonsomm
 </a> </p>

## License
GPLv3