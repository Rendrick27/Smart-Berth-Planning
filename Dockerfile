FROM jupyter/pyspark-notebook:x86_64-ubuntu-22.04

# Install dependencies
RUN pip install geopandas==0.13.0
RUN pip install geodatasets==2023.3.0
RUN pip install folium==0.14.0
RUN pip install matplotlib==3.7.5
RUN pip install SciencePlots==2.1.0
RUN pip install movingpandas==0.16.0
RUN pip install numpy==1.25.0
RUN pip install pandas==2.0.3
RUN pip install scipy==1.11.1
RUN pip install seaborn==0.12.2
RUN pip install scikit-learn==1.3.0

WORKDIR /nexus
COPY . /nexus