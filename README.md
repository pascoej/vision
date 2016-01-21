#Vision
##Prachi Bodas, John Pascoe
##Carnegie Mellon University
##16-264 - Humanoids

Do this to setup: 
http://www.pyimagesearch.com/2015/06/29/install-opencv-3-0-and-python-3-4-on-osx/
but replace build command with this
```Shell
cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D PYTHON3_PACKAGES_PATH=~/.virtualenvs/cv3/lib/python3.5/site-packages \
  -D PYTHON3_LIBRARY=/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/libpython3.5m.dylib \
  -D PYTHON3_INCLUDE_DIR=/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/include/python3.5m \
  -D INSTALL_C_EXAMPLES=OFF \
  -D INSTALL_PYTHON_EXAMPLES=ON \
  -D BUILD_EXAMPLES=ON \
  -D BUILD_opencv_python3=ON \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules ..```

Also check out opencv version 3.1.0

