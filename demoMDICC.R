source('.../MDICC-main/MDICC-main/NetworkFusion.R') 
library(Rcpp)
library(parallel)
library(Matrix)

setwd(".../MDICC-main/MDICC-main/")
dyn.load("projsplx_R.dll")

# connect anaconda environment
library(reticulate)
use_virtualenv("...\\MDICC-main\\MDICC-main\\MDICC_env") 
Sys.setenv(RETICULATE_PYTHON=".../MDICC-main/MDICC-main/MDICC_env/Scripts/python.exe") 
use_python(".../MDICC-main/MDICC-main/MDICC_env/Scripts/python.exe", required=TRUE)
py_config()
py_available()
source_python("LocalAffinityMatrix.py")
source_python("score.py")
source_python("label.py")
source_python("preProcessing.py")

# set start point for runtime analysis of MDICC
start_time <- Sys.time()

setwd(".../MDICC-main/MDICC-main/data1/data1/brca/")
list <- list.files()
data <- data.frame()
data1 <- list()
X <- list()

for(i in list){
  path <- i
  data <- feature_selection_percentage(i, 0.33)

  data11 <- as.matrix(data)
  data1[[i]] = scale(data11, center=TRUE, scale=TRUE) 
  data2 = t(data1[[i]])
  d1 = dist(data2)
  d1 = as.matrix(d1)
  X[[i]] <- d1
}

k1 = 18 
k2 = 42  
k3 = 2  
c  = 3  

aff = list()
for(i in 1:3){ 
  a = as.matrix(X[[i]])
  xxx = testaff(a,k1)
  aff[[i]] = xxx
}

fusion = MDICC(aff,c = c,k = k2)

# end point of runtime analysis of MDICC
end_time <- Sys.time()
end_time - start_time

fusion_M = as.matrix(fusion)
#write.matrix(testaff(fusion_M, k1), file =".../MDICC-main/MDICC-main/data1/data1/fusion_affin.csv")

score = MDICCscore(fusion_M,k3,'.../MDICC-main/MDICC-main/data1/data1/label.csv','class1')
names(score) = c('RI','ARI','NMI','Accu','F1') 

label = MDICClabel(fusion_M,k3)
MDICCresult = list()
MDICCresult[['score']] = score
MDICCresult[['label']] = label

