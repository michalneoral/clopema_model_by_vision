function [] = showNamesInDictionaty( path )

    names=getNamesInDictionaty(path);
    for i=1:size(names,2)
        disp(names(i))
    end

end

