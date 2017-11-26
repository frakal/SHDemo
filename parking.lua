local current_place = redis.call("get", KEYS[1])
if current_place then return current_place end
local free_place = redis.call("lpop", "freeplaces") 
-- freeplaces is list holding free spaces, added in redis beforehand
if free_place == nil then return 'Sorry. no more parking places' end
redis.call("set", KEYS[1], free_place)
return free_place
