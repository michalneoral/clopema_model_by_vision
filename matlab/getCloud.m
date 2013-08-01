function [ pcloud, distance ] = getCloud( queue )

res_X=480;
res_Y=640;

first=zeros(res_X, res_Y);
second=first;

index=1;
for i=1:res_X
    for j=1:res_Y
        first(i,j)=queue(index);
        second(i,j)=queue(index+1);
        index=index+2;
    end
end

queue=first+second.*256;

[pcloud, distance] = depthToCloud(queue);

%dopsat odstranění velké vzdálenosti

end

