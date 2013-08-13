im1 = queueToImage(msgs{8,1}{1,25}.data)./255;
im2 = queueToImage(msgs{8,1}{1,26}.data)./255;
im3 = queueToImage(msgs{8,1}{1,27}.data)./255;

im1c = rgb2gray(im1);
im2c = rgb2gray(im2);

im1f = motionDetection(im1, rgb_back);
im2f = motionDetection(im2, rgb_back);
im3f = motionDetection(im3, rgb_back);

im1fc = rgb2gray(im1f);
im2fc = rgb2gray(im2f);