function [ filtredImage ] = motionDetection( image1,image2 )

offset = 0.1;

%     for i=1:size(image1,1)
%         for j=1:size(image1,2)
%             for k=1:size(image1,3)
%                 if max(max( image1(i,j,:) - image2(i,j,:))) < offset
%                     filtredImage(i,j,:) = NaN;
%                 end
%             end
%         end
%     end
    
maskedImage = abs(image1-image2) >= offset;

maskedImage(:,:,1) = (maskedImage(:,:,1)+maskedImage(:,:,2)+maskedImage(:,:,3)) >= 1-offset;
maskedImage(:,:,2) = maskedImage(:,:,1);
maskedImage(:,:,3) = maskedImage(:,:,2);
% filtredImage=zeros(size(image));
%     for i=1:3
%         filtredImage(:,:,i)=image1(:,:,i).*maskedImage(:,:,1);
%     end

filtredImage = maskedImage .* image1;
end