#include <bits/stdc++.h>
using namespace std;
#define fo(i, a, n) for(int i=a; i<n; i++)
#define pb push_back 

map<int, pair<int, int>> createGrantChart(vector<int> arrival, vector<int> burst){
    map<int, pair<int, int>> mp;
    int index=0;
    fo(i, 0, arrival.size()){
        if(i==arrival[i]){
            mp[i+1]={index, index+burst[i]};
            index=burst[i];
        }
        else{
            int start=max(arrival[i], index);
            mp[i+1]={start, start+burst[i]};
            index=start+burst[i];
        }
    }
    return mp;
}

vector<int> getCompletionTime(map<int, pair<int, int>> mp){
    vector<int> completionTime;
    for(auto it: mp){
        completionTime.push_back(it.second.second);
    }
    return completionTime;
}
vector<int> getTurnAroundTime(map<int, pair<int, int>> mp, vector<int> arrival){
    vector<int> turnAroundTime;
    int i=0;
    for(auto it: mp){
        turnAroundTime.push_back(it.second.second-arrival[i]);
        i++;
    }
    return turnAroundTime;
}
vector<int> getWaitingTime(vector<int> turnAround, vector<int> burst){
    vector<int> waitingTime;
    fo(i, 0, burst.size()){
        waitingTime.push_back(turnAround[i]-burst[i]);
    }
    return waitingTime;
}
vector<int> getResponseTime(map<int, pair<int, int>> mp, vector<int> arrival){
    vector<int> responseTime;
    int i=0;
    for(auto it: mp){
        responseTime.push_back(it.second.first-arrival[i]);
        i++;
    }
    return responseTime;
}

double getAveragTurnAroundTime(vector<int> turnAround, int N){
    double avg=0;
    fo(i, 0, N){
        avg=avg+turnAround[i];
    }
    avg= avg/N;
    return avg;
}
double getAveragWaitingTime(vector<int> waitingTime, int N){
    double avg=0;
    fo(i, 0, N){
        avg=avg+waitingTime[i];
    }
    avg= avg/N;
    return avg;
}
int main(){
    cout<<"Input the no. of processes"<<endl;
    int N;
    cin>>N;
    cout<<endl;

    vector<int> burstTime(N);
    cout<<"Enter process burst time"<<endl;
    fo(i, 0, N){
        cout<<"P["<<i+1<<"]";
        int temp;
        cin>>temp;
        burstTime[i]=temp;
    }   

    cout<<endl;
    vector<int> arrivalTime(N);
    cout<<"Enter arrival time"<<endl;
    fo(i, 0, N){
        cout<<"P["<<i+1<<"]";
        int temp;
        cin>>temp;
        arrivalTime[i]=temp;
    }   
    
    cout<<endl;
    vector<int> turnAround = getTurnAroundTime(createGrantChart(arrivalTime, burstTime), arrivalTime);
    vector<int> responseTime = getResponseTime(createGrantChart(arrivalTime, burstTime), arrivalTime);
    vector<int> waitingTime = getWaitingTime(turnAround, burstTime);
    vector<int> CompletionTime = getCompletionTime(createGrantChart(arrivalTime, burstTime));


    // // map<int, pair<int, int>> mp = createGrantChart(arrivalTime, burstTime);
    // // for(auto it: mp){
    // //     cout<<it.first<<" "<<it.second.first<<" "<<it.second.second<<endl;
    // // }

    cout<<"AT = Arrival Time"<<endl;
    cout<<"BT = Burst Time"<<endl;
    cout<<"CT = Completion Time"<<endl;
    cout<<"TAT = Turn Around Time"<<endl;
    cout<<"WT = Waiting Time"<<endl;
    cout<<"RT = Response Time"<<endl;

    cout<<"\nProcess\t\tAT\tBT\tCT\tTAT\tWT\tRT"<<endl;

    fo(i, 0, N){
        cout<<"P["<<i+1<<"]"<<"\t\t"<<arrivalTime[i]<<"\t"<<burstTime[i]<<"\t"<<CompletionTime[i]<<"\t"<<turnAround[i]<<"\t"<<waitingTime[i]<<"\t"<<responseTime[i]<<endl;
    }
    cout<<endl;
    cout<<"Average Turn Around Time: "<<getAveragTurnAroundTime(turnAround, N)<<endl;
    cout<<"Average Waiting Time: "<<getAveragWaitingTime(waitingTime, N)<<endl;
}