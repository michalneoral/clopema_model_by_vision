% find and show two close images (rgb and depth)
% show different time between

function [ output ] = multiplayer( msgs, nfile )

%osetrit

    topics={
    '/xtion1/depth/image_raw';
    '/xtion1/rgb/image_raw';
    '/xtion1/depth/image_raw';
    };

    output = findMostClosed( msgs, topics, nfile);



end