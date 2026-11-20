#pragma once
#include <cmath>
#include <cstddef>
#include <limits>
namespace lord_sumi {
template <size_t N, size_t E> class RouteGraph {
 struct Edge { size_t from,to; double cost; };
 Edge edges_[E]; size_t count_=0;
 bool fault_=false;
public:
 bool add(size_t from,size_t to,double cost) {
  if(fault_) return false;
  if(from>=N||to>=N||!std::isfinite(cost)||cost<0||count_==E) {fault_=true;return false;}
  edges_[count_++]={from,to,cost}; return true;
 }
 bool fault() const {return fault_;}
 void reset(){count_=0;fault_=false;}
 struct Result {bool reachable; bool valid; double cost; size_t nodes[N]; size_t length;};
 Result shortest(size_t start,size_t goal) const {
  Result r={false,false,0,{},0};
  if(fault_||start>=N||goal>=N) return r;
  double dist[N]; size_t prev[N]; bool used[N]={};
  for(size_t i=0;i<N;++i){dist[i]=std::numeric_limits<double>::infinity();prev[i]=N;}
  dist[start]=0;
  for(size_t k=0;k<N;++k){
   size_t u=N;
   for(size_t i=0;i<N;++i)if(!used[i]&&(u==N||dist[i]<dist[u]))u=i;
   if(u==N||!std::isfinite(dist[u]))break;
   used[u]=true;
   if(u==goal)break;
   for(size_t j=0;j<count_;++j)if(edges_[j].from==u){
    double candidate=dist[u]+edges_[j].cost;
    if(!std::isfinite(candidate))return r;
    if(candidate<dist[edges_[j].to]){dist[edges_[j].to]=candidate;prev[edges_[j].to]=u;}
   }
  }
  r.valid=true;
  if(!std::isfinite(dist[goal]))return r;
  r.reachable=true;r.cost=dist[goal];
  size_t reverse[N];size_t len=0;
  for(size_t p=goal;p!=N&&len<N;p=prev[p]){reverse[len++]=p;if(p==start)break;}
  if(len==0||reverse[len-1]!=start){r.valid=false;r.reachable=false;return r;}
  r.length=len;
  for(size_t i=0;i<len;++i)r.nodes[i]=reverse[len-i-1];
  return r;
 }
};
}