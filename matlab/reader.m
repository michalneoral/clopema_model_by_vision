% clopema_model_by_vision
% Michal Neoral
topics = {'/joint_states'; '/tf'; '/xtion1/depth_registered/camera_info'; '/xtion1/depth_registered/image'; '/xtion1/depth_registered/image/compressedDepth';'/xtion1/rgb/image_color';'/xtion1/rgb/image_color/theora';'/xtion1/rgb/image_mono';'/xtion1/rgb/image_mono/theora';'/xtion1/rgb/image_raw';'/xtion1/rgb/image_raw/theora';'/xtion1/rgb/image_rect';'/xtion1/rgb/image_rect/theora';'/xtion1/rgb/image_rect_color';'/xtion1/rgb/image_rect_color/theora';'/xtion1/depth_registered/points';};

[msgs] = bagToStruct(bag,topics);
