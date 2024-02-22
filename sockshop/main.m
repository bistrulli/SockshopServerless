%clear

N=10;
K=10;
TF=N*K;

%dimensione dipendi dal numero di nomi
X0=zeros(1,62);
MU=zeros(1,62);

X0(2)=1;

MU([2 4 8 11 12 15 16 21 22 28 29 33 34 38 39 43 44 48 49 53 54 58 59 ])=1./[1.0 0.0001 1.0 0.0001 1.0 0.0001 1.0 0.0001 1.0 0.0001 1.0 0.0001 1.0 0.0001 1.0 0.0001 1.0 0.0001 1.0 0.0001 1.0 0.0001 1.0 ]; 
NT=[1 1 1 1 1 1 1 1 1 1 1 1 ]*inf;
NC=[1 1 1 1 1 1 1 1 1 1 1 1 ]*inf;

[t,y,ssROde] = lqnODE(X0,MU,NT,NC);

% Bm=[];
% e=inf;
% while(e>0.01)
%     [X,ssRSim] = lqn(X0,MU,NT,NC,TF,1,1);
%     X0=X(:,end);
%     avgT=cumsum(ssRSim(1,:))./linspace(0,size(ssRSim(1,:),2),size(ssRSim(1,:),2));
% 
%     batches=reshape(ssRSim(1,1:end-1),N,K);
%     Bm=[Bm;mean(batches,2)];
% 
%     SEM = std(Bm)/sqrt(length(Bm));               % Standard Error
%     ts = tinv([0.025  0.975],length(Bm)-1);      % T-Score
%     CI = mean(Bm) + ts*SEM;                      % Confidence Intervals
%     e=(mean(Bm)-CI(1))/mean(Bm);
%     disp(e);
% end
% 
% Tb=mean(Bm);
% RTsim=X0(1)/Tb;

Tode=ssROde(1);
RTode=X0(2)/Tode;

% [Tb,RTsim;
%  Tode,RTode];

writematrix([Tode,RTode],"MPP.csv");
 
%system("java -jar /usr/local/bin/DiffLQN.jar model.lqn");