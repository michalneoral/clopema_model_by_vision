function [image] = queueToImage (queue,res_X,res_Y)
    sizeOfColor = size(queue,1)/res_X/res_Y;
    image=zeros(res_Y,res_X,sizeOfColor);
    count=1;
    for i=1:res_Y
        for j=1:res_X
            for k=1:sizeOfColor
                image(i,j,k)=queue(count);
                count=count+1;
            end
        end
    end    
end