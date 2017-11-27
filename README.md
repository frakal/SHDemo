# SHDemo
3 tasks for a SeekandHit demo

## Toy Robot
Run the script robot.py and enter commands in the form of
PLACE X,Y,F MOVE LEFT RIGHT REPORT

## Redis/lua
First run 
```
redis-cli --eval generate_free_places.lua
```
to make a list of free spaces, then 
```
redis-cli --eval parking.lua plane:n
```
to assing a parking place to the plane number n.
