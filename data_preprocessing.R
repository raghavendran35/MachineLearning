

#importing the dataset
dataset = read.csv('Data.csv')


#unlike in python, indexing starts at 0

#deal with missing value in age column

#ifelse(pred,x,y)
#note the "ave" part of ifelse can have second parameter empty
#because of default value of mean
dataset$Age = ifelse(is.na(dataset$Age),
                      ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE )),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary,FUN = function(x) mean(x, na.rm = TRUE )),
                     dataset$Salary)

#Encodin categorical data
#change labels to factors and we can specify factors
dataset$Country = factor(x = dataset$Country, 
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
              
#c is a vector in R, labels does not matter, just use for default

dataset$Purchased = factor(x = dataset$Purchased, 
                         levels = c('No', 'Yes'),
                         labels = c(0, 1))
#Splitting dataset into training set and test set
#below installed caTools library, and then covered it as we dont need to install again
#install.packages('caTools')
library(caTools)    #activate caTools library
set.seed(123) #equivalent to random_state in python
split = sample.split(dataset$Purchased, SplitRatio = 0.8 ) 
#True in split means observation is in training set, split ratio is for training

training_set = subset(dataset, split == TRUE)
#rememeber which was True and False from dataset
test_set = subset(dataset, split == FALSE)

#####Featue Scaling
#note factors are not numeric, no feature scaling on columns with factors
#which are the categorical variables
training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])
