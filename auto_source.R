############################### DATA IMPORT #################################

# Les données sont importées sous forme de tableau. Première colonne : Nom du broker
# Les tarifs sont notés comme suit: Seuil Minimum,Seuil Maximum,Frais fixe,Frais Variables.
# les lignes ayant moins d'élément se verront compléter par 0.

d_broker= read.table(paste(getwd(),"/Data/Courtiers.txt", sep=""), header= TRUE, sep=" ",stringsAsFactors = FALSE)
d_historique = read.table(paste(getwd(),"/Data/d_historique.txt", sep=""),header= TRUE, sep="\t",stringsAsFactors = FALSE)
############################### CLASS SOURCING #################################

##### Sourcing main Classes ##########

source(paste(getwd(),"/Classes/Asset.R", sep=""), local= FALSE)
source(paste(getwd(),"/Classes/Broker.R", sep=""), local= FALSE)
source(paste(getwd(),"/Classes/Investment.R", sep=""), local= FALSE)
source(paste(getwd(),"/Classes/Portfolio.R", sep=""), local= FALSE)
source(paste(getwd(),"/Classes/User.R", sep=""), local= FALSE)

##### Underlying Classes Asset ##########

source(paste(getwd(),"/Classes/Stock.R", sep=""), local= FALSE)

##### Stategie sourcing ####

source(paste(getwd(),"/Strategies/ExpositionConstante.R", sep=""), local= FALSE)
source(paste(getwd(),"/Strategies/BuyAndHold.R", sep=""), local= FALSE)
       