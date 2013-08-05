function [ rect_image ] = rectificationImage( rect, image )

    rect_image=zeros(size(image));
    
    

    
    
    % DODELAT
    
     for i=1:size(image,1)
         for j=1:size(image,2)
             for k=1:size(image,3)
                 sec_image(i,j,k,:) = rect.P * [i j image(i,j,k) 1]';
%                  x = u / w;
%                  y = v / w;
             end
         end
     end

     rect_image=sec_image;
     
end

