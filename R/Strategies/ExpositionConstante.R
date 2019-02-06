

S_EC_comp_investment_quantity_treshold= function(treshold,investment)
{
  investment_quantity_inf=treshold%/%investment$get_asset_price()
  investment_quantity_sup=investment_quantity_inf+1
  
  if (treshold-investment_quantity_inf*investment$get_asset_price()< investment_quantity_sup*investment$get_asset_price()-treshold)
  {
    return(investment_quantity_inf)
  }
  else
  {
    return(investment_quantity_sup)
  }
}

f_equilibrage=function(broker,investment,cash,treshold)
{
  delta_cash=0
  asset_quantity= investment$get_investment_quantity()
  asset_quantity_treshold=S_EC_comp_investment_quantity_treshold(treshold,investment$get_investment_asset()$get_asset_price())
  variation=asset_quantity_treshold-asset_quantity
  broker_fees = broker$broker_comp_fees()
    if(!is.null(broker_fees))
    {
      if(variation !=0)
      {
        if (broker_fees+ abs(variation)*investment$get_asset_price()<cash)
        {
          delta_cash= variation*investment$get_asset_price()+broker_fees
          asset_quantity = investment$get_investment_quantity()+variation
          
        }
      }
    }
  return(c(delta_cash,nb_action))
}

############################################ BODY 
Capital = 10000
T=4
cash=matrix(0.0,T,ncol=1)
cash[1]=Capital

stock_price = matrix(data = c(100,110,120,130))

f_ultimate= function(Objectif, Nb_obs, nb_stock_initial,t_cash,stock_price)
{
  nb_stock= matrix(0,nrow=Nb_obs)
  nb_stock[1]=nb_stock_initial
  for(i in 2:Nb_obs){
    
    val=f_equilibrage(d_broker,"BoursoramaClassic",Objectif,stock_price[i],nb_stock[i-1],cash[i-1])
    nb_stock[i]=val[2]
    cash[i]=cash[i-1]-val[1]
    
  }
  print(c("Exposition :", Objectif, "Nombre d'observation :", Nb_obs, "Nombre d'actions à t0 :",nb_stock_initial,"Capital initial", t_cash[1]))
  m=matrix(c(stock_price,nb_stock,cash),ncol=3)
  colnames(m)=c("Stockprice","   Nombre d'actions","    Capital")
  print(c("Gain de ", (cash[length(cash)]+nb_stock[length(nb_stock)]*stock_price[length(stock_price)]-cash[1])))
  return(m) 
}










