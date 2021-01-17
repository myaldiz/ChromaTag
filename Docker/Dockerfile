FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates git wget vim cmake build-essential cmake curl ca-certificates \
    	libjpeg-dev libpng-dev x11-apps v4l-utils unzip ffmpeg \
		libgoogle-glog-dev libatlas-base-dev libeigen3-dev libsuitesparse-dev \
        libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev python-dev \
        python-numpy python3-dev python3-numpy python3-pip python3-setuptools \
        libtbb2 libtbb-dev  libtiff-dev libdc1394-22-dev \
		libfreeimage-dev libgflags-dev \
		qtbase5-dev libqt5opengl5-dev libcgal-dev \
		libglfw3-dev libgif-dev libpango1.0-dev \
        liblcm-dev liblcm-bin libcanberra-gtk-module libcanberra-gtk3-module\
	&& apt-get install -y --no-install-recommends lsb-release less udev \
  	&& rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN wget https://github.com/opencv/opencv/archive/3.4.3.zip \
    && unzip 3.4.3.zip && rm 3.4.3.zip \
    && cd opencv-3.4.3 && mkdir build && cd build \
    && cmake -D CMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local \
      -DPYTHON_DEFAULT_EXECUTABLE=$(which python3) -DBUILD_opencv_python3=ON  .. \
    && make -j8 \
    && make install

ADD . /opt/chromatag
RUN cd /opt/chromatag && mkdir build && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release .. \
    && make -j8 

RUN pip3 install jupyter matplotlib ipympl