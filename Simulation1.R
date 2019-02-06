source("auto_source.R")
t_cash=matrix(0,4)
t_cash[1]=10000

NATIXIS_SPOT = L_stocks[[2]]
BoursoramaDecouverte = L_brokers[[1]]
ptf1=Portefeuille$new(BoursoramaDecouverte,0.20,0.15)

l1= Investment$new(NATIXIS_SPOT,10,BoursoramaDecouverte,"20/12/2018")
l2= Investment$new(L_stocks[[3]],10,ptf1$get_ptf_broker(),"20/12/2018")


ptf1$add_ptf_investment(c(l1,l2))
print(S_BnH(t_cash,NATIXIS_SPOT,BoursoramaDecouverte ,1,3))
