function [  ] = calcHodiny( hodiny )
    obedMin=40;
    sumMin=0;
    for i=1:size(hodiny,1)
        startDay=hodiny(i,1);
        endDay=hodiny(i,2);
        minStartDay=mod(startDay,100);
        minEndDay=mod(endDay,100);
        hodStartDay=(startDay-minStartDay)/100;
        hodEndDay=(endDay-minEndDay)/100;
        sumMin= sumMin+(hodEndDay-hodStartDay)*60+(minEndDay-minStartDay)-obedMin;
    end
disp(sumMin/60)

end

