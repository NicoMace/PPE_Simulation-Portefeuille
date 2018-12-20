#charger la librairie
d_historique = read.table(paste(getwd(),"/Data/d_historique.txt", sep=""),header= TRUE, sep="\t",stringsAsFactors = FALSE)
library(R6)
#version du package > 1.0.1 -- classes portables
packageVersion("R6")

Stock <- R6Class(
  "Stock",
  inherit = Asset,
  
  public = list(
    #Constructor
    initialize = function(asset_code,
                          asset_cost,
                          asset_price,
                          stock_ISIN,
                          stock_currency,
                          stock_flow)
    {
      private$asset_cost = asset_cost
      private$asset_price = asset_price
      private$asset_code = asset_code
      
      private$stock_ISIN = stock_ISIN
      private$stock_currency = stock_currency
      private$stock_flow = stock_flow
    },
    
    #ACCESSEUR
    get_stock_ISIN = function() {
      return(private$stock_ISIN)
    },
    get_stock_currency = function() {
      return(private$stock_currency)
    },
    get_stock_flow = function() {
      return(private$stock_flow)
    },
    set_stock_ISIN = function(stock_ISIN) {
      private$stock_ISIN = stock_ISIN
    },
    set_stock_currency = function(stock_currency) {
      private$stock_currency = stock_currency
    },
    set_stock_flow = function(stock_flow) {
      private$stock_flow = stock_flow
    }
  ),
  #membres privé
  private = list(
    #champs
    stock_ISIN = NA,
    stock_currency = NA,
    stock_flow = NA
    
  )
  
)
############################ A FINIR ##################
init_stocks = function()
{
  L_stocks= list()
  for (j in 2:length(d_historique[1,]))
  {
    assign(noquote(colnames(d_historique)[j]),
      Stock$new(colnames(d_historique)[j],d_historique[1, j],
                d_historique[1, length(d_historique[, 1])],
        "CODE","€",0))
    L_stocks= c(L_stocks,get(noquote(colnames(d_historique)[j])))
  }
  return(L_stocks)
}
L_stocks=init_stocks()
#CAC_40 = Stock$new("NATIXIS_SPOT",100,110, "NAT_CAC40","$", 0)
