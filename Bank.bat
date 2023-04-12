( 
 :: 進程數量
 echo 5
 :: 資源個數
 echo 6
 :: 最大資源數分別是
 echo 10 12 15 20 14 10

 :: P1~P5進程已經占用的資源量
 echo 1 0 2 1 3 0
 echo 2 1 0 5 0 0
 echo 1 2 1 0 1 0
 echo 0 0 1 2 1 2
 echo 0 0 0 1 0 0

 :: P1~P5進程最大資源需求量
 echo 2 1 2 3 0 1
 echo 3 1 0 1 2 3
 echo 4 1 2 1 0 5
 echo 1 2 0 9 9 1
 echo 0 1 1 15 10 8 ) | Banker_Algorithm.exe

pause
