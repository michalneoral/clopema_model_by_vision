% find and show two close images (rgb and depth)
% show different time between

function [ order_images ] = multiplayer( msgs, nfile )

    offset = 0.1;

    topics={
    '/xtion1/depth/image_raw';
    '/xtion1/rgb/image_raw';
    };

    order_images = findMostClosed( msgs, topics, nfile);    
    size_of_topics = size(order_images,1);
    order_of_topics = zeros(size_of_topics,1);
    for i = 1:size_of_topics
        order_of_topics(i)=getTopicPosition(msgs, topics{i,1});
    end
    
    if order_images(:,1) >= offset
        for i=1:size_of_topics
            multiplayerSubplot(size_of_topics,i,order_of_topics(i),order_images(i,1),msgs,order_of_topics(1),order_images(1));
        end
    end
end