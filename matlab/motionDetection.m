function [ filtredImage ] = motionDetection( image1,image2 )

offset = 0.1;
filtredImage = image1;

    for i=1:size(image1,1)
        for j=1:size(image1,2)
            for k=1:size(image1,3)
                if max(max( image1(i,j,:) - image2(i,j,:))) < offset
                    filtredImage(i,j,:) = NaN;
                end
            end
        end
    end
    
end