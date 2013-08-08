function [ filtredImage, maskedImage ] = motionDetection( image1,image2 )

offset = 0.1;
    
maskedImage = abs(image1-image2) >= offset;

maskedImage(:,:,1) = (maskedImage(:,:,1)+maskedImage(:,:,2)+maskedImage(:,:,3)) >= 1-offset;

%% mathematical morphology opening
openingMask = ones (10);
maskedImage(:,:,1) = imopen(maskedImage(:,:,1),openingMask);

%%
maskedImage(:,:,2) = maskedImage(:,:,1);
maskedImage(:,:,3) = maskedImage(:,:,2);

filtredImage = maskedImage .* image1;

end