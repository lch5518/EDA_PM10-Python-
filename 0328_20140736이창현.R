#1
x <- sample(c(1,2,3,4,5,6),100,T)
hist(x)
install.packages('nortest')
library(nortest)
ad.test(x)

#2
x1 <- 0
num <- c(1:100)
for(i in num){
  x1[i] = mean(sample(c(1,2,3,4,5,6),5,T))  
}
hist(x1)
ad.test(x1)

#3
x2 <- 0
for(i in num){
  x2[i] = mean(sample(c(1,2,3,4,5,6),10,T))  
}
hist(x2)
ad.test(x2)

#4
x3 <- 0
for(i in num){
  x3[i] = mean(sample(c(1,2,3,4,5,6),20,T))  
}
hist(x3)

ds <- ad.test(x3)
ds$p.value



#ad.test의 p값과 n을 제목으로 출력할 것.
myfun <- function(n){
  y <- 0
  num <- c(1:100)
  for(i in num){
    y[i] = mean(sample(c(1,2,3,4,5,6),n,T))  
  }
  ad.test(y)
  hist(y,main = "일 때 정규근사")
  
}

myfun(50)
myfun(100)
myfun(200)
