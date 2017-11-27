for i=1,99,1 
do 
   redis.call("RPUSH","freeplaces",i)
end