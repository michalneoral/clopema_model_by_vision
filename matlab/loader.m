% clopema_model_by_vision
% Michal Neoral

nfiles=showNamesInDictionaty (path_to_bag_files);
if nfiles==0
    sprintf('No files in %s or no access',path_to_bag_files)
else
    bagfile = input ('Put name of bag file: ','s');
        path_and_bagfile = strcat(path_to_bag_files, bagfile);
        bag = ros.Bag(path_and_bagfile);
        bag.info()
        reader
end