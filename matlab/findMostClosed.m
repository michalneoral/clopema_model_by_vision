% Find closed time and return number of closed image

function [ nclose ] = findMostClosed( msgs, topics, nfile )

    quantity_of_topics = size(topics,1);
    order_of_topics = zeros (quantity_of_topics,1);
    nclose = zeros(quantity_of_topics,1);
    
    for i = 1:quantity_of_topics
        order_of_topics(i)=getTopicPosition(msgs, topics{i,1});
    end
    
    nclose(1) = nfile;
    if nfile > 0 && nfile < size(msgs{order_of_topics(1),2},2);
    time = getTimeOfImage(msgs, order_of_topics(1), nfile);
        for i = 2:quantity_of_topics
            nclose(i) = getMostClosed( time, msgs, order_of_topics(i), nfile );
        end
    else
        disp('Too big put number of images');
    end
end

