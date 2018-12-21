#charger la librairie
library(R6)
#version du package > 1.0.1 -- classes portables
packageVersion("R6")

Portefeuille <- R6Class(
  "Portefeuille",
  public = list(
    #Constructor
    initialize = function(ptf_broker,ptf_list_investments,ptf_expected_return, ptf_expected_risk)
    {
      private$ptf_broker= ptf_broker
      private$ptf_expected_return = ptf_expected_return
      private$ptf_expected_risk = ptf_expected_risk
      
      private$ptf_list_investments= ptf_list_investments
      
      private$ptf_real_return = NA
      private$ptf_real_risk = NA
    },
    
    #ACCESSEUR
    get_ptf_broker= function(){
      return(private$ptf_broker)
    },
    get_ptf_list_investments = function(){
      return(private$ptf_list_investments)
    },
    get_ptf_expected_return = function() {
      return(private$ptf_expected_return)
    },
    get_ptf_expected_risk = function() {
      return(private$ptf_expected_risk)
    },
    get_ptf_real_return = function() {
      return(private$ptf_real_return)
    },
    get_ptf_real_risk = function() {
      return(private$ptf_real_risk)
    },
    set_ptf_broker= function(ptf_broker){
      private$ptf_broker= ptf_broker
    },
    set_ptf_list_investments = function(ptf_list_investments){
      private$ptf_list_investments= ptf_list_investments
    },
    set_ptf_expected_return = function(ptf_expected_return) {
      private$ptf_expected_return = ptf_expected_return
    },
    set_ptf_expected_risk = function(ptf_expected_risk) {
      private$ptf_expected_risk = ptf_expected_risk
    },
    set_ptf_real_return = function(ptf_real_return) {
      private$ptf_real_return = ptf_real_return
    },
    set_ptf_real_risk = function(ptf_real_risk) {
      private$ptf_real_risk = ptf_real_risk
    },
    
    ###### Methode
    add_ptf_investment = function(ptf_investment)
    {
      private$ptf_list_investments= c(private$ptf_list_investments,ptf_investment)
    }
  ),
  #membres privé
  private = list(
    #champs
    ptf_broker = NA,
    
    ptf_expected_return = NA,
    ptf_expected_risk = NA,
    ptf_real_return = NA,
    ptf_real_risk = NA,
    
    ptf_list_investments = list()
    
  )
  
)

