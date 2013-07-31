function [ picture ] = doImageXtion( queue )

%make picture from queue

first=zeros(480, 640);
second=first;
third=first;
fourth=first;

% lenght_of_front = size(queue) / res_X / res_Y;

index=1;
for i=1:480
    for j=1:640
        first(i,j)=queue(index);
        second(i,j)=queue(index+1);
        third(i,j)=queue(index+2);
        fourth(i,j)=queue(index+3);
        index=index+4;
    end
end
 
picture=(first+second.*256+third.*(256^2));

for i=1:480
    for j=1:640
        if fourth(i,j) == 127
            picture(i,j)=NaN;
        end
    end
end

figure(1)

colormap(gray(256))
image(fourth)

figure(2)

%mesh(picture)
meshc(picture)

end