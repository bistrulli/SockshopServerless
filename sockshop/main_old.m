clear

N=10;
K=10;
TF=N*K;

%dimensione dipendi dal numero di nomi
X0=zeros(1,62);
MU=zeros(1,62);

X0(2)=1;

MU([2 4 8 11 12 15 16 21 22 28 29 33 34 38 39 43 44 48 49 53 54 58 59 ])=1./[0.0299 0.0001 0.105 0.0001 0.0542 0.0001 0.0434 0.0001 0.0204 0.0001 0.1279 0.0001 0.0234 0.0001 0.031 0.0001 0.0532 0.0001 0.1048 0.0001 0.0467 0.0001 0.4 ]; 
NT=[1 1 1 1 1 1 1 1 1 1 1 1 ]*inf;
NC=[1 1 1 1 1 1 1 1 1 1 1 1 ]*inf;

names=["SSAdd","SSAddress","SSCart","SSCartQuery","SSCatQuery",...
        "SSCtlg","SSDel","SSGet","SSHome","SSItem","SSList"];

[t,y,ssROde] = lqnODE(X0,MU,NT,NC);

Tode=ssROde(1);
RTode=X0(2)/Tode;


NTLqn=[inf,sum(y(end,4:8)),sum(y(end,10:13)),...
          sum(y(end,14:19)),sum(y(end,20:26)),...
          sum(y(end,27:31)),sum(y(end,32:36)),...
          sum(y(end,37:41)),sum(y(end,42:46)),...
          sum(y(end,47:51)),sum(y(end,52:56)),...
          sum(y(end,57:62))];
NCopt=[inf*ones(size(y,1),1),sum(y(:,[4,8]),2),sum(y(:,[11,12]),2),...
           sum(y(:,[15,16]),2),sum(y(:,[21,22]),2),...
           sum(y(:,[28,29]),2),sum(y(:,[33,34]),2),...
            sum(y(:,[38,39]),2),sum(y(:,[43,44]),2),...
            sum(y(:,[48,49]),2),sum(y(:,[53,54]),2),...
            sum(y(:,[58,59]),2)];

%NTopt=[inf,ceil(NTLqn(2:end)./NCopt(end,2:end))];
%NTopt=[inf,ones(1,length(NT)-1)];
NTopt=[inf,ones(1,size(names,2))*80];

% [t2,y2,ssROde2] = lqnODE(X0,MU,[inf,ceil(NTLqn(2:end))],max(NCopt));
%  
% figure
% hold on
% plot(t,y)
% plot(t2,y2,'-.')

for i=1:length(names)
    disp([names(i),NTopt(i+1)])
    system(sprintf("sh ../%s/update.sh %d 100 1",names(i),NTopt(i+1)))
end