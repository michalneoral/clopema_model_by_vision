% clopema_model_by_vision
% Michal Neoral

showNamesInDictionaty (path_to_bag_files);

bagfile = input ('Put name of bag file: ','s');
path_and_bagfile = strcat(path_to_bag_files, bagfile);
bag = ros.Bag(path_and_bagfile);
bag.info()
reader