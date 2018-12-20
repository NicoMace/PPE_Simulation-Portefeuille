source("auto_source.R")
t_cash=matrix()

NATIXIS_SPOT = L_stocks[[2]]
NATIXIS_SPOT$set_asset_price(NATIXIS_SPOT$get_asset_cost())
BoursoramaDecouverte = L_brokers[[1]]

l1= Investment$new(NATIXIS_SPOT,10,BoursoramaDecouverte,"20/12/2018")
