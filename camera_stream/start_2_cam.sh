gst-launch-1.0 v4l2src device=/dev/video0 ! "image/jpeg,width=1280, height=720,framerate=15/1" ! rtpjpegpay ! udpsink host=192.168.1.11 port=9001 stream. v4l2src deice=/dev/video1 ! "image/jpeg,width=1280, height=720,framerate=15/1" ! rtpjpegpay ! udpsink host=192.168.1.11 port=9002 stream.
