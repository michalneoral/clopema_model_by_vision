function [ time ] = getTimeOfImage( msgs, n_topic, n_image )
    time = msgs{n_topic,2}{1,n_image}.time.time;
end