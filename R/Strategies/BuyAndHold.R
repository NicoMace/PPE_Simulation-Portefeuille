
f_investment_quantity=function(t_cash,investment,Broker)
{
  asset_price=investment$get_investment_asset()$get_asset_price()
  investment_quantity=t_cash[1]%/%asset_price
  reste=t_cash[1]%%asset_price
  while (Broker$broker_comp_fees(investment_quantity,asset_price)>reste) {
    reste=reste+asset_price
    investment_quantity=investment_quantity-1
  }
  return(investment_quantity)
} 



#Calcul du cash restant dans le portefeuille
f_cash_restant=function(d2,broker,nb_positions,stock_price,t_cash)
{
  cash =t_cash[1] - stock_price[1]* f_nb_actions(t_cash[1],stock_price)-comp_broker_fees(d2,"BoursoramaClassic",nb_positions,stock_price[1])
  return(cash)
}


#Calcul des Profits and Loss
f_PL=function(d2,broker,nb_positions,stock_price)
{
  PL=nb_positions*(stock_price[2]-stock_price[1])-comp_broker_fees(d2,"BoursoramaClassic",nb_positions,stock_price[1])-comp_broker_fees(d2,"BoursoramaClassic",nb_positions,stock_price[2])
  return(PL)
}

#Calcul du rendement
f_rdt=function(PL,Kapital)
{
  r=PL/Kapital
  return(r)
}





f_ultimate = function(Kapital,m_frais_broker,broker,stock_price)
{
  nb_actions=f_nb_actions(Kapital,stock_price[1])
  PL= f_PL(m_frais_broker,broker,nb_actions,stock_price)
  rdt= f_rdt(PL,Kapital)
  cash_restant = f_cash_restant(m_frais_broker,broker,nb_actions,stock_price,Kapital)
  return(c("Nombre d'action : ",nb_actions," PL : ",PL, " rendement :", rdt, "cash restant : ", cash_restant))
}




t_cash= matrix(0)
t_cash[1]=10000

#l1= Investment$new(NATIXIS_SPOT,10,BoursoramaDecouverte,"20/12/2018")


# Compute nb of asset to buy. alpha is the exposure percentage
comp_asset_quantity= function(cash,asset, broker, alpha){
  
  asset_price= asset$get_asset_price()
  asset_quantity = alpha*cash %/% asset_price
  broker_fees= broker$broker_comp_fees(asset_quantity, asset_price)
  while(asset_price*asset_quantity + broker_fees >alpha*cash)
  {
    asset_quantity=asset_quantity-1
    broker_fees= broker$broker_comp_fees(asset_quantity, asset_price)
  }
  return(asset_quantity)
}

#
S_BnH = function(t_cash, asset, broker, alpha, Nb_Obs){
  
  for(i in 2:Nb_Obs)
  {

    asset_price= asset$get_asset_price()
    asset_quantity= comp_asset_quantity(t_cash,asset, broker, alpha) 
    broker_fees= broker$broker_comp_fees(asset_quantity, asset_price)
    print("lol")
    if (asset_quantity = 0){
      t_cash[i]=t_cash[i-1]-(asset_price*asset_quantity +broker_fees)
    }
  }
  return(t_cash)
}









