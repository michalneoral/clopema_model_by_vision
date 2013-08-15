function [  ] = showPlotOfDistancesInTime( dist, queue, points )

    timeStamp = zeros (1,size(queue,2));
    for i=1:size(queue,2)
        timeStamp(1,i)=queue{1, i}(1,2);        
    end
    fig=figure(1);
    clf(fig);
    hold all;
    for i=1:size(dist,1)
        plot( timeStamp, dist(i,:));
    end
    hold off

end

