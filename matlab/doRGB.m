function [ picture ] = doRGB( queue )
res_X=480;
res_Y=640;
%make picture from queue

red=zeros(res_X, res_Y);
green=red;
blue=red;

rgb=zeros(res_X, res_Y, 3);

% lenght_of_front = size(queue) / res_X / res_Y;

index=1;
for i=1:res_X
    for j=1:res_Y
        red(i,j)=queue(index);
        green(i,j)=queue(index+1);
        blue(i,j)=queue(index+2);
        rgb(i,j,1)=queue(index);
        rgb(i,j,2)=queue(index+1);
        rgb(i,j,3)=queue(index+2);
        index=index+3;
    end
end
    

x = reshape(rgb, res_X, res_Y, 3); % reshape pulls columnwise, assume 6x2 image
x = x/255; %scale the data to be between 0 and 1
image(x);
picture=x;
end

