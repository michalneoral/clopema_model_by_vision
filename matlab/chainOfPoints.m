function [ chain ] = chainOfPoints( startPoint, optFlow )

    chain = zeros(size(optFlow,2),2);
    chain(1,:) = startPoint;
    
    for i = 2:size(optFlow,2)
        chain(i,:)=getNextPoint(chain(i-1,:), optFlow, i);
    end

end

function [ nextPoint ] = getNextPoint(lastPoint, flow, number)
    nextPoint = [flow{1,number}(lastPoint(1),lastPoint(2),1) + lastPoint(1),flow{1,number}(lastPoint(1),lastPoint(2),2) + lastPoint(2)];
end