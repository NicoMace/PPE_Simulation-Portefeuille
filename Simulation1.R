source("auto_source.R")
t_cash=matrix()

NATIXIS_SPOT = L_stocks[[2]]
BoursoramaDecouverte = L_brokers[[1]]
ptf1=Portefeuille$new(BoursoramaDecouverte,l1,0.20,0.15)

l1= Investment$new(NATIXIS_SPOT,10,BoursoramaDecouverte,"20/12/2018")
l2= Investment$new(L_stocks[[3]],10,ptf1$get_ptf_broker(),"20/12/2018")


ptf1$add_ptf_investment(l2)
