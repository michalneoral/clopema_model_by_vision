% find and show two close images (rgb and depth)
% show different time between

function [ order_images ] = multiplayer( msgs, nfile )

    topics={
    '/xtion1/depth/image_raw';
    '/xtion1/rgb/image_raw';
    '/xtion1/rgb/image_rect_color';
    };

    order_images = findMostClosed( msgs, topics, nfile);    
    size_of_topics = size(order_images,1);
    order_of_topics = zeros(size_of_topics,1);
    for i = 1:size_of_topics
        order_of_topics(i)=getTopicPosition(msgs, topics{i,1});
    end
    
    if order_images(:) ~= 0
        for i=1:size_of_topics
            multiplayerSubplot(size_of_topics,i,order_of_topics(i),order_images(i),msgs,order_of_topics(1),order_images(1))
        end
    end
end