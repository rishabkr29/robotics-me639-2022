close all; clear all; clc;
%th1 = 0 ;th2 = pi/4 ; th3 = pi/4;
L1 = 2; L2 = 2; L3 = 2;
x = 2; 
y = 2;
for  x= 0:0.1:8
%inverse kinematics 
[th1, th2, th3] = IK_RR(x,y,L1,L2,L3);
%Jacobian Matrix
J = [-L1*sin(th1), -L2*sin(th2), -L3*sin(th3);
      L1*cos(th1), L2*cos(th2),  L3*sin(th3);];
%eigen values and vectors
[V,D] = eig(J*J');
ev = eig(J*J'); %eigen Vector
t1 = atan2(V(2,2),V(1,2));
xe = sqrt(max(abs(ev)));
ye = sqrt(min(abs(ev)));
%Forward kinamatics
x = L1*cos(th1) + L2*cos(th2)+ L3*cos(th3);
y = L1*sin(th1) + L2*sin(th2)+ L3*sin(th3);
plot(0,0,'ko','MarkerFaceColor','k','MarkerSize',8)
hold on 
plot([0, L1*cos(th1),x],[0,L1*sin(th1),y],'r-o','linewidth',2.5,'MarkerFaceColor','b','MarkerSize',8)
%Velocity or Manipubility 
aa = [cos(t1), -sin(t1); sin(t1), cos(t1)]*[xe*cosd(0:360)/xe; ye*sind(0:360)/xe];
plot(x+aa(1,:),y+aa(2,:),'b-');
hold on 
%Force ellipsoid
bb = [cos(t1), -sin(t1); sin(t1), cos(t1)]*[ye*sind(0:360)/xe; xe*cosd(0:360)/xe];
plot(x+bb(1,:),y+bb(2,:),'m- ');
axis([-1.5*(L1+L2) 1.5*(L1+L2) -1.5*(L1+L2) 1.5*(L1+L2) ]);
axis square
grid on 
hold off
pause(0.5)
end
%Inverse kinematics 
function [th1, th2, th3] = IK_RR(x,y,L1,L2,L3)
l =sqrt(x^2+y^20); th1 = 0; th2 = 0; th3 = 0;
c2 = (x^2 + y^2 - L1^2 - L2^2)/(2*L1*L2);
s2 = -sqrt(1-c2^2);
if (l< (L1+L2))
   th1 = wrapTo2Pi(atan2(y,x) -  atan2(L2*s2, L1+L2*c2));  
   th2 = wrapTo2Pi(atan2(s2,c2)); 
end
end


