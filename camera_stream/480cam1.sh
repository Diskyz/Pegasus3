gst-launch-1.0 -v v4l2src device=/dev/cameraMAST ! image/jpeg,width=640,height=480,framerate=15/1 \
  ! rtpjpegpay ! udpsink host=192.168.1.100 port=1234
