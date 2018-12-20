
f_investment_quantity=function(t_cash,asset_cost, asset_price,Broker)
{
  investment_quantity=t_cash[1]%/%asset_cost
  reste=Kapital%%asset_cost
  while (Broker$comp_broker_fees(investment_quantity,asset_cost)>reste) {
    reste=reste+asset_cost
    investment_quantity=investment_quantity-1
  }
  return(investment_quantity)
} 



#Calcul du cash restant dans le portefeuille
f_cash_restant=function(d2,broker,nb_positions,stock_price,Kapital)
{
  cash =Kapital - stock_price[1]* f_nb_actions(Kapital,stock_price)-comp_broker_fees(d2,"BoursoramaClassic",nb_positions,stock_price[1])
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

