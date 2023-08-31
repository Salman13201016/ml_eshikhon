#Start - Loss & Profit Calculation problem

#Cake's flavour names are
c1="Back Forest Cake"
c2="Vanilla Cake"
c3="Red Velvet Cake"
c4="Lemon Sponge Cake"
c5="Chocolate Cake"

#Output-1 : Owner wants to visualize the each cake flavor types
print("\n1. Owner wants to visualize the each cake flavor types :")
print("Answer : Cake flavor types are - ")
print(c1,',',c2,',',c3,',',c4,',',c5,'\n')

#-------------------------------------- Inventory Cost ------------------------------------------------

#Raw matarial cost every cake for each pound
rm_c_c1 = 180
rm_c_c2 = 150
rm_c_c3 = 220
rm_c_c4 = 165
rm_c_c5 = 170

#Additional cost for every cake for each pound
transportCost = 150
spaceCost = 50
staffCost = 60

#Utility cost 3% on Transport and Raw Material Cost for each pound
utilityCost_c1 = ((rm_c_c1 + transportCost) * 3)/100
utilityCost_c2 = ((rm_c_c2 + transportCost) * 3)/100
utilityCost_c3 = ((rm_c_c3 + transportCost) * 3)/100
utilityCost_c4 = ((rm_c_c4 + transportCost) * 3)/100
utilityCost_c5 = ((rm_c_c5 + transportCost) * 3)/100

#Total Cost for every cake for each pound
totalCost_c1 = rm_c_c1 + transportCost + spaceCost + staffCost + utilityCost_c1
totalCost_c2 = rm_c_c2 + transportCost + spaceCost + staffCost + utilityCost_c2
totalCost_c3 = rm_c_c3 + transportCost + spaceCost + staffCost + utilityCost_c3
totalCost_c4 = rm_c_c4 + transportCost + spaceCost + staffCost + utilityCost_c4
totalCost_c5 = rm_c_c5 + transportCost + spaceCost + staffCost + utilityCost_c5

#Output-2: Owner wants to visualize the total inventory cost for each cake perpound
print("2. Owner wants to visualize the total inventory cost for each cake perpound :")
print("Answer : The total inventory cost for each cake perpound - ")
print(c1," = ",totalCost_c1)
print(c2," = ",totalCost_c2)
print(c3," = ",totalCost_c3)
print(c4," = ",totalCost_c4)
print(c5," = ",totalCost_c5,'\n')

#--------------------------------- Selling Cost -------------------------------------------------

#Selling price of the each cake per pound before discount 
pr_bf_d_c1 = 780
pr_bf_d_c2 = 600
pr_bf_d_c3 = 800
pr_bf_d_c4 = 650
pr_bf_d_c5 = 600

#Output-3 : Owner wants to visualize the selling price before discount for each cake per pound
print("3. Owner wants to visualize the selling price before discount for each cake per pound :")
print("Answer : The selling price before discount for each cake per pound - ")
print(c1," = ",pr_bf_d_c1)
print(c2," = ",pr_bf_d_c2)
print(c3," = ",pr_bf_d_c3)
print(c4," = ",pr_bf_d_c4)
print(c5," = ",pr_bf_d_c5,"\n")

#--------------------------------------------- After Discount -----------------------------------------

#Output-4 : Owner wants to visualize the selling price after discount for each cake per pound
print("4. Owner wants to visualize the selling price after discount for each cake per pound")
print("Answer : The selling price after discount for each cake per pound -")
print("The owner gives 5% discount on first 3 cakes and 7% discount on rest of the cake")

#Calculation of the selling price after discount for each cake per pound
pr_af_d_c1 = pr_bf_d_c1 - ((pr_bf_d_c1 * 5)/100)
pr_af_d_c2 = pr_bf_d_c2 - ((pr_bf_d_c2 * 5)/100)
pr_af_d_c3 = pr_bf_d_c3 - ((pr_bf_d_c3 * 5)/100)
pr_af_d_c4 = pr_bf_d_c4 - ((pr_bf_d_c4 * 7)/100)
pr_af_d_c5 = pr_bf_d_c5 - ((pr_bf_d_c5 * 7)/100)

print(c1," = ",pr_af_d_c1)
print(c2," = ",pr_af_d_c2)
print(c3," = ",pr_af_d_c3)
print(c4," = ",pr_af_d_c4)
print(c5," = ",pr_af_d_c5,"\n")

#----------------------------------------- Amount of Loss or Profit ------------------------------------

#Making total pound each flavour
m_t_p_c1 = 5
m_t_p_c2 = 7
m_t_p_c3 = 10
m_t_p_c4 = 5
m_t_p_c5 = 9

#Total Invertory Cost of making total pound each flavour
t_inv_c_c1 = totalCost_c1 * m_t_p_c1
t_inv_c_c2 = totalCost_c2 * m_t_p_c2
t_inv_c_c3 = totalCost_c3 * m_t_p_c3
t_inv_c_c4 = totalCost_c4 * m_t_p_c4
t_inv_c_c5 = totalCost_c5 * m_t_p_c5

#Total Selling Price of before discount making total pound each flavour
pr_bf_d_tp_c1 = pr_bf_d_c1 * m_t_p_c1
pr_bf_d_tp_c2 = pr_bf_d_c2 * m_t_p_c2
pr_bf_d_tp_c3 = pr_bf_d_c3 * m_t_p_c3
pr_bf_d_tp_c4 = pr_bf_d_c4 * m_t_p_c4
pr_bf_d_tp_c5 = pr_bf_d_c5 * m_t_p_c5

#Total Selling Price of after discount making total pound each flavour
pr_af_d_tp_c1 = pr_af_d_c1  * m_t_p_c1
pr_af_d_tp_c2 = pr_af_d_c2  * m_t_p_c2
pr_af_d_tp_c3 = pr_af_d_c3  * m_t_p_c3
pr_af_d_tp_c4 = pr_af_d_c4  * m_t_p_c4
pr_af_d_tp_c5 = pr_af_d_c5  * m_t_p_c5

#Find amount of profit each cake 
prf_c1 = pr_af_d_tp_c1 - t_inv_c_c1
prf_c2 = pr_af_d_tp_c2 - t_inv_c_c2
prf_c3 = pr_af_d_tp_c3 - t_inv_c_c3
prf_c4 = pr_af_d_tp_c4 - t_inv_c_c4
prf_c5 = pr_af_d_tp_c5 - t_inv_c_c5

#Output-5 : Owner wants to estimate total amount of profit after sell for each cake
print("5. Owner wants to estimate total amount of profit after sell for each cake :")
print("Answer : Total amount of profit after sell for each cake -")
print(c1," = ",prf_c1)
print(c2," = ",prf_c2)
print(c3," = ",prf_c3)
print(c4," = ",prf_c4)
print(c5," = ",prf_c5,"\n")

#----------------------------------------- Percentage of Loss or Profit ------------------------------------

#Find % of profit/loss after sell for each cake
prf_p_c1 = (prf_c1 / pr_af_d_tp_c1) * 100
prf_p_c2 = (prf_c2 / pr_af_d_tp_c2) * 100
prf_p_c3 = (prf_c3 / pr_af_d_tp_c3) * 100
prf_p_c4 = (prf_c4 / pr_af_d_tp_c4) * 100
prf_p_c5 = (prf_c5 / pr_af_d_tp_c5) * 100

#Output-6 : Owner wants to estimate % of profit/loss after sell for each cake
print("6. Owner wants to estimate % of profit/loss after sell for each cake")
print("Answer : % of profit/loss after sell for each cake -")
print(c1," = ",prf_p_c1)
print(c2," = ",prf_p_c2)
print(c3," = ",prf_p_c3)
print(c4," = ",prf_p_c4)
print(c5," = ",prf_p_c5,"\n")