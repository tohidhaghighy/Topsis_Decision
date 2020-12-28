import numpy as np
import math

class Topsis:
    def __init__(self,alternative_count,criteria_count):
        self.alternative_count=alternative_count
        self.criteria_count=criteria_count

    def make_matrix(self):
        topsis_table=[]
        for i in range(1,self.alternative_count+1):
            alternative_table=[]
            for j in range(1,self.criteria_count+1):
                alternative_table.append(int(input("Alternative {} Criteria {} :".format(i,j))))
            topsis_table.append(alternative_table)

        return topsis_table

    def make_normalize_matrix(self,topsis_matrix):
        numpy_topsis_matrix=np.array(topsis_matrix)
        x_normed = numpy_topsis_matrix / numpy_topsis_matrix.sum(axis=0)
        return x_normed
        
    def get_ahp_vector(self):
        ahp_list=[]
        for i in range(self.criteria_count):
            ahp_list.append(float(input("Enter {} Criteria Point :".format(i+1))))
        return ahp_list

    def multiply_ahp_into_topsis(self,ahp_vector,topsis_table):
        return topsis_table*ahp_vector
 
    def Get_Ideal_Postive(self,topsis_matrix):
        return topsis_matrix.max(axis=0)
    
    def get_Ideal_negative(self,topsis_matrix):
        return topsis_matrix.min(axis=0)
    
    def Find_Distance_Postive_Matrix(self,postive_ideal,matrix):
        distance_postive=[]
        for i,criteria in enumerate(matrix):
            sum_negative=0
            for j in criteria:
                a=np.sqrt(j**2+postive_ideal[i-1]**2)
                sum_negative+=a
            distance_postive.append(sum_negative)
        return distance_postive
    
    def Find_Distance_negative_Matrix(self,negative_ideal,matrix):
        distance_negative=[]
        for i,criteria in enumerate(matrix):
            sum_negative=0
            for j in criteria:
                a=np.sqrt(j**2+negative_ideal[i-1]**2)
                sum_negative+=a
            distance_negative.append(sum_negative)
        return distance_negative
    
    def Closness_Coeficent(self,negative_distance,postive_distance):
        array_negative=np.array(negative_distance)
        array_postive=np.array(postive_distance)
        cc=array_negative/(array_postive+array_negative)
        return cc

    

if __name__ == "__main__":
    alternative_count=int(input("Count of Alternative : "))
    Criteria_count=int(input("Count of Criteria : "))


    # get negative criteria column
    negative_column=[]
    for negative in range(0,Criteria_count):
        ans=input("is {} Criteria column negative :".format(negative+1))
        if(ans=="y"):
            negative_column.append(-1)
        else:
            negative_column.append(1)

    print(negative_column)
    
    #end negative column

    #get matrix criteria and alternative
    topsis = Topsis(alternative_count,Criteria_count)
    topsis_tab=topsis.make_matrix()

    #end get alternative


    #normalize matrix for sum of column and devide to sum
    normalize_matrix=topsis.make_normalize_matrix(topsis_tab)
    # get weight vector
    ahp_vector=topsis.get_ahp_vector()
    #end

    multi_ahp_topsis=topsis.multiply_ahp_into_topsis(ahp_vector,normalize_matrix)

    print(multi_ahp_topsis)
    add_negative_totopsis = multi_ahp_topsis*negative_column

    print(add_negative_totopsis)
    #get postive ideal answer
    postive_ideal=topsis.Get_Ideal_Postive(add_negative_totopsis)
    negative_ideal=topsis.get_Ideal_negative(add_negative_totopsis)


    
    print("----------------------------------------------")

    print(postive_ideal)

    print("----------------------------------------------")

    print(negative_ideal)

    # find distance 

    print("---------------postive-------------------------")

    poistive_distance=topsis.Find_Distance_Postive_Matrix(postive_ideal,multi_ahp_topsis)
    print(poistive_distance)
    
    print("-----------------negative-----------------------")

    negative_distance=topsis.Find_Distance_negative_Matrix(negative_ideal,multi_ahp_topsis)
    print(negative_distance)

    
    print("-----------------Closeness Coefisent-----------------------")
    final_cc=topsis.Closness_Coeficent(poistive_distance,negative_distance)

    print(final_cc)

    #نتیجه اخر هر چه به 1 نزدیک تر شود جواب ایده ال تر خواهد بود 









    












