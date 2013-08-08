function [ something ] = showSubPlotWithPoints( msgs, queue, nfile, rgb_back )
something = 0;

topic3d=1;
topicrgb=2;

y_s = 2;
x_s = 2;

res_Y=480;
res_X=640;

%% Plotting 3D

[ pcloud, distance ] = getCloud( msgs{queue{nfile,1}(topic3d,3),1}{1,queue{nfile,1}(topic3d,1)}.data , true);

subplot(y_s,x_s,1);
surf(distance,'EdgeColor','none');
view(0,-90);
rotate3d off;
colormap(jet);

%% Plotting Image Color

subplot(y_s,x_s,2);
preImage = queueToImage(msgs{queue{nfile,1}(topicrgb,3),1}{1,queue{nfile,1}(topicrgb,1)}.data,res_X,res_Y);
imageRGB = normalizeRGB (preImage);
image(imageRGB);

% %% Plotting 3D 2
% 
% [ pcloud, distance ] = getCloud( msgs{queue{nfile+1,1}(1,3),1}{1,queue{nfile+1,1}(1,1)}.data , true);
% 
% subplot(y_s,x_s,3);
% surf(distance,'EdgeColor','none');
% view(0,-90);
% rotate3d off;
% 
% %% Plotting Image Color 2
% 
% subplot(y_s,x_s,4);
% preImage = queueToImage(msgs{queue{nfile+1,1}(2,3),1}{1,queue{nfile+1,1}(2,1)}.data,res_X,res_Y);
% imageRGB = normalizeRGB (preImage);
% image(imageRGB);

%% Plot masked

% imageMasked=nan(size(imageRGB,1),size(imageRGB,2));
subplot(y_s,x_s,3);
% for i=1:res_Y
%     for j=1:res_X
%         %if ~isnan(distance(i,j))
%             imageMasked(i,j)=imageRGB(i,j,1)*0.6+imageRGB(i,j,2)*0.3+imageRGB(i,j,3)*0.1;
%         %end
%     end
% end
% image(imageMasked);

imageFiltred = motionDetection(imageRGB, rgb_back);
image(imageFiltred);

%% Plot Moravec

% %imageMoravec=moravec(imageRGB);
% imageMoravec=moravec(imageMasked);
% imageMoravec=moravec(imageMoravec);
% 
% subplot(y_s,x_s,4);
% %normalizedMoravec = normalizeToOneWithBorder(imageMoravec);
% getCouplesOfPoints(imageMoravec,imageMoravec);
% 
% imagemor=zeros(size(imageMoravec,1),size(imageMoravec,2),3);
% for i=1:3
% imagemor(:,:,i)=imageMoravec(:,:);
% end
% 
% image(imagemor);
% something=imageMoravec;

end

function [couples] = getCouplesOfPoints(moravec1,moravec2,max_speed)

    moravec1=reduceMoravec(moravec1);
    moravec2=reduceMoravec(moravec2);

    if nargin < 3
        max_speed=75;
    end
    
    couples = 0;
        
end

function [reduceMoravec] = reduceMoravec(moravecImg)
    reduceMoravec=moravecImg;
    min = 0.3;
    for i=1:size(moravecImg,1)
        for j=1:size(moravecImg,2)
            if max(moravecImg(i,j,:) < min)
                reduceMoravec(i,j,:)=NaN;
            end
        end
    end    
end
 
% function [normPicture] = normalizeToOneWithBorder(picture,min,max)
% 
%     if nargin < 2
%         min = 0;
%         max = 1;
%     end
% 
%     pictureSize = size(picture);
%     normPicture=nan(pictureSize);
%     for i=1:pictureSize(1)
%         for j=1:pictureSize(2)
%             if max(picture(i,j,:) < min) || max(picture(i,j,:) > max)
%                 normPicture(i,j,:)=NaN;
%             else
%                 normPicture(i,j,:)=picture(i,j,:);
%             end
%         end
%     end
%     
%     smallest = min(normPicture(:,:,:));
%     scale = 1/(max(normPicture(:,:,:))-smallest);
%     for i=1:pictureSize(1)
%         for j=1:pictureSize(2)
%             for k=1:pictureSize(3)
%                 normPicture(i,j,k)=(normPicture(i,j,k)-smallest)*scale;
%             end
%         end
%     end
%     
% end

function [mask] = getMask(radius)
    
end