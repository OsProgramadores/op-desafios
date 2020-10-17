clear all;clc
ktour('a1');

function ktour(str)
    visits = zeros(8,8);
    st = [105-str(1) str2double(str(2))];
    visits(st(1),st(2)) = 1;
    disp(str)
    for move = 2:64
        [st,visits] = step(st,visits,move);
    end
end

function [n,visits] = step(s,visits,move)
    [x,y] = meshgrid(1:8,1:8);
    board =[x(:),y(:)];
    mo = [2 1;2 -1;1 2;1 -2;-1 2;-1 -2;-2 1;-2 -1];
    arr = [];
    for m=1:8
        c = s + mo(m,:);
        if ismember(c,board,'rows') && visits(c(1),c(2)) == 0
            arr = [arr;c];
        end
    end
    nmoves = zeros(size(arr,1),1);
    for a=1:size(arr,1)
        for m=1:8
            nc = arr(a,:) + mo(m,:);
            if ismember(nc,board,'rows') && visits(nc(1),nc(2)) == 0
                nmoves(a) = nmoves(a) + 1;
            end
        end
    end
    [~,i]=min(nmoves);
    n = arr(i,:);
    disp([char(105-n(1)),num2str(n(2))])
    visits(n(1),n(2)) = move;
end
