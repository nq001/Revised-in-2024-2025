 #IMPLEMENTATION OF FCFS ON (CPU SCHEDULING) 
import numpy as mm
# Calculate Waiting time of FCFS
def findwaitTime(Process,n,Burst,WT):
    WT[0]=0
    for i in range(1,n):
        WT[i]=Burst[i-1]+WT[i-1]

 # Calculate Tournaround Time of FCFS   
def findTAT(Process,n,Burst,WT,TAT):
    for i in range(n):
        TAT[i]= WT[i]+Burst[i]
# Calculate the average of Waiting and Turnaround

def avgWaitTAT(BT,n,WT,TAT,AVG_WT,AVG_TAT):
    AVG_WT= mm.mean(WT)
    AVG_TAT=mm.mean(TAT)
    print("Process Burst Time"+"Waiting Time"+"TurnAround")
    for i in range(n):
        print(" P"+str(i+1)+"\t"+str(BT[i])+"\t"+str(WT[i])+"\t\t"+str(TAT[i]))
    print("Average of Waiting Time:"+str(AVG_WT))
    print("Average of Turnaround Time:"+str(AVG_TAT))


#Input: BurtTime
BT=[24,9,4]
Process =[1,2,3]
n=len(Process)
WT=[0]*n
TAT=[0]*n
AVG_WT=0
AVG_TAT=0
findwaitTime(Process,n,BT,WT)
findTAT(Process, n,BT,WT,TAT)
avgWaitTAT(BT,n,WT,TAT,AVG_WT,AVG_TAT)


# Assignment:
    # -- SJF Premptive vs nonPremptive 
    # -- RR
    # -- (wait time) + tournaround time
    # -- (recognize inputs)
