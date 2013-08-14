if ~ exist('countImage','var')
    countImage=1;
end
if countImage > size(images,2)
    countImage=1;
end
image(images{1,countImage})
countImage=countImage+1;