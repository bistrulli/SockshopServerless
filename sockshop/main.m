%clear

N=10;
K=10;
TF=N*K;

%dimensione dipendi dal numero di nomi
X0=zeros(1,62);
MU=zeros(1,62);

X0(2)=100;

MU([2 4 8 11 12 15 16 21 22 28 29 33 34 38 39 43 44 48 49 53 54 58 59 ])=1.0./[1.054613180771685 0.0001 1.0927543099100077 0.0001 0.9514319342877264 0.0001 1.0220376827518338 0.0001 0.9921933620787473 0.0001 1.218180081635334 0.0001 1.0190138657802208 0.0001 1.1537804970268 0.0001 0.9950603417257318 0.0001 1.0881959816988638 0.0001 1.0975508133906884 0.0001 0.9893983305454546 ]; 
NT=[1 1 1 1 1 1 1 1 1 1 1 1 ]*inf;
NC=[1 1 1 1 1 1 1 1 1 1 1 1 ]*inf;

names=["SSAdd","SSAddress","SSCart","SSCartQuery","SSCatQuery",
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
NTopt=[inf,ceil(NTLqn(2:end)./NCopt(2:end))];
NCopt=[inf,sum(y(end,[4,8])),sum(y(end,[11,12])),...
           sum(y(end,[15,16])),sum(y(end,[21,22])),...
           sum(y(end,[28,29])),sum(y(end,[33,34])),...
            sum(y(end,[38,39])),sum(y(end,[43,44])),...
            sum(y(end,[48,49])),sum(y(end,[53,54])),...
            sum(y(end,[58,59]))];

for i=1:length(names)
    disp([names(i),NTopt(i+1)])
    system(sprintf("sh ../%s/update.sh %d 100 1",names(i),NTopt(i+1)))
end